import json
import socket
from io import BufferedReader
from custom_request import Request
from custom_response import Response
from log.log import get_log

log = get_log(__name__)


class CustomHTTPHandler:
    def __init__(self, conn: socket.socket):
        self.conn = conn

    def parse_request(self) -> Request | None:
        try:
            with self.conn.makefile('rb') as rfile:
                method, path, version = self.parse_request_line(rfile)
                headers = self.parse_headers(rfile)
                self.handle_request(Request(method, path, version, headers, rfile), self.conn)
        except Exception as e:
            log.exception(e)

    def parse_request_line(self, rfile: BufferedReader) -> tuple:
        MAX_LINE = 16  # maximum number of bytes accepted from the user
        request = rfile.readline(MAX_LINE + 1)  # b'GET / HTTP/1.1\r\n'
        if len(request) > MAX_LINE:
            raise Exception('Length of request line!')
        method, path, version = request.decode('utf-8').split()
        return method, path, version

    def parse_headers(self, rfile: BufferedReader) -> dict:
        headers = {}
        buf = rfile.readline()
        while b'\r\n' != buf:
            header, content = buf.decode('utf-8').split(':', 1)
            headers[header] = content.strip()
            buf = rfile.readline()
        return headers

    def handle_request(self, req: Request, conn: socket.socket):
        if req.method == 'GET':
            response = Response(200, 'OK', {"response": "Hello, World!"})
            body = json.dumps(response.body).encode('utf-8')

            response_content = (
                                   f'HTTP/1.1 {response.status} {response.reason}\r\n'
                                   f'Content-Type: application/json\r\n'
                                   f'Content-Length: {len(body)}\r\n'
                                   f'Connection: close\r\n'
                                   f'\r\n'
                               ).encode('utf-8') + body

            self.conn.sendall(response_content)

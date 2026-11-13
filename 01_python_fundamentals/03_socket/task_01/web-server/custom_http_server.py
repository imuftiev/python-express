import socket
import threading
from log.log import get_log
from custom_http_handler import CustomHTTPHandler

log = get_log(__name__)


class CustomHTTPServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def create_server(self) -> None:
        try:
            server = socket.create_server((self.host, self.port), family=socket.AF_INET)
            while True:
                conn, _ = server.accept()
                log.info(f'CONNECTION - {_[0]}:{_[1]}')
                handler = CustomHTTPHandler(conn)
                thread = threading.Thread(
                    target=handler.parse_request
                )
                thread.start()
        except Exception as e:
            log.exception(e)



if __name__ == "__main__":
    chs = CustomHTTPServer('localhost', 8080)
    chs.create_server()

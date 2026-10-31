import json
import threading
import socket
from db import get_connection
from user import User

IP = 'localhost'
PORT = 8080
server = socket.create_server((IP, PORT), family=socket.AF_INET)


def handle_request(client: socket.socket, address: tuple) -> None:
    print(f'[*] The client has connected {address[0]}:{address[1]}')
    while True:
        client.send(b'Type your name')
        data = client.recv(4096).decode('utf-8')
        if not data:
            break
        try:
            response = handle_client(data)
        except Exception as e:
            print(f"Database error: {e}")

            response = {
                "status": 500,
                "body": str(e)
            }

        client.sendall(json.dumps(response, ensure_ascii=False).encode("utf-8"))


def handle_client(name: str) -> dict | Exception:
    response_status = {}
    user = User(name)
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute('insert into users (name) values (%s)', (user.name,))
            conn.commit()
    response_status["status"] = response_status.get("status", 200)
    response_status["body"] = response_status.get("body", user.name)
    return response_status


def main() -> None:
    print(f'[*] Server started {IP}:{PORT}')
    while True:
        client, address = server.accept()
        thread = threading.Thread(target=handle_request, args=(client, address))
        thread.start()


main()

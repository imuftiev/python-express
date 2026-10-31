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
        user = handle_client(str(data))
        client.send(('Hello, ' + str(user)).encode('utf-8'))


def handle_client(name: str) -> User:
    user = User(name)
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute('insert into users (name) values (%s)', (name,))
            conn.commit()
    return user


def main() -> None:
    print(f'[*] Server started {IP}:{PORT}')
    while True:
        client, address = server.accept()
        thread = threading.Thread(target=handle_request, args=(client, address))
        thread.start()


main()

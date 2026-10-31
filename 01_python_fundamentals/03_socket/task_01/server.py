import threading
import socket

IP = 'localhost'
PORT = 8080
server = socket.create_server((IP, PORT), family=socket.AF_INET)

def handle_client(client: socket.socket, address: tuple) -> None:
    print(f'[*] The client has connected {address[0]}:{address[1]}')
    while True:
        data = client.recv(4096)
        if not data:
            break
        print(f'Client: ', data.decode('utf-8'))
        client.send(b'ACK')


def main() -> None:
    print(f'[*] Server started {IP}:{PORT}')
    while True:
        client, address = server.accept()
        thread = threading.Thread(target=handle_client, args=(client, address))
        thread.start()


main()

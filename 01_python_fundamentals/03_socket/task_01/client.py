import socket


IP = 'localhost'
PORT = 8080

client = socket.create_connection((IP, PORT))

while True:
    response = client.recv(4096)
    print(response.decode('utf-8'))
    data = str(input('Enter: '))
    client.send(data.encode('utf-8'))

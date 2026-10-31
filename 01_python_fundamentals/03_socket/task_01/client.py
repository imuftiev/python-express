import socket


IP = 'localhost'
PORT = 8080

client = socket.create_connection((IP, PORT))

while True:
    data = input('Enter the message you want to send: ')
    client.send(data.encode('utf-8'))
    response = client.recv(4096)
    print('Server response: ', response.decode('utf-8'))
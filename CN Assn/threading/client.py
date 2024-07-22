import socket
port = 50000
host = '127.0.0.1'
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((host,port))
while True:
    msg = input('Enter message or bye to close connection : ')
    client.send(msg.encode())
    if msg == 'bye':
        break
    result = client.recv(2048).decode()
    print('Server Response : ', result)

print('Connection closed')
client.close()
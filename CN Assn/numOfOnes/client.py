import socket
host = '127.0.0.1'
port = 50000
portClient = 8000
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.bind((host,portClient))
client.connect((host,port))

while True:
    msg = input('Enter message : ')
    if msg == 'Quit':
        break
    client.send(msg.encode())
    result = client.recv(2048).decode()
    print('Server Response : ',result)
print('Conection closed...')
client.close()
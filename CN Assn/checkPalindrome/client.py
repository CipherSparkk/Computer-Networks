import socket
port = 50000
portClient = 8000
host = '127.0.0.1'
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.bind((host,portClient))
client.connect((host,port))
while True:
    msg = input('Enter string : ')
    if msg ==   'Quit':
        break
    client.send(msg.encode())
    result = client.recv(2048).decode()
    print('Server Response : ',result)

print('Connection closed')
client.close()
import socket

port = 50000
host = '127.0.0.1'
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((host,port))

while True:
    ip = input('Enter IP address : ')
    client.send(ip.encode())
    if ip == 'bye':
        break
    result = client.recv(2048).decode()
    print('Server Response : ', result)
    
print('Connecton closed')
client.close()
import socket
port = 50000
portClient = 8000
host = '127.0.0.1'
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.bind((host,portClient))
client.connect((host,port))
codeword = input('Enter codeword : ')
key = input('Enter key : ')
client.send(f'{codeword} {key}'.encode())
result = client.recv(2048).decode()
print('Server Response : ',result)
print('Connection closed')
client.close()
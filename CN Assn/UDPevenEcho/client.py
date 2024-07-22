import socket
port = 50000
portClient = 8000
host = '127.0.0.1'
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.bind((host,portClient))

while True:
    msg = input('Enter string : ')
    client.sendto(msg.encode(),(host,port))
    if msg == 'bye':
        break
    result, addr = client.recvfrom(2048)
    print('Server Response : ', result.decode())

print('Connection Closed')
client.close()
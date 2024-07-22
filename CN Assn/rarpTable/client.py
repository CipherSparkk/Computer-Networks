import socket
host = '127.0.0.1'
port = 50000
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((host,port))
while True:
    mac_addr = input('Enter mac address : ')
    client.send(mac_addr.encode())
    if mac_addr == 'bye':
        break
    result = client.recv(2048).decode()
    print('IP Address : ', result)
print('Connection closed')
client.close()
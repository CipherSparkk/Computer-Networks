import socket
port = 50000
host = '127.0.0.1'
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind((host,port))
while True:
    conn, addr = server.recvfrom(2048)
    msg = conn.decode()
    if msg == 'bye':
        break
    str1 = ''
    if len(msg)%2 == 0:
        i=1
    else:
        i=0
    while i<len(msg):
        str1 = str1 + msg[i]
        i+=2
    server.sendto(str1.encode(),addr)
print('Connection closed from client')
server.close()

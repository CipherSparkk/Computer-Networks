import socket
port = 50000
host = '127.0.0.1'
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind((host, port))
while True:
    conn,addr = server.recvfrom(2048)
    msg = conn.decode()
    if msg == 'bye':
        break
    cnt = 0
    i=0
    while i<len(msg):
        if msg[i] == '1':
            cnt+=1
        i+=1
    
    cnt = str(cnt)
    server.sendto(cnt.encode(),addr)
print('Connection closed form client')
server.close()
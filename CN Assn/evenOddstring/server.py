import socket
port = 50000
host = '127.0.0.1'
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
server.bind((host,port))
server.listen(5)
conn,addr = server.accept()
while True:
    msg = conn.recv(2048).decode()
    if msg == 'bye':
        break
    if len(msg)%2 == 0:
        i=1
    else:
        i=0
    str1 = ''
    while i<len(msg):
        str1 = str1 + msg[i]
        i+=2
    conn.send(str1.encode())
print('Connection closed from client')
conn.close()
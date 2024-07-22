import socket
host = '127.0.0.1'
port = 50000
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR, 1)
server.bind((host,port))
server.listen(2)
print('Server is listening...')
conn,addr = server.accept()
while True:
    msg = conn.recv(2048).decode()
    if msg == 'Quit':
        break
    print('Message from client : ', msg)
    i=0
    cnt=0
    while i<len(msg):
        if msg[i] == '1':
            cnt += 1
        i+=1
    cnt = str(cnt)
    conn.send(cnt.encode())

print('Connection closed from Client!!!')
conn.close()
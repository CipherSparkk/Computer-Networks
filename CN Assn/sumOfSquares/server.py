import socket

port = 50000
host = '127.0.0.1'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server.bind((host,port))
server.listen(2)
print('Server is listening...')

conn,addr = server.accept()

while True:
    msg = conn.recv(2048).decode()
    print('Message from client : ',msg)
    if msg == 'Quit':
        break
    msg = int(msg)
    sum = 0
    i=1
    while i<=msg:
        res = i*i
        sum += res
        i+=1
    sum = str(sum)
    conn.send(sum.encode())

print('Connection closed from client!!!')
conn.close()
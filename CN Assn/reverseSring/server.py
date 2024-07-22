import socket
port = 50000
host = '127.0.0.1'
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
server.bind((host,port))
server.listen(2)
print('Server is listening...')
conn,addr=server.accept()
while True:
    msg = conn.recv(2048).decode()
    if msg == 'Quit':
        break
    str1 =''
    i=0
    j=len(msg)-1
    print('Message Received : ',msg)
    while j>=0:
        str1 = str1 + msg[j]
        i+=1
        j-=1

    conn.send(str1.encode())
print('Connection closed form Client...')
conn.close()
    
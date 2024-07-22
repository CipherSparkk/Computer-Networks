import socket
port = 50000
host = '127.0.0.1'
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((host,port))
server.listen(2)
print('Server is listening...')
conn,addr = server.accept()
while True:
    msg = conn.recv(2048).decode()
    if msg == 'Quit':
        break
    print('Message from client : ',msg)
    i=0
    str1 = 'This is Palindrome'
    j = len(msg)-1
    while i<j:
        if msg[i] != msg[j]:
            str1 = 'This is not a Palindrome'
            break
        i+=1
        j-=1
    
    conn.send(str1.encode())
print('Connection closed from Client')
conn.close()
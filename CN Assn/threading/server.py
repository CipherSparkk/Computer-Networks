import socket
import threading

def handle_client (client,addr,num):
    while True:
        msg = client.recv(2048).decode()
        if msg == 'bye':
            break
        result = input(f'Enter Response for client {i} : ')
        client.send(result.encode())
    print(f'Client {num} disconnected')
    client.close()

    
port = 50000
host = '127.0.0.1'
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((host,port))
server.listen(5)
print('Server is listening...')
i=0
while True:
    conn,addr = server.accept()
    i+=1
    print(f'Client {i} connected.')
    client_thread = threading.Thread(target=handle_client, args=(conn,addr,i))
    client_thread.start()




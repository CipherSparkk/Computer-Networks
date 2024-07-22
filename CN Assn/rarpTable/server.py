import socket
import threading
import subprocess

port = 50000
host = '127.0.0.1'

def get_ip_addr (client,num):
    rarp_output = subprocess.check_output(['arp','-a'], text= True)
    rarp_table = {}
    rarp_entries = rarp_output.split('\n')
    for rarp_entry in rarp_entries:
        if len(rarp_entry.strip())>0:
            parts = rarp_entry.split(' ')
            print(parts)
            rarp_table[parts[3]] = parts[1]
    
    print('ARP Table : ', rarp_table)
    mac_addr = client.recv(2048).decode()
    if mac_addr == 'bye':
        print(f'Client {num} disconnected')
        client.close()
    client.send(rarp_table.get(mac_addr, 'Unknown').encode())

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

server.bind((host,port))
server.listen(5)
print('Server is listening...')

i=0
while True:
    conn,addr = server.accept()
    i+=1
    client_thread = threading.Thread(target=get_ip_addr,args=(conn,i))
    client_thread.start()


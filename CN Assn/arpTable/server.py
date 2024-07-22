import socket
import threading
import subprocess

def get_ip_addr(client,num):
    arp_output = subprocess.check_output(['arp', '-a'],text=True)
    arp_entries = arp_output.split('\n')
    arp_table = {}
    for arp_entry in arp_entries:
        if len(arp_entry.strip())>0:
            parts = arp_entry.split(' ')
            if len(parts) >=4 and parts[0] != 'gateway':
                arp_table[parts[1]] = parts[3]
    print('ARP Table : ',arp_table)

    ip_addr = client.recv(2048).decode()
    if ip_addr == 'bye':
        print(f'Connection closed from client {num}')
        client.close()
    client.send(arp_table.get(ip_addr,"Unknown").encode())
    
host = '127.0.0.1'
port = 50000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
server.bind((host,port))
server.listen(5)
print('Server is listening...')
i=0
while True:
    conn,addr = server.accept()
    i+=1
    client_thread = threading.Thread(target = get_ip_addr,args=(conn,i))
    client_thread.start()


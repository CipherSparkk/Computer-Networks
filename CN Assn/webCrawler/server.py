import socket
from urllib.request import urlopen
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import ssl

def web_crawler(url, depth):
    if depth > 0:  
        try:
            ctx = ssl.create_default_context()
            ctx.check_hostname = False
            ctx.verify_mode = ssl.CERT_NONE
            
            response = urlopen(url, context=ctx)
            html = response.read().decode('utf-8')
            soup = BeautifulSoup(html, 'html.parser')
            links = [urljoin(url, link.get('href')) for link in soup.find_all('a', href=True)]
            return links
        except Exception as e:
            return [str(e)]
    else:
        return ["Depth not supported in this demo!!!"]

host = "127.0.0.1"
port = 50000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Binding host address and port
server.bind((host, port))  
print("Socket binded to %s" % port)

server.listen(2)
print("Socket is listening...")
# Accepting new connection
conn, addr = server.accept()  
print("Connection from: " + str(addr))
while True:
        msg = conn.recv(2048).decode()
        if msg == 'Quit':
            break
        url, depth = msg.split(' ') 
        print("From connected user: " + str(msg))
        depth = int(depth.strip())
        links = web_crawler(url, depth)
        result = '\n'.join(links)
        conn.send(result.encode())
print("Connection closed from client")        
# Close connection with client
conn.close()  



import socket

# Defining port  
port=50000
portClient=8000

# Host IP Address
host="127.0.0.1"

# Creating client
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.bind((host, portClient))
client.connect((host, port))
while True:	
	url,depth='',''
	url = input("Enter your URL or enter 'Quit' to exit : ")
	if(url == 'Quit'):
		client.send(url.encode())
		break
	depth = input('Enter the depth : ')
	client.send(f'{url} {depth}'.encode())
	result = client.recv(2048).decode()
	print("From server:", result)
		
print("Connection closed from server")
# Closing Connection
client.close()
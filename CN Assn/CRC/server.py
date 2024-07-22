import socket  
port = 50000
host = '127.0.0.1'
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((host, port))
server.listen(2)
print("Socket is listening...")
conn, addr = server.accept()        
msg = conn.recv(2048).decode()
code, key = msg.split(' ')
print('Data from Client: ', code)
print('Key from Client: ', key)
str2 = key
k=0
other = ''
while(k<len(key)):
    other = other + '0'
    k+=1

k=1
while(k<len(key)):
    code = code + '0'
    k+=1
p = len(key)-1;
l = len(code)
i=len(key)
str1 = code[0:len(key)]
result = []  
while(i<=l):
    j=0;
    if(str1[j] == '1'):
        str2 = key
    else:
        str2 = other
    while(j<len(key)):
        result.append(str(int(str1[j]) ^ int(str2[j])))
        j+=1
    res = ''.join(result[-(p):])
    if i<l:
        res = res + code[i]
    str1 = res
    i += 1
l2 = len(res)
cnt = l - l2
error = ''
while(cnt):
    error = error + '0'
    cnt-=1
    
error = error + res
ans = ''
i=0
while(i<l):
    if(error[i] == code[i]):
        ans = ans + '0'
    else:
        ans = ans + '1'
    i+=1
conn.send(str(ans).encode())
print("Connection closed from client")
conn.close()

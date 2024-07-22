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
    if msg == 'Quit':
        break
    print('Message received from client : ', msg)
    i=len(msg)-1
    answer=0
    stack = []
    while i>=0:
        while i>=0 and msg[i] != '*' and msg[i] != '/' and msg[i] != '+' and msg[i] != '-' and msg[i] != '^':
            stack.append(int(msg[i]))
            i-=1
        else:
            if len(stack)>1:
                operand1 = stack.pop()
                operand2 = stack.pop()
                if msg[i] == '/':
                    res = operand1 / operand2
                if msg[i] == '*':
                    res = operand1 * operand2
                if msg[i] == '+':
                    res = operand1 + operand2
                if msg[i] == '-':
                    res = operand1 - operand2
                if msg[i] == '^':
                    res = operand1 ** operand2
                stack.append(res)
                answer = res
            else:
                answer = stack.pop()
            i-=1
    answer = str(answer)
    conn.send(answer.encode())
print('Connection closed from client...')
conn.close()


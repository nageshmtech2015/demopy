import socket
s = socket.socket()
print('Socket created')

s.bind(('localhost', 9998))
s.listen(3)
print('Waiting for connections')
while True:
    c, addr = s.accept()
    name = c.recv(1024).decode()
    print("connected with ", addr, name)
    c.send(bytes('Welcome to socket programming','utf-8'))
    c.close()
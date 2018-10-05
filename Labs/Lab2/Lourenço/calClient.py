import socket
import time

s = socket.socket()
host = socket.gethostname()
port = 12345
s.connect((host, port))

while True:
    request = input('Request(push, pop, add, sub, exit): ')

    if 'push' in request:
        s.send("push".encode())
        pushValue = input('Value to push: ')
        s.send(pushValue.encode())

    if 'pop' in request:
        s.send("pop".encode())
        reply = str(s.recv(1024))
        print("Received reply:", reply[2])

    if 'add' in request:
        s.send("add".encode())

    if 'sub' in request:
        s.send("sub".encode())

    if request == 'exit':
        s.send("exit".encode())
        break

s.close()

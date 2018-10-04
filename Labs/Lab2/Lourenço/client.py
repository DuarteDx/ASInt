import socket
import time

s = socket.socket()
host = socket.gethostname()
port = 12345
s.connect((host, port))

## Code to execute on the server
s.send("push".encode())
time.sleep(1)
s.send("5".encode())
time.sleep(1)
s.send("push 10".encode())
time.sleep(1)
s.send("add".encode())
time.sleep(1)
s.send("pop".encode())
reply = str(s.recv(1024))
print(reply)


s.close()
import socket
import pickle

s = socket.socket()
host = socket.gethostname()
port = 12345
s.connect((host, port))
s.send("5".encode())

reply = s.recv(1024)
print(str(reply))
var = pickle.loads(reply)

print(var.a)

print(var)

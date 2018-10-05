import socket
import pickle
from pick import testClass

s = socket.socket()

host = socket.gethostname()
port = 12345
s.bind((host, port))
s.listen(5)

c, addr = s.accept()
print("Connection from", str(addr))

request = str(c.recv(1024))
num = int(request[2])
var = testClass(num)

c.send(pickle.dumps(var))


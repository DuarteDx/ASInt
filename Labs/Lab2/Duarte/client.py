import socket

mySocket = socket.socket()

host = socket.gethostname()
port = 12345

mySocket.connect((host, port))
print(mySocket.recv(500))

mySocket.close()
import socket
from rpnCalculator import rpnCalculator

mySocket = socket.socket()

host = socket.gethostname()
port = 12345

mySocket.bind((host, port))
mySocket.listen(5)

while True:
    connection, addr = mySocket.accept()
    
    ##ToDO: Requests logic

    connection.close()
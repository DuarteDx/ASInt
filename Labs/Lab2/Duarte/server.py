import socket

mySocket = socket.socket()

host = socket.gethostname()
port = 12345

mySocket.bind((host, port))
mySocket.listen(5)

while True:
    connection, addr = mySocket.accept()
    print('Client connection: ' + str(connection) + '\n')
    print('Client address: ' + str(addr) + '\n')

    connection.send('Hello'.encode())
    connection.close()

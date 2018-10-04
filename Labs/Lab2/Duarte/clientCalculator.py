import socket

mySocket = socket.socket()

host = socket.gethostname()
port = 12345

mySocket.connect((host, port))

while True:
    request = input('Request(push, pop, add, exit): ')

    if request == 'push':
        pushValue = input('Value to push: ')
        mySocket.send(request.encode(), pushValue.encode())

    if request == 'exit':
        break

    mySocket.send(request.encode())
    print("Request sent!")

mySocket.close()
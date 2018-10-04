import socket
import calculator
import re

s = socket.socket()
calc = calculator.rpnCalculator()

host = socket.gethostname()
port = 12345
s.bind((host, port))
s.listen(5)

while True:
    c, addr = s.accept()
    print("Connection from", str(addr))
    request = str(c.recv(1024))
    print(request)

    if "push" in request:
        num = str(c.recv(1024))
        num = int(num[2])
        calc.pushValue(num)

    if "pop" in request:
        num = calc.popValue()
        c.send(str(num).encode())

    if "add" in request:
        calc.add()

    c.close()
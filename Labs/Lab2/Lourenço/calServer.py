import socket
import calculator

s = socket.socket()
calc = calculator.rpnCalculator()

host = socket.gethostname()
port = 12345
s.bind((host, port))
s.listen(5)

c, addr = s.accept()
print("Connection from", str(addr))

while True:
    request = str(c.recv(1024))

    if "push" in request:
        print("Push request received")
        num = str(c.recv(1024))
        num = int(num[2])
        calc.pushValue(num)
        print(calc.Memory)

    if "pop" in request:
        num = calc.popValue()
        c.send(str(num).encode())

    if "add" in request:
        calc.add()
    
    if "sub" in request:
        calc.sub()
    
    if "exit" in request:
        break

c.close()
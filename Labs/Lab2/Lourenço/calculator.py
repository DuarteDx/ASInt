class rpnCalculator:
    "RPN calculator example"

    def __init__(self):
        self.Memory = []
    
    def pushValue(self, num):
        return self.Memory.insert(0, int(num))

    def popValue(self):
        return self.Memory.pop(0)

    def add(self):
        a = self.popValue()
        b = self.popValue()
        self.pushValue(a+b)

    def sub(self):
        a = self.popValue()
        b = self.popValue()
        self.Memory.insert(0, a-b)
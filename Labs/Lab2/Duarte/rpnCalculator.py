class rpnCalculator:

    def __init__(self):
        self.memory = []

    def pushValue(self, value):
        self.memory.append(value)
        print("Value pushed!")
        self.print()

    def popValue(self):
        self.memory.pop()
        print("Value popped!")
        self.print()

    def addValues(self):
        'Adds the two topmost values of the stack and pushes the new value'
        newValue = self.memory[-1] + self.memory[-2]
        self.memory.append(newValue)
        print("Values added!")
        self.print()

    def subValues(self):
        'Subtracts the two topmost values of the stack and pushes the new value'
        newValue = self.memory[-1] - self.memory[-2]
        self.memory.append(newValue)
        print("Values subtracted!")
        self.print()

    def print(self):
        print('Current stack: ' + str(self.memory))
        print('\n')


'''myStack = rpnCalculator()
myStack.pushValue(3)
myStack.pushValue(9)
myStack.pushValue(5)
myStack.popValue()
myStack.addValues()
myStack.subValues()'''






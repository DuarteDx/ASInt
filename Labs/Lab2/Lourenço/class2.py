class Employee:
    'Common base class for all employees'
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print("Total Employee %d" % Employee.empCount)

    def displayEmployee(self):
        print("Name : " + self.name + ", Salary: " + str(self.salary))

E = Employee("Carlos", 5000)
E2 = Employee("ana", 10000)

E.displayCount()
E.displayEmployee()
print(E2.empCount)
print(E.name)


class Employee:
    numEmployee = 0
    totalPay = 0

    def __init__(self, name, family, salary, department):
        self.name = name
        self.family = family
        self.salary = salary
        self.department = department

        self.numEmployee += 1
        self.totalPay += self.salary

    def avgsalary(self):
        print(self.totalPay / self.numEmployee)


emp1 = Employee('bob', 'john', 20000, 'IT')
emp2 = Employee('lock', 'john', 60000, 'IT')

print(avgsalary())

class Employee:
    def __init__(self, name, salary=30000):
        self.name, self.salary = name, salary
            
    # Add the __str__() method
    def __str__(self):
        return "Employee name: {}\nEmployee salary:{}".format(self.name, self.salary)

    def __repr__(self):
        return "Employee(\"{}\", {})".format(self.name, self.salary)

emp1 = Employee("Amar Howard", 30000)
print(emp1)
emp2 = Employee("Carolyn Ramirez", 35000)
print(repr(emp2))

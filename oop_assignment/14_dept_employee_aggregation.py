
class Employee:
    def __init__(self, name):
        self.name = name

class Department:
    # Aggregation: Department has an Employee (employee exists independently)
    def __init__(self, employee):
        self.employee = employee

emp = Employee("Alia")       # Independent Employee object
dept = Department(emp)       # Employee passed to Department
print(dept.employee.name)   
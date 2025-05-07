class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name         # Public variable
        self._salary = salary    # Protected variable (by convention)
        self.__ssn = ssn         # Private variable (name mangling)

# Create an object of Employee
emp = Employee("Alia", 50000, "123-45-6789")

# Accessing public variable
print("Name:", emp.name)  # This works

# Accessing protected variable
print("Salary:", emp._salary)  #  This works, but should be avoided outside the class by convention

# Accessing private variable directly
try:
    print("SSN:", emp.__ssn)  #  This will raise an AttributeError
except AttributeError as e:
    print("Error accessing __ssn:", e)
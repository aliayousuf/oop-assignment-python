
class Multiplier:
    def __init__(self, factor):
        self.factor = factor  

    def __call__(self, num):
        return num * self.factor  # Multiply input by factor

# Create an instance of Multiplier with factor 
m = Multiplier(5)
# Test if the object is callable
print(callable(m))  
# Use the object like a function
result = m(10)  
print(result)  
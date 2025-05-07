from abc import ABC, abstractmethod

# Define the abstract base class
class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

# Inherit from Shape and implement the area method
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

rect = Rectangle(10, 5)
print(f"The area of the rectangle is: {rect.area()}")
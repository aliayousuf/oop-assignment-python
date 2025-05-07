
class Student:
  def __init__(self,name,marks):
    self.name = name
    self.marks = marks
    
  def display(self):
    print(f"Student Name: {self.name}")
    print(f"Marks : {self.marks}")

s1 = Student("Alia",85)
s1.display()
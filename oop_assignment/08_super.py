
class Person:
  def __init__(self,name):
    self.name = name

class Teacher(Person):
  def __init__(self,name,subject):
    super().__init__(name)
    self.subject = subject


t1 = Teacher("Alia", "physics")
print(f"Name: {t1.name}, Subject: {t1.subject}")
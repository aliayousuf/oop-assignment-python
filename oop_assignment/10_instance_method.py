
class Dog:
  def __init__(self,name,breed):
    self.name=name
    self.breed=breed

  def bark(self):
    print(f"{self.name} is barking loudly! Woof woof!")


dog = Dog("Max","German Shepherd")
dog.bark()

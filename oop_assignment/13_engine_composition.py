
class Engine:
  def start(self):
    print("Engine started...")

class Car:
  def __init__(self, engine):
    self.engine = engine  # Composition: Car has an Engine

  def drive(self):
    self.engine.start()  # Accessing Engine method via Car

    
# Create an Engine object
engine = Engine()
# Pass the Engine object to the Car
car = Car(engine)
# Start the car (which internally starts the engine)
car.drive()
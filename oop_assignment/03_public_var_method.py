class Car:
    def __init__(self, brand):
        self.brand = brand  # public variable

    def start(self):  # public method
        print(f"{self.brand} car is starting...")


car1 = Car("Audi")

# Access the public variable and method
print("Car brand:", car1.brand)
car1.start()
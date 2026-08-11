class Car:

    color = "Black"

    @staticmethod
    def start():
        print("car started..")

    @staticmethod
    def stop():
        print("Car Stopped")

class ToyotaCar(Car):
    def __init__(self, name):
        self.name = name

car1 = ToyotaCar("Fortuner")
car2 = ToyotaCar("Innova")

print(car1.start())
print(car2.color)
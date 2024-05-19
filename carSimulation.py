class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.speed = 0

    def accelerate(self, acceleration):
        self.speed += acceleration
        pass

    def brake(self, deceleration):
        self.speed -= deceleration
        pass

    def get_speed(self):
        return self.speed
        pass

    def __str__(self):
        return f"{self.make} {self.model} ({self.year})"


# Example usage:
car = Vehicle("Toyota", "Camry", 2022)
print(car)  # Output: Toyota Camry (2022)

car.accelerate(30)
print(car.get_speed())  # Output: 30

car.brake(10)
print(car.get_speed())  # Output: 20
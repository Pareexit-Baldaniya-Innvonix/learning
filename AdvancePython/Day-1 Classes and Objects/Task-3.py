# Task 3: Instantiate object from the class
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year


details = Car("BMW", "M4", 2026)
print(details.make)
print(details.model)
print(details.year)

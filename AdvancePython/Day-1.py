# Day 1: Classes and Objects

# Task 2:
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

# Task 3:
details = Car("BMW", "M4", 2026)
print(details.make)
print(details.model)
print(details.year)
# Day 1: Classes and Objects

# Task 1:
# Class: Blueprint of the object
# Objest: Actual instance(interface) of the class

# Task 2:
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

# Task 3:
Car_details = Car("BMW", "M4", 2026)
print(Car_details.make)
print(Car_details.model)
print(Car_details.year)
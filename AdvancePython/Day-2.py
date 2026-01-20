# Day 2: Constructors and Methods

# Task 1: simple constructure
class Toy:
    def __init__(self):
        self.name = "Bear"
        self.size = "small"

toy = Toy()
print(toy.name)
print(toy.size)

# Task 2: parameterized constructure
class Movie:
    def __init__(self, name, type, cinema):
        self.name = name
        self.type = type
        self.cinema = cinema

movie = Movie("Avatar: Fire and Ash", "Action", "Hollywood")
print(movie.name)
print(movie.type)
print(movie.cinema)

# Task 3:
# 1. Instance method:
class Car:
    def __int__(self):
        self.color = "Blue"

    def show_color(self):  # this is instance method
        print(f"the car is {self.color}")

# 2. Class Method:
class Car:
    total_cars = 0

    def __init__(self):
        Car.total_cars += 1

    @classmethod
    def get_fleet_size(cls):
        return f"total cars build: {cls.total_cars}"
    
# 3. Static Method:
class Car:
    @staticmethod
    def isMotorized():
        return True
    
# 4. Accessors:
class Car:
    def __init__(self, brand):
        self._brand = brand
    
    @property
    def brand_name(self):
        return self._brand.upper()
    
# 5. Mutators:
class Car:
    def __init__(self, speed):
        self._speed = speed

    @property
    def speed(self):
        return self._speed
    
    @speed.setter
    def speed(self, value):
        if value < 0:
            print("Speed can not be negative")
        else:
            self._speed = value

# Task 4:
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

carDetails = Car("BMW", "M4", 2026)
print(carDetails.make)
print(carDetails.model)
print(carDetails.year)

# Task 5:
class Car:
    age = 20
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    @property
    def age(self):
        current_year = 2026
        return current_year - self.year

details = Car("BMW", "M4", 2024)
print(details.make)
print(details.model)
print(details.year)
print(details.age)
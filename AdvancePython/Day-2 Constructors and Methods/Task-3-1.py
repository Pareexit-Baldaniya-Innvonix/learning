# Task 3:
# 1. Instance method:
class InsCar:
    def __init__(self):
        self.color = "Blue"

    def show_color(self):  # this is instance method
        print(f"The car is {self.color}")

car = InsCar()
car.show_color()
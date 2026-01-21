# Task 3:
# 2. Class Method:
class ClsCar:
    total_cars = 0

    def __init__(self):
        ClsCar.total_cars += 1

    @classmethod
    def get_fleet_size(cls):
        return f"Total cars build: {cls.total_cars}"
    
car1 = ClsCar()
print(car1.get_fleet_size())
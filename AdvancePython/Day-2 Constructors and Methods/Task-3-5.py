# Task 3:
# 5. Mutators:
class MutCar:
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

car4 = MutCar(60)
print(car4.speed)
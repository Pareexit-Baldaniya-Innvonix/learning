# Task 5:
class AgeOfCar:
    age = 20

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    @property
    def age(self):
        current_year = 2026
        return current_year - self.year


details = AgeOfCar("BMW", "M4", 2024)
print(f"Make: {details.make}")
print(f"Model: {details.model}")
print(f"Year: {details.year}")
print(f"Age: {details.age}")

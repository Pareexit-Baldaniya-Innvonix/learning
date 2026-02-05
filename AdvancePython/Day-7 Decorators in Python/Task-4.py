# Task 4:
class Circle:
    def __init__(self, radius: float) -> None:
        self.radius: float = radius

    @property
    def area(self) -> float:
        return 3.14 * (self.radius**2)


c = Circle(5)
print(f"Radius: {c.radius}")
print(f"Area: {c.area}")

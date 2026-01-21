# Task 1: simple constructure
from enum import Enum


class size:
    SMALL = "small"
    MEDIUM = "medium"
    LARGE = "large"


class Toy:
    def __init__(self):
        self.name = "Bear"
        self.size = size.SMALL


toy = Toy()
print(toy.name)
print(toy.size)

# Task 2:
from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def make_sound(self) -> str:
        pass


class Dog(Animal):
    def make_sound(self) -> str:
        return "Bark"


class Cat(Animal):
    def make_sound(self) -> str:
        return "Meow"


if __name__ == "__main__":
    animals = [Dog(), Cat()]

    for animal in animals:
        print(f"{type(animal).__name__} says: {animal.make_sound()}")

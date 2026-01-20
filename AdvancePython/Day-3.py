# Day 3: Advanced OOP concepts

# Task 1:
class Outer:  # outer class
    class Inner:  # inner class
        pass

# Task 2:
class DemoClass:
    def instance_method(self):
        return ("Instance method called", self)
    
    @classmethod
    def class_method(cls):
        return ("Class method called", cls)

    @staticmethod
    def static_method():
        return ("Static method called",)
    
# Task 3:
# 1. Inheritance:
class Animal:
    def __init__(self, name):
        self. name
    
    def info(self):
        print("Animal name:", self.name)

class Dog(Animal):
    def sound(self):
        print(self.name, "barks")

d = Dog("Buddy")
d.info()
d.sound()

# 2. Constructors:
def __init__(self):
    #body of the constructor
    pass

class Class():
    def __init__(self):
        print(x)

class SubClass(Class):
    def __init__(self, x):
        super.__init__(x)

x = [1, 2, 3, 4, 5]
a = SubClass(x)

# 3. Method overloading:
def Add(datatype, *args):
    if datatype == "int":
        answer = 0

    if datatype == "str":
        answer = ""

    for x in args:
        answer = answer = x
    print(answer)

Add("int", 5, 6)
Add("str", "Hello", "World")

# 4. Method Overriding:
class A:
    def func1(self):
        print("Feature 1 of calss A")

    def func2(self):
        print("Feature 2 of calss A")

class B:
    def func1(self):
        print("Modified feature 1 of calss A by class B")

    def func3(self):
        print("Feature 3 of calss B")

obj = B
obj.func1()

# Task 4:
class Employee:
    def __init__(self):
        self.name = "Hello"
        self.add = self.add()

    def show(self):
        print("Name: ", self.name)

    class Address():
        def __init__(self):
            self.add = "India"

        def display(self):
            print("Add: ", self.add)
        
e1 = Employee()
e1.show()

# Task 5:
class Calculator:

    @classmethod
    def add(cls, a, b):
        return a + b

    @classmethod
    def sub(cls, a, b):
        return a - b
    
    @classmethod
    def mul(cls, a, b):
        return a * b
    
    @classmethod
    def div(cls, a, b):
        if b == 0:
            return "Error: Connot divide by zero"
        return a / b
    
print("Addition: ", Calculator.add(10, 5))
print("Subtraction: ", Calculator.sub(10, 5))
print("Multiplication: ", Calculator.mul(10, 5))
print("Division: ", Calculator.div(10, 5))
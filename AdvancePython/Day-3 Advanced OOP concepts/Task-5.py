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


print(f"Addition: {Calculator.add(10, 5)}")
print(f"Subtraction: {Calculator.sub(10, 5)}")
print(f"Multiplication: {Calculator.mul(10, 5)}")
print(f"Division: {Calculator.div(10, 5)}")
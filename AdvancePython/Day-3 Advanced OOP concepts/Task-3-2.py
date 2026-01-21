# Task 3:
# 2. Constructors:
def __init__(self):
    # body of the constructor
    pass


class Class:
    def __init__(self, x):
        print(f"Parent class: {x}")


class SubClass(Class):
    def __init__(self, x):
        super().__init__(x)


x = [1, 2, 3, 4, 5]
a = SubClass(x)
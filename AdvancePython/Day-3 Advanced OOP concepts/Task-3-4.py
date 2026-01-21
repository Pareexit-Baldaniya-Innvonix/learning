# Task 3:
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


obj = B()
obj.func1()
# Task 4:
class Employee:
    def __init__(self):
        self.name = "John"
        self.addr = self.Address()

    def show(self):
        print("Name:", self.name)
        self.addr.display()

    class Address:
        def __init__(self):
            self.add = "India"

        def display(self):
            print("Address:", self.add)


e1 = Employee()
e1.show()

# Task 3: Decorators
def changecase(func):
    def myinner():
        return func().upper()

    return myinner


@changecase
def myfunction():
    return "Hello World!"


print(myfunction())
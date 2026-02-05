# Task 3:
def greetings(func: any) -> None:
    def wrapper() -> None:  # nested function
        print("Hello!")
        func()
        print("How are you?")

    return wrapper


@greetings
def world() -> None:
    print(", World")


world()

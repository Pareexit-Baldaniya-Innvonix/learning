# Task 1: Decorators
def change_case(func: str) -> str:
    def inner_func() -> str:
        return func().upper()

    return inner_func()


@change_case
def greet_func() -> str:
    return "Hello World!"


print(greet_func)

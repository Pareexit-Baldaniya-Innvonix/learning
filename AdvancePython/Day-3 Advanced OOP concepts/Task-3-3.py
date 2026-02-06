# Task 3:
# 3. Method overloading:
def add_values(*args: any) -> None:
    if not args:
        print("No argument provided!")
        return

    first_arg = args[0]

    if isinstance(first_arg, int):
        result = 0
    elif isinstance(first_arg, str):
        result = ""
    else:
        print(f"Unsupported datatype: {type(first_arg).__name__}")
        return

    try:
        for x in args:
            result += x
        print(result)
    except TypeError:
        print(f"Error: all arguments must be of the same type.")


if __name__ == "__main__":
    add_values(5, 6)
    add_values("Hello ", "World")
    add_values(1.2, 1.4)
    add_values(10, "mixed")

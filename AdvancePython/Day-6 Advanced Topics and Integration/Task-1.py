# Exceptions:
class ValueTooHighError(Exception):
    pass


def check_value(n: int) -> None:
    if n > 100:
        raise ValueTooHighError(f"Validation failed: {n} is greater than 100")


# custom exception
try:
    check_value(200)
except ValueTooHighError as e:
    print(e)

# How to handle exceptions:
# user input exception
try:
    user_input = input("Enter a divisor: ")
    num = int(user_input)

    result = num / 10
    print(f"Result: {num} / 10 = {result}")

except ZeroDivisionError:
    print("You can't divide by zero!")
except ValueError:
    print("That wasn't a valid number!")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
    print("Execution complete.")

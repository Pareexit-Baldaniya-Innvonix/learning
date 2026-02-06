# Task 2:
import threading
import time


def square(num: int) -> None:
    print(f"Square: {num*num}")
    time.sleep(1)


def cube(num: int) -> None:
    print(f"Cube: {num*num*num}")
    time.sleep(1)


square_thread = threading.Thread(target=square, args=(4,))
cube_thread = threading.Thread(target=cube, args=(4,))

square_thread.start()
cube_thread.start()

square_thread.join()
cube_thread.join()

print("Done!")

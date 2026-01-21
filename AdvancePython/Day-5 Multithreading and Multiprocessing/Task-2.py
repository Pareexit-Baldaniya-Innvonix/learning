# Task 2:
import threading
import time


def Square(num):
    print(f"Square: {num*num}")
    time.sleep(1)


def Cube(num):
    print(f"Cube: {num*num*num}")
    time.sleep(1)


t1 = threading.Thread(target=Square, args=(4,))
t2 = threading.Thread(target=Cube, args=(4,))

t1.start()
t2.start()

t1.join()
t2.join()

print("Done!")
# Task 3:
import multiprocessing
import os


def check_task():
    print(f"task running in process id: {os.getpid()}")


if __name__ == "__main__":
    p1 = multiprocessing.Process(target=check_task)
    p2 = multiprocessing.Process(target=check_task)

    p1.start()
    p2.start()

    p1.join()
    p2.join()
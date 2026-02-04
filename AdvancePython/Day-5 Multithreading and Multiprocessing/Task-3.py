# Task 3:
import multiprocessing
import os


def check_task() -> None:
    print(f"task running in process id: {os.getpid()}")


if __name__ == "__main__":
    first_process = multiprocessing.Process(target=check_task)
    second_process = multiprocessing.Process(target=check_task)

    first_process.start()
    second_process.start()

    first_process.join()
    second_process.join()

    print("Process finished.")

# Task 5:
import time


def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        print(f"Time taken: {end_time - start_time:.4f} seconds.")
        return result

    return wrapper


@timer
def waste_time():
    time.sleep(1)
    print("Function finished!")


waste_time()

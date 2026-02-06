# Task 5:
import time


def timer(func: any) -> callable:
    def wrapper(*args: any, **kwargs: any) -> any:
        start_time = time.perf_counter()  # start time
        result = func(*args, **kwargs)  # actual function
        end_time = time.perf_counter()  # end time
        print(
            f"Time taken: {end_time - start_time:.4f} seconds."
        )  # calculate and print duration
        return result

    return wrapper


@timer  # decorator
def waste_time() -> None:
    time.sleep(1)
    print("Function finished!")


if __name__ == "__main__":
    waste_time()

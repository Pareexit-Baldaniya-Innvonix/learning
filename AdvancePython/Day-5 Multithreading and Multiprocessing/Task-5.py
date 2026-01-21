# Task 5:
import multiprocessing
import time


def compute_square(num):
    return num * num


if __name__ == "__main__":
    dataset = list(range(10000000))

    start_time = time.perf_counter()
    end_time = time.perf_counter()
    print(f"Sequential processing would take much longer...")

    print(f"Starting parallel computing on {multiprocessing.cpu_count()} cores...")
    start_time = time.perf_counter()

    with multiprocessing.Pool() as pool:
        results = pool.map(compute_square, dataset)

    end_time = time.perf_counter()

    print(f"Parallel processing finished in {end_time - start_time:.4f} seconds.")
    print(f"Computed {len(results)} results.")
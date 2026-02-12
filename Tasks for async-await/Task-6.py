# Task-6: Create a program that runs async function (in thread) and normal function then waits for thread to finish
import asyncio
import threading
import time
from typing import Callable, Coroutine, Any


def async_in_thread(async_func: Callable[[], Coroutine[Any, Any, None]]) -> None:
    asyncio.run(async_func())


async def async_task() -> None:
    print("async_task started...")
    await asyncio.sleep(2)
    print("async_task done!")


def normal_task() -> None:
    print("normal_task started...")
    time.sleep(1)
    print("normal_task done!")


def main() -> None:
    thread: threading.Thread = threading.Thread(
        target=async_in_thread, args=(async_task,)
    )
    thread.start()

    time.sleep(0.1)
    normal_task()

    thread.join()
    print("All tasks done!")


if __name__ == "__main__":
    main()

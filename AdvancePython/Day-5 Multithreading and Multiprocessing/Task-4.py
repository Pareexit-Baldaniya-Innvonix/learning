# Task 4:
import requests
import threading
from concurrent.futures import ThreadPoolExecutor
import os

IMAGE_DIR = "AdvancePython/Day-5 Multithreading and Multiprocessing/downloaded_images"
MAX_WORKERS = 5
TIMEOUT = 30


def download_image(url: str) -> None:
    try:
        filename = os.path.join(IMAGE_DIR, url.split("/")[-1])
        print(f"Starting download: {url} (Thread: {threading.current_thread().name})")

        response = requests.get(url, timeout=TIMEOUT)
        response.raise_for_status()
        if response.status_code == 200:
            with open(filename, "wb") as f:
                f.write(response.content)
            print(f"Successfully saved to {filename}")
        else:
            print(f"Failed to download {url}: Status {response.status_code}")

    except Exception as e:
        print(f"Error downloading {url}: {e}")


def main() -> None:

    os.makedirs(IMAGE_DIR, exist_ok=True)

    urls = [
        "https://picsum.photos/id/237/200/300.jpg",
        "https://picsum.photos/id/238/200/400.jpg",
        "https://picsum.photos/id/239/200/500.jpg",
        "https://picsum.photos/id/240/200/600.jpg",
        "https://picsum.photos/id/241/200/700.jpg",
    ]

    print(f"Starting downloads using {MAX_WORKERS} workers...\n")

    with ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(download_image, urls)

    print("\nAll downloads completed!")


if __name__ == "__main__":
    main()

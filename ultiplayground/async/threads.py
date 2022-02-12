from concurrent.futures import ThreadPoolExecutor
import requests
import threading
import time


thread_local = threading.local()


def get_session():
    if not hasattr(thread_local, "session"):
        thread_local.session = requests.Session()
    return thread_local.session


def download_site(url):
    session = get_session()
    session.get(url)


def download_all_sites(sites):
    with ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(download_site, sites)


if __name__ == "__main__":
    sites = [
        "https://jython.org",
        "http://olympus.realpython.org/dice",
        "https://github.com/UltiRequiem/python",
    ] * 100

    start_time = time.time()

    download_all_sites(sites)

    duration = time.time() - start_time

    print(f"Downloaded {len(sites)} pages in {duration} seconds!")

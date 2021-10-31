import requests
from datetime import datetime

print(datetime.now())


def fetch(url: str):
    requests.get(url)


def main():
    for _ in range(10):
        fetch("https://www.google.com")


main()


print(datetime.now())

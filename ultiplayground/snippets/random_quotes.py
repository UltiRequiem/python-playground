import requests


QUOTES_DATA: dict = requests.get("https://api.quotable.io/random").json()


if __name__ == "__main__":
    print(QUOTES_DATA["content"])
    print(f" - {QUOTES_DATA['author']}")

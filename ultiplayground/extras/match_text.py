import json
import os


def read_all_lines(file_path: str):
    """
    Parse a CSV file and return a list of dictionaries.
    """
    with open(file_path, "r", encoding="UTF-8") as file:
        return file.read().splitlines()


def grouped(iterable, times: int):
    return zip(*[iter(iterable)] * times)


data = [
    {"shortname": shortname.upper(), "fullname": fullname}
    for shortname, fullname in grouped(read_all_lines("data/crypto_shortname"), 2)
]

with open(f"{os.getcwd()}/data/data.json", "w", encoding="UTF-8") as f:
    json.dump(data, f)

import csv
import json
from os.path import dirname


def parse_csv(file_path: str, from_script_dir=True, reader=csv.reader):
    """
    Parse a CSV file and return a list of dictionaries.
    """

    if from_script_dir:
        file_path = f"{dirname(__file__)}/{file_path}"

    with open(file_path, "r") as csv_file:
        reader = reader(csv_file)
        return [row[0] for row in reader]


def grouped(iterable, n: int):
    return zip(*[iter(iterable)] * n)


data = {}

for shortname, fullname in grouped(parse_csv("crypto_shortname.csv"), 2):
    data[shortname] = fullname

with open(f"{dirname(__file__)}/data.json", "w") as f:
    json.dump(data, f)

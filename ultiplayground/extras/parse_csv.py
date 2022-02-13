import csv
import json
import os


def parse_csv(file_path: str, from_script_dir=True, reader=csv.reader):
    """
    Parse a CSV file and return a list of dictionaries.
    """

    if from_script_dir:
        file_path = f"{os.getcwd()}/data/{file_path}"

    with open(file_path, "r") as csv_file:
        reader = reader(csv_file)
        return [row[0] for row in reader]


def grouped(iterable, n: int):
    return zip(*[iter(iterable)] * n)


data = [
    {"shortname": shortname.upper(), "fullname": fullname}
    for shortname, fullname in grouped(parse_csv("crypto_shortname.csv"), 2)
]

with open(f"{os.getcwd()}/data/data.json", "w") as f:
    json.dump(data, f)

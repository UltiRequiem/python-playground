#!/usr/bin/env python

from os import system
from sys import argv


# Waiting for Python 3.10 match & case


def main(command: str) -> None:
    if command == "format":
        system("black .")
    elif command == "lint":
        system("pylint ultiplayground tests")
    else:
        raise BaseException("That is not a valid command!")


if __name__ == "__main__":
    try:
        main(argv[1])
    except IndexError:
        print("You are missing parameters!")

from typing import Callable


def increment_by(num: int) -> Callable:
    def incrementer(n: int) -> int:
        return n + num

    return incrementer


increment_by_ten = increment_by(10)


if __name__ == "__main__":
    ONE_HUNDRED = increment_by_ten(90)
    print(ONE_HUNDRED)

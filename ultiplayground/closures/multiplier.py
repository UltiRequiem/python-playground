from typing import Callable


def make_multiplier_of(num_one: int) -> Callable:
    def multiplier(num_two: int) -> int:
        return num_two * num_one

    return multiplier


multiply_three = make_multiplier_of(3)

multiply_five = make_multiplier_of(5)

if __name__ == "__main__":
    print(multiply_three(9))
    print(multiply_five(3))
    print(multiply_five(multiply_three(2)))

def make_multiplier_of(n: int):
    def multiplier(x: int) -> int:
        return x * n

    # multiplier = lambda x: x * n

    return multiplier


multiply_three = make_multiplier_of(3)

multiply_five = make_multiplier_of(5)

if __name__ == "__main__":
    print(multiply_three(9))
    print(multiply_five(3))
    print(multiply_five(multiply_three(2)))

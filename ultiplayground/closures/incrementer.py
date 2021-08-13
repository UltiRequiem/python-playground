def increment_by(num):
    def increment(n):
        return n + num

    return increment


increment_by_ten = increment_by(10)


if __name__ == "__main__":
    ONE_HUNDRED = increment_by_ten(90)
    print(ONE_HUNDRED)

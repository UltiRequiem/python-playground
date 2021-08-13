from .incrementer import increment_by_ten
from .multiplier import multiply_five
from .returner import say_cheese, say_hello


def use_incrementer() -> None:
    TEN = increment_by_ten(0)
    print(TEN)


def use_multiplier() -> None:
    fifty = multiply_five(10)
    print(fifty)


def use_returner() -> None:
    cheese = say_cheese()
    hello = say_hello()
    print(cheese, hello)

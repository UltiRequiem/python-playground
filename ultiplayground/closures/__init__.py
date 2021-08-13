from .incrementer import increment_by_ten
from .multiplier import multiply_five
from .returner import say_cheese


def use_incrementer():
    TEN = increment_by_ten(0)
    print(TEN)


def use_multiplier():
    fifty = multiply_five(50)
    print(fifty)

def use_returner():
    msg = say_cheese()
    print(msg)

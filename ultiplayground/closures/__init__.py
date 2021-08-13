from .incrementer import INCREMENT_BY_10
from .multiplier import FIVE_TIMES
from .returner import say_cheese


def use_incrementer():
    TEN = INCREMENT_BY_10(0)
    print(TEN)


def use_multiplier():
    fifty = FIVE_TIMES(50)
    print(fifty)

def use_returner():
    msg = say_cheese()
    print(msg)

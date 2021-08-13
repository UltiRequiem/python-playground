from playground.closures import INCREMENT_BY_10, FIVE_TIMES, say_cheese


def test_incrementer():
    assert INCREMENT_BY_10(10) == 20, "Incrementer is invalid!"


def test_multiplier():
    assert FIVE_TIMES(10) == 50, "Multiplier is invalid!"


def test_print():
    assert say_cheese() == "cheese"

from ultiplayground.closures import increment_by_ten, multiply_five, say_cheese


def test_incrementer():
    assert increment_by_ten(10) == 20, "Incrementer is invalid!"


def test_multiplier():
    assert multiply_five(10) == 50, "Multiplier is invalid!"


def test_print():
    assert say_cheese() == "cheese", "Incorrect message!"

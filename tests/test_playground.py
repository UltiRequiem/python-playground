from ultiplayground import __authors__, __version__


def test_version():
    assert isinstance(__version__, str), "The version value is invalid!"


def test_authors():
    assert isinstance(__version__, str), "The authors value is invalid!"

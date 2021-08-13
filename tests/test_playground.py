from ultiplayground import __version__, __author__


def test_version():
    assert isinstance(__version__, str), "The version value is invalid!"


def test_authors():
    assert isinstance(__version__, str), "The authors value is invalid!"

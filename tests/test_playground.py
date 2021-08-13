from playground import __version__


def test_version():
    assert isinstance(__version__, str), "The version is invalid!"

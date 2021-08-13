from ultiplayground.snippets import POKEMON, POKEMONS_NAME, QUOTES_DATA


def test_pokemon():
    assert isinstance(POKEMON, str), "This Pokemon is not valid!"


def test_pokemons():
    assert isinstance(POKEMONS_NAME, list), "This Pokemon list is not valid!"


def test_quotes():
    assert isinstance(QUOTES_DATA, str), "This Pokemon list is not valid!"

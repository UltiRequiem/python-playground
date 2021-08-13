"""
This tells Python that this is a module.
"""


from .random_pokemon import POKEMON, POKEMONS_NAME
from .random_quotes import QUOTES_DATA


def use_pokemons():
    return POKEMON in POKEMONS_NAME


def use_quotes():
    return isinstance(QUOTES_DATA, dict)

"""
This tells Python that this is a module.
"""


from .random_pokemon import POKEMON, POKEMONS_NAME


def use_pokemons():
    return POKEMON in POKEMONS_NAME

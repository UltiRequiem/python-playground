import json
from random import choice

import requests

POKEMON_API = "https://pokeapi.co/api/v2/pokemon-species/?limit=151"

POKEMON_DATA = json.loads(requests.get(POKEMON_API).content)

POKEMONS_NAME = [pokemon["name"] for pokemon in POKEMON_DATA["results"]]

POKEMON = choice(POKEMONS_NAME).capitalize()

if __name__ == "__main__":
    print(f"A Wild {POKEMON} Has Appeared!")

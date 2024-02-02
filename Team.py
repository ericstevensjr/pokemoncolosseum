import random
from Pokemon import pokemon_list

class Team:
    def __init__(self, name):
        self.name = name
        self.pokemon = []

    def assign_pokemon(self, pokemon_list):
        # Randomly choose 3 Pokemons from the list
        self.pokemon = random.sample(pokemon_list, 3)

    def print_team(self):
        print(f"Team Name: {self.name}")
        for pokemon in self.pokemon:
            print(f"Pokemon: {pokemon.name}, Type: {pokemon.type}, HP: {pokemon.hp}, Attack: {pokemon.attack}, Defense: {pokemon.defense}")
            for move in pokemon.moves:
                print(f"Move: {move.name}, Type: {move.type}, Power: {move.power}")
            print("\n\n")

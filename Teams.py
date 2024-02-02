import random
from Pokemon import pokemon_list

class Team:
    def __init__(self, name):
        self.name = name
        self.pokemon = []

    def assign_pokemon(self, pokemon_list):
        # Randomly choose 3 Pokemons from the list
        pickedPokemon = random.sample(pokemon_list, 3)
        self.pokemon.extend(pickedPokemon)
        for pokemon in pickedPokemon:
            pokemon_list.remove(pokemon)

    def print_team(self):
        print(f"\nTeam Name: {self.name}")
        print(self.name + "'s Pokemon are:\n")
        for pokemon in self.pokemon:
            print(f"Pokemon: {pokemon.name}\nType: {pokemon.type}, HP: {pokemon.hp}, Attack: {pokemon.attack}, Defense: {pokemon.defense}")
            for move in pokemon.moves:
                print(f"Move: {move.name}")
            print("\n")

    def pokemon_names(self):
        return ', '.join([pokemon.name for pokemon in self.pokemon])
    
    def checkHp(self):
        if self.pokemon.hp <= 0:
             return False
        else:
            return True
        
        

    def selectTeamRocketMove(pokemon):
        if not pokemon.moves:
            pokemon.resetMoves()

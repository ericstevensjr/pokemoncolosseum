import random
from Pokemon import pokemonList

class Team:
    def __init__(self, name):
        self.name = name
        self.pokemon = []

    # Method to assign Pokemon to a team
    def assignPokemon(self, pokemonList):
        # Randomly choose 3 Pokemons from the list
        pickedPokemon = random.sample(pokemonList, 3)
        self.pokemon.extend(pickedPokemon)
        for pokemon in pickedPokemon:
            pokemonList.remove(pokemon)

    # Method created to make sure I was correctly parsing CSV
    def printTeam(self):
        print(f"\nTeam Name: {self.name}")
        print(self.name + "'s Pokemon are:\n")
        for pokemon in self.pokemon:
            print(f"Pokemon: {pokemon.name}\nType: {pokemon.type}, HP: {pokemon.hp}, Attack: {pokemon.attack}, Defense: {pokemon.defense}")
            for move in pokemon.moves:
                print(f"Move: {move.name}")
            print("\n")

    # Method to display the Pokemon's name on a team.
    def pokemonNames(self):
        return ', '.join([pokemon.name for pokemon in self.pokemon])
        
    # Method to randomly choose a move based on Team Rocket's Pokemons.
    def selectTeamRocketMove(self,pokemon):
        # Resetting their move list if they need it
        if not pokemon.moves:
            pokemon.resetMoves()
        # Choosing and returning a random move.
        move = random.choice(pokemon.moves)
        pokemon.moves.remove(move)
        return move

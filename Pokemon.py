import csv
from Moves import moves_dict

class Pokemon:
    def __init__(self, name, type, hp, attack, defense, moves):
        self.name = name
        self.type = type
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.allMoves = []
        self.moves = []

    # Function to add moves to individual pokemon based on move list
    def add_move(self, move):
        self.moves.append(move)
        self.allMoves.append(move)

    # Function to reset moves when all have been used
    def resetMoves(self):
        self.moves = self.allMoves[:] 

    def checkHp(self):
        if self.hp <= 0:
             return False
        else:
            return True   

# Creating list to store Pokemon
pokemon_list = []

# Parsing the CSV file
with open('pokemon-data.csv', mode = 'r') as file:
    reader = csv.reader(file)

    # Skipping file header row
    next(reader, None)

    # Iterating through the file for Pokemon
    for row in reader:
        pokemon_moves_names = row[7].strip("[]").replace("'", "").split(", ")
        pokemon = Pokemon(
            name = row[0],
            type = row[1],
            hp = int(row[2]),
            attack = int(row[3]),
            defense = int(row[4]),
            moves = []
        )
        # Importing moves to link to individual Pokemon
        for move_name in pokemon_moves_names:
            if move_name in moves_dict:
                pokemon.add_move(moves_dict[move_name])
        pokemon_list.append(pokemon)

# for pokemon in pokemon_list:
#    print(f"Name: {pokemon.name}, Type: {pokemon.type}, HP: {pokemon.hp}, Attack: {pokemon.attack}, Defense: {pokemon.defense}")
#    for move in pokemon.moves:
#        print(f"Move: {move.name}, Type: {move.type}, Power: {move.power}")
#    print("\n\n\n")

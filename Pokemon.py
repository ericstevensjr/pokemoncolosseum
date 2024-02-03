import csv
from Moves import movesDict

class Pokemon:
    def __init__(self, name, type, hp, attack, defense, moves):
        self.name = name
        self.type = type
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.allMoves = []
        self.moves = []

    # Method to add moves to individual pokemon based on move list
    def addMove(self, move):
        self.moves.append(move)
        self.allMoves.append(move)

    # Method to reset moves when all have been used
    def resetMoves(self):
        self.moves = self.allMoves[:] 

    # Method used to check health points for a Pokemon during battle.
    def checkHp(self):
        if self.hp <= 0:
             return False
        else:
            return True   

# Creating list to store Pokemon from CSV
pokemonList = []

# Parsing the CSV file
with open('pokemon-data.csv', mode = 'r') as file:
    reader = csv.reader(file)

    # Skipping file header row
    next(reader, None)

    # Iterating through the file for Pokemon
    for row in reader:
        pokemonMovesNames = row[7].strip("[]").replace("'", "").split(", ")
        pokemon = Pokemon(
            name = row[0],
            type = row[1],
            hp = int(row[2]),
            attack = int(row[3]),
            defense = int(row[4]),
            moves = []
        )

        # Importing moves to link to individual Pokemon
        # I was confused on if this was better done in the Moves class, or this one. I left it here.
        for moveName in pokemonMovesNames:
            if moveName in movesDict:
                pokemon.addMove(movesDict[moveName])
        
        # Adding pokemon to main list
        pokemonList.append(pokemon)

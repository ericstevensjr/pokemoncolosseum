import csv

class Pokemon:
    def __init__(self, name, type, hp, attack, defense, moves):
        self.name = name
        self.type = type
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.moves = moves

# Creating list to store Pokemon
pokemon_list = []

# Parsing the CSV file
with open('pokemon-data.csv', mode = 'r') as file:
    reader = csv.reader(file)

    # Skipping file header row
    next(reader, None)

    # Iterating through the file for Pokemon
    for row in reader:
        pokemon = Pokemon(
            name = row[0],
            type = row[1],
            hp = row[2],
            attack = row[3],
            defense = row[4],
            moves = row[7].strip("[]").replace("'", ""),
        )
        pokemon_list.append(pokemon)

for pokemon in pokemon_list:
    print(f"Name: {pokemon.name}, Type: {pokemon.type}, HP: {pokemon.hp}, Attack: {pokemon.attack}, Defense: {pokemon.defense}, Moves: {pokemon.moves}")
    print("\n\n\n")

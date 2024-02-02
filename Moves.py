import csv

# Dictionary for use when looking up moves for Pokemon
moves_dict = {}

class Move:
    def __init__(self, name, type, power):
        self.name = name
        self.type = type
        self.power = power

# Parsing CSV file
with open('moves-data.csv', mode = 'r') as file:
    reader = csv.reader(file)
    # Skipping header row
    next(reader, None)
    for row in reader:
        move = Move(
            name = row[0],
            type = row[1],
            power = row[5]
        )
        moves_dict[move.name] = move

#for move_name, move in moves_dict.items():
#    print(f"Name: {move.name}, Type: {move.type}, Power: {move.power}")

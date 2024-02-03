import csv

# Dictionary for use when looking up moves for Pokemon
movesDict = {}

class Move:
    def __init__(self, name, type, power):
        self.name = name
        self.type = type
        self.power = power

# Parsing CSV file
with open('moves-data.csv', mode = 'r') as file:
    reader = csv.reader(file)
    
    # Skipping the header row of the CSV file
    next(reader, None)

    # Iterating through CSV and storing moves
    for row in reader:
        move = Move(
            name = row[0],
            type = row[1],
            power = row[5]
        )
        movesDict[move.name] = move

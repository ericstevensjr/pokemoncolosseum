import csv

moves_list = []

class Move:
    def __init__(self, name, type, power):
        self.name = name
        self.type = type
        self.power = power

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
        moves_list.append(move)

for move in moves_list:
    print(f"Name: {move.name}, Type: {move.type}, Power: {move.power}")
    print("\n\n\n")


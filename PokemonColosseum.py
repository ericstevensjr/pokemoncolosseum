import random
from Teams import Team
from Pokemon import pokemon_list

# Initialize game
print("\nWelcome to Pokemon Colosseum!\n")

# Get player name
playerName = input("Enter Player Name: ")

# Create teams and assign Pokemon
pokemonAvailable = pokemon_list.copy()
playerTeam = Team("Team " + playerName)
playerTeam.assign_pokemon(pokemonAvailable)
teamRocket = Team("Team Rocket")
teamRocket.assign_pokemon(pokemonAvailable)

# Printing what Pokemon each team enters with
print(f"\nTeam Rocket enters with {teamRocket.pokemon_names()}")
print(f"\n{playerTeam.name} enters with {playerTeam.pokemon_names()}")


# Coin toss to determine who goes first
firstTeam = random.choice([playerTeam.name, teamRocket.name])
currentMove = firstTeam
print("\nFirst up is: " + currentMove)

# Battle implementation
gameOver = False
while gameOver == False:
    if currentMove == playerTeam.name:
        pass
    else:
        pass



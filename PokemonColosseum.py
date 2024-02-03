import random
from Teams import Team
from Pokemon import pokemon_list
from Damage import damage

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
print("\nLet the battle begin!")

# Coin toss to determine who goes first
firstTeam = random.choice([playerTeam.name, teamRocket.name])
currentMove = firstTeam
print("Coin toss goes to ----- " + currentMove + " to start the attack!")


# Battle implementation
gameOver = False
while gameOver == False:
    currentPlayerPokemon = playerTeam.pokemon[0]
    currentRocketPokemon = teamRocket.pokemon[0]
    if currentMove == playerTeam.name:
        # Menu to choose move for player POKE
        # Print choice "Team Player's choice: X"
        # SAME CAST PRINT STATEMENT AS TEAM ROCKET WHEN CHOSEN
        # Damage calculation
        # Print "Now ROCKETPOKE had XX HP, and TEAMPOKE has XX HP."
        # If HP for one of the pokemon falls below 0, then say "POKE faints back to poke ball"
        gameOver = True
        pass
    else:
        selectedMove = teamRocket.selectTeamRocketMove(currentRocketPokemon)
        damageNum = damage(selectedMove, currentRocketPokemon, currentPlayerPokemon)
        print(f"Team Rocket's {currentRocketPokemon.name} cast '{selectedMove.name}' to {currentPlayerPokemon.name}")
        print(f"Damage to {currentPlayerPokemon.name} is {damageNum} points.")
        # Print "Damage to POKEMON is XX Points"
        # Calculate HP
        # Print "Now ROCKETPOKE had XX HP, and TEAMPOKE has XX HP."
        # If HP for one of the pokemon falls below 0, then say "POKE faints back to poke ball"
        gameOver = True
        pass



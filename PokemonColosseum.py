import random
from Teams import Team
from Pokemon import pokemonList
from Damage import damage

# Initialize game
print("\nWelcome to Pokemon Colosseum!\n")

# Get player name
playerName = input("Enter Player Name: ")

# Create teams and assign Pokemon
pokemonAvailable = pokemonList.copy()
playerTeam = Team("Team " + playerName)
playerTeam.assignPokemon(pokemonAvailable)
teamRocket = Team("Team Rocket")
teamRocket.assignPokemon(pokemonAvailable)

# Printing what Pokemon each team enters with
print(f"\nTeam Rocket enters with {teamRocket.pokemonNames()}")
print(f"\n{playerTeam.name} enters with {playerTeam.pokemonNames()}")
print("\nLet the battle begin!")

# Coin toss to determine who goes first
firstTeam = random.choice([playerTeam.name, teamRocket.name])
currentMove = firstTeam
print("Coin toss goes to ----- " + currentMove + " to start the attack!")


# Battle implementation
# I would have loved to have put this in it's own class and file, but I got on a time crunch so I implemented here.
# Main loop
gameOver = False
while gameOver is False:
    # Assigning current Pokemon in battle
    currentPlayerPokemon = playerTeam.pokemon[0]
    currentRocketPokemon = teamRocket.pokemon[0]

    # Checking which team's move it is
    # If Player's turn, then letting them choose a move from a menu.
    if currentMove == playerTeam.name:
        print(f"\nChoose the move for {currentPlayerPokemon.name}")
        for i, move in enumerate(currentPlayerPokemon.moves, start = 1):
            print(f"{i}. {move.name}")

        print("\n")

        # Checking that user input is valid, and not outside parameters.
        validMoveSelection = False
        while not validMoveSelection:
            try:
                moveSelection = int(input()) - 1
                if 0 <= moveSelection < len(currentPlayerPokemon.moves):
                    selectedMove = currentPlayerPokemon.moves.pop(moveSelection)
                    validMoveSelection = True
                else:
                    print("Please enter a number that corresponds to an available move.")
            except ValueError:
                print("Please enter a number that corresponds to an available move.")
        
        print(f"\n{playerTeam.name}'s choice: {(moveSelection + 1)}\n")

        # If needed, resetting move sets
        if not currentPlayerPokemon.moves:
            currentPlayerPokemon.resetMoves()

        # Damage calculation and displaying move's damage
        damageNum = damage(selectedMove, currentPlayerPokemon, currentRocketPokemon)
        print(f"{playerTeam.name}'s {currentPlayerPokemon.name} cast '{selectedMove.name}' to {currentRocketPokemon.name}")
        print(f"Damage to {currentRocketPokemon.name} is {damageNum} points.")

        # Removing damage from HP and then checking Team Rockets Pokemon's HP after move
        currentRocketPokemon.hp = currentRocketPokemon.hp - damageNum
        if currentRocketPokemon.checkHp() is False:
            print(f"Now {currentRocketPokemon.name} faints back to poke ball., and {currentPlayerPokemon.name} has {currentPlayerPokemon.hp} HP.")
            teamRocket.pokemon.pop(0)
            if not teamRocket.pokemon:
                print(f"\nAll of Team Rocket's Pokemon fainted, and {playerTeam.name} prevails!")
                gameOver = True
            else:
                print(f"\nNext for Team Rocket, {teamRocket.pokemon[0].name} enters battle!\n")
        else: 
            print(f"Now {currentRocketPokemon.name} has {currentRocketPokemon.hp} HP, and {currentPlayerPokemon.name} has {currentPlayerPokemon.hp} HP")
            currentMove = teamRocket.name
        pass

    # Team Rocket's turn and move selection
    else:
        # Function I created in the team class to randomly pick Team Rocket's move.
        selectedMove = teamRocket.selectTeamRocketMove(currentRocketPokemon)

        # Damage calculation and print statements
        damageNum = damage(selectedMove, currentRocketPokemon, currentPlayerPokemon)
        print(f"\nTeam Rocket's {currentRocketPokemon.name} cast '{selectedMove.name}' to {currentPlayerPokemon.name}")
        print(f"Damage to {currentPlayerPokemon.name} is {damageNum} points.")

        # Calculating Player's Pokemon's HP
        currentPlayerPokemon.hp = currentPlayerPokemon.hp - damageNum

        # Checking if Player's Pokemon fainted.
        if currentPlayerPokemon.checkHp() is False:
            print(f"Now {currentRocketPokemon.name} has {currentRocketPokemon.hp} HP, and {currentPlayerPokemon.name} faints back to poke ball.")
            playerTeam.pokemon.pop(0)
            if not playerTeam.pokemon:
                print(f"\nAll of Team {playerTeam.name}'s Pokemon fainted, and Team Rocket prevails!")
                gameOver = True
            else:
                print(f"\nNext for {playerTeam.name}, {playerTeam.pokemon[0].name} enters battle!\n")
        else: 
            print(f"Now {currentRocketPokemon.name} has {currentRocketPokemon.hp} HP, and {currentPlayerPokemon.name} has {currentPlayerPokemon.hp} HP")

        # Switching turns
        currentMove = playerTeam.name
        pass
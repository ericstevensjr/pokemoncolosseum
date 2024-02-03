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
        print(f"\nChoose the move for {currentPlayerPokemon.name}")
        for i, move in enumerate(currentPlayerPokemon.moves, start = 1):
            print(f"{i}. {move.name}")

        print("\n")

        moveSelection = int(input()) - 1
        print(f"\n{playerTeam.name}'s choice: {(moveSelection + 1)}\n")
        selectedMove = currentPlayerPokemon.moves.pop(moveSelection)
        if not currentPlayerPokemon.moves:
            currentPlayerPokemon.resetMoves()

        damageNum = damage(selectedMove, currentPlayerPokemon, currentRocketPokemon)
        print(f"{playerTeam.name}'s {currentPlayerPokemon.name} cast '{selectedMove.name}' to {currentRocketPokemon.name}")
        print(f"Damage to {currentRocketPokemon.name} is {damageNum} points.")

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

    else:
        selectedMove = teamRocket.selectTeamRocketMove(currentRocketPokemon)

        damageNum = damage(selectedMove, currentRocketPokemon, currentPlayerPokemon)
        print(f"\nTeam Rocket's {currentRocketPokemon.name} cast '{selectedMove.name}' to {currentPlayerPokemon.name}")
        print(f"Damage to {currentPlayerPokemon.name} is {damageNum} points.")

        currentPlayerPokemon.hp = currentPlayerPokemon.hp - damageNum
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

        currentMove = playerTeam.name
        pass



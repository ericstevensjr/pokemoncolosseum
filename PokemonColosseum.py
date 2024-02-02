import random
from Team import Team
from Pokemon import pokemon_list

# Initialize game
print("\nHello and welcome to Pokemon Colosseum!")

# Create teams and assign Pokemon
playerTeam = Team("Team Player")
playerTeam.assign_pokemon(pokemon_list)
playerTeam.print_team()
teamRocket = Team("Team Rocket")
teamRocket.assign_pokemon(pokemon_list)
teamRocket.print_team()




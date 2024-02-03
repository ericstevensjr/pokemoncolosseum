import random
import math

def damage(selectedMove, pokemonA, pokemonB):
    stabVal = stab(selectedMove, pokemonB)
    typeEffVal = typeEffeciency(selectedMove, pokemonB)
    randomInt = random.uniform(0.5, 1)
    damageCount = (float(selectedMove.power)) * ((float(pokemonA.attack) / (float(pokemonB.defense))) 
                                                 * stabVal * typeEffVal * randomInt)
    damageCount = math.ceil(damageCount)
    return damageCount    

def typeEffeciency(move, pokemon):
    match (move.type, pokemon.type):
        case ("Normal", "Normal"):
            return 1
        case ("Normal", "Fire"):
            return 1
        case ("Normal", "Water"):
            return 1
        case ("Normal", "Electric"):
            return 1
        case ("Normal", "Grass"):
            return 1
        case ("Fire", "Normal"):
            return 1
        case ("Fire", "Fire"):
            return 0.5
        case ("Fire", "Water"):
            return 0.5
        case ("Fire", "Electric"):
            return 1
        case ("Fire", "Grass"):
            return 2
        case ("Water", "Normal"):
            return 1
        case ("Water", "Fire"):
            return 2
        case ("Water", "Water"):
            return 0.5
        case ("Water", "Electric"):
            return 1
        case ("Water", "Grass"):
            return 0.5
        case ("Electric", "Normal"):
            return 1
        case ("Electric", "Fire"):
            return 1
        case ("Electric", "Water"):
            return 2
        case ("Electric", "Electric"):
            return 0.5
        case ("Electric", "Grass"):
            return 0.5
        case ("Grass", "Normal"):
            return 1
        case ("Grass", "Fire"):
            return 0.5
        case ("Grass", "Water"):
            return 2
        case ("Grass", "Electric"):
            return 1
        case ("Grass", "Grass"):
            return 0.5
        case _:
            return 1

def stab(moveA, pokemon2):
    if moveA.type == pokemon2.type:
        return 1.5
    else:
        return 1
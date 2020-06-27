import random

def printMapEnergy(nbRecharge, mapEnergie):
    compteur = 0
    while compteur < nbRecharge:
        compteur += 1
        index = random.randint(0, (len(mapEnergie) - 1))
        while mapEnergie[index] == "z" or index == 0:
            index = random.randint(0, (len(mapEnergie) - 1))
        mapEnergie[index] = "z"
    result = ""
    for i in mapEnergie:
        result = result + str(i)
    mapEnergie[index] = "-"
    return result

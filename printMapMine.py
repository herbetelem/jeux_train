import random

def printMapMine(nbMine, mapMine):
    compteur = 0
    while compteur < nbMine:
        compteur += 1
        index = random.randint(0, (len(mapMine) - 1))
        while isinstance(mapMine[index], int) or index == 0:
            index = random.randint(0, (len(mapMine) - 1))
        nbcaisse = random.randint(1, 9)
        mapMine[index] = nbcaisse
    result = ""
    for i in mapMine:
        result = result + str(i)
    mapMine[index] = "-"
    return result

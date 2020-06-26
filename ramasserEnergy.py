def ramasserEnergy(mapEnergy, energy, regenEnergy, positionTrain, coutCharge):
    energy = energy + regenEnergy - coutCharge
    listeMap = list(mapEnergy)
    listeMap[positionTrain] = "-"
    listeMap = "".join(listeMap)
    return listeMap, energy

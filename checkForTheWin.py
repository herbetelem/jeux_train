def checkForTheWin(mapTrain, longWay):
    mapTrain = list(mapTrain)
    compteur = 0
    for index in mapTrain:
        if index == "-":
            compteur += 1
    if compteur == longWay:
        return True
    else:
        return False
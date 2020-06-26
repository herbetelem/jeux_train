def ramasserMine(mapMine, energy, cargaison, positionTrain, coutCharge, cargaisonMax):
    newMap = ""
    chargementPossible = cargaisonMax - cargaison
    chargementPotentiel = int(mapMine[positionTrain])
    print("il y a " + str(chargementPotentiel) + " caisse, vous pouvez en prendre " + str(chargementPossible) + ".")
    nbCharge = int(input("Combien souhaitez vous en prendre : "))
    while nbCharge > chargementPotentiel or nbCharge > chargementPossible:
        if nbCharge > chargementPotentiel:
            nbCharge = int(input("il n'y a pas autant de caisse, veuillez ressaisir un chiffre : "))
        else:
            nbCharge = int(input("il n'y a pas assez de place, veuillez ressaisir un chiffre : "))
    else:
        reste = chargementPotentiel - nbCharge
        cargaison = cargaison + nbCharge
        listeMap = list(mapMine)
        if reste == 0:
            listeMap[positionTrain] = "-"
        else:
            listeMap[positionTrain] = str(reste)
        for index in listeMap:
            newMap = newMap + str(index)
        energy = energy - coutCharge
        return newMap, energy, cargaison







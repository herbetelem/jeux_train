# Import All Functions
import printMap as printMap
import printMapEnergy as printMapEnergy
import printMapMine as printMapMine
import printEnergy as printEnergy
import checkInt as checkInt
import ramasserEnergy as ramasserEnergy
import ramasserMine as ramasserMine
import livraison as livraison
import checkForTheWin as checkForTheWin
import loose as loose
import win as win
import testson as son
import checkIsInt as checkIsInt


print("Bonjour, blablabla jeux")
print()

# Set up variable, in auto mode or manual
mode = str(input("mode auto, oui ou non ? "))
if mode == "oui":
    longWay = 50
    MaxCargo = 10
    nbSpot = 20
    nbRecharge = 5
    energy = 200
    regenEnergy = 50
    coutRun = 1
    coutCharge = 2
else:
    longWay = int(input("longueur de la voie : "))
    MaxCargo = int(input("nombre de cargason max : "))
    nbSpot = int(input("nombre de spot : "))
    nbRecharge = int(input("nombre de recharge : "))
    energy = int(input("max energie : "))
    regenEnergy = int(input("regen energie : "))
    coutRun = int(input("cout d'energie par deplacement : "))
    coutCharge = int(input("cout d'energie par chargement : "))

lap = 0
cargo = 0
mapNormal = ["="] * longWay
mapEnergy = ["-"] * longWay
mapMine = ["-"] * longWay
positionTrain = 0
statut = "ok"
actionPossible = ["ramasser", "rouler", "livraison"]
mapPrintedEnergy = printMapEnergy.printMapEnergy(nbRecharge, mapEnergy)
mapPrintedMine = printMapMine.printMapMine(nbSpot, mapMine)



#print First map
print(printMap.printMap(0, mapNormal))
print(mapPrintedEnergy)
print(mapPrintedMine)
print("Il vous reste " + str(printEnergy.printEnergy(energy, 0, coutRun)) + " energie")



# Core Function
while statut == "ok":
    action = str(input("Que voulez vous faire ? rouler ou ramasser : "))
    while action not in actionPossible:
        action = str(input("rouler ou ramasser : "))
    if action == "rouler":
        moove = int(input(
            "quel distance voulez vous parcourir (positif pour aller en avant et negatif pour l'arriere) : "))
        while (positionTrain + moove) < 0 or (positionTrain + moove) > longWay:
            moove = int(input("veuillez ne pas sortir des voies "))
        positionTrain = positionTrain + moove
        energy = printEnergy.printEnergy(energy, abs(moove), coutRun)

    elif action == "ramasser":
        if mapPrintedMine[positionTrain] == "-" and mapPrintedEnergy[positionTrain] == "-":
            print("Il n'y a rien a ramsser ici")
        elif checkInt.checkInt(mapPrintedMine[positionTrain]) and mapPrintedEnergy[positionTrain] == "z":
            print("deux option s'offre avous, ramasser de l'energie ou des chargement")
            ChoicePickUp = str(
                input("que souhaitez vous prendre: energie ou chargement : "))
            choixPossible = ["energie", "chargement"]
            while ChoicePickUp not in choixPossible:
                ChoicePickUp = str(
                    input("energie ou chargement sont vos seuls option : "))
            if ChoicePickUp == "energie":
                action = ramasserEnergy.ramasserEnergy(
                    mapEnergy, energy, regenEnergy, positionTrain, coutCharge)
                energy = action[1]
                mapPrintedEnergy = action[0]
            else:
                action = ramasserMine.ramasserMine(
                    mapPrintedMine, energy, cargo, positionTrain, coutCharge, MaxCargo)
                energy = action[1]
                mapPrintedMine = action[0]
                cargo = action[2]
        elif checkInt.checkInt(mapPrintedMine[positionTrain]):
            action = ramasserMine.ramasserMine(
                mapPrintedMine, energy, cargo, positionTrain, coutCharge, MaxCargo)
            energy = action[1]
            mapPrintedMine = action[0]
            cargo = action[2]
        else:
            action = ramasserEnergy.ramasserEnergy(
                mapEnergy, energy, regenEnergy, positionTrain, coutCharge)
            energy = action[1]
            mapPrintedEnergy = action[0]
    else:
        action = livraison.livraison(energy, positionTrain)
        energy = action
        cargo = 0
        positionTrain = 0
    print(printMap.printMap(positionTrain, mapNormal))
    print(mapPrintedEnergy)
    print(mapPrintedMine)
    print()
    print("Il vous reste " + str(energy) + " energie")
    print("Votre chagement est de " + str(cargo) + "/" + str(MaxCargo) + ".")
    if cargo > 0:
        print("Si vous souhaitez vider votre chargement saisissez 'livraison'.")
    print()
    lap += 1
    if positionTrain == 0 and lap > 0:
        if checkForTheWin.checkForTheWin(mapPrintedMine, longWay):
            statut = "win"
    elif energy <= 0:
        statut = "ko"


if statut == "ko":
    loose.loose(lap)
    son.playMusicLost()

elif statut == "win":
    win.win(lap)
    son.playMusicWin()

import printMap as printMap
import printMapEnergy as printMapEnergy
import printMapMine as printMapMine
import printEnergy as printEnergy


print("Bonjour, blablabla jeux")
print()

longVoie = int(input("longueur de la voie : "))
mapNormal = ["="] * longVoie
mapEnergy = ["-"] * longVoie
mapMine = ["-"] * longVoie
nbSpot = int(input("nombre de spot : "))
nbRecharge = int(input("nombre de recharge : "))
energy = int(input("max energie : "))
regenEnergy = int(input("regen energie : "))
coutRun = int(input("cout d'energie par deplacement : "))
coutCharge = int(input("cout d'energie par chargement : "))
positionTrain = 0
statut = "ok"

actionPossible = ["ramasser", "rouler"]
mapPrintedEnergy = printMapEnergy.printMapEnergy(nbRecharge, mapEnergy)
mapPrintedMine = printMapMine.printMapMine(nbSpot, mapMine)



print(printMap.printMap(0, mapNormal))
print(mapPrintedEnergy)
print(mapPrintedMine)
print("Il vous reste " + str(printEnergy.printEnergy(energy, 0, coutRun)) + " energie")

while statut == "ok":
    if energy <= 0:
        statut = "ko"
    else:
        action = str(input("Que voulez vous faire ? rouler ou ramasser : "))
        while action not in actionPossible:
            action = str(input("rouler ou ramasser : "))
        if action == "rouler":
            deplacement = int(input("quel distance voulez vous parcourir (positif pour aller en avant et negatif pour l'arriere) : "))
            while (positionTrain + deplacement) < 0 or (positionTrain + deplacement) > longVoie:
                deplacement = int(input("veuillez ne pas sortir des voies "))
            positionTrain = positionTrain + deplacement
            energy = printEnergy.printEnergy(energy, abs(deplacement), coutRun)
            print(printMap.printMap(positionTrain, mapNormal))
            print(mapPrintedEnergy)
            print(mapPrintedMine)
            print("Il vous reste " + str(energy) + " energie")
        else:
            if mapPrintedMine[positionTrain] == "-" and mapPrintedEnergy[positionTrain] == "-":
                print("Il n'y a rien a ramsser ici")



if statut == "ko":
    print()
    print("   ________                        ________                      ")
    print("  /  _____/_____    _____   ____   \_____  \___  __ ___________  ")
    print(" /   \  ___\__  \  /     \_/ __ \   /   |   \  \/ // __ \_  __ \ ")
    print(" \    \_\  \/ __ \|  Y Y  \  ___/  /    |    \   /\  ___/|  | \/ ")
    print("  \______  (____  /__|_|  /\___  > \_______  /\_/  \___  >__|    ")
    print("         \/     \/      \/     \/          \/          \/        ")
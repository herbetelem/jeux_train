import printMap as printMap
import printMapEnergy as printMapEnergy
import printMapMine as printMapMine
import printEnergy as printEnergy
import checkInt as checkInt
import ramasserEnergy as ramasserEnergy
import ramasserMine as ramasserMine
import livraison as livraison
import checkForTheWin as checkForTheWin


print("Bonjour, blablabla jeux")
print()

mode = str(input("mode auto, oui ou non ? "))
if mode == "oui":
    longVoie = 50
    maxCargaison = 10
    mapNormal = ["="] * longVoie
    mapEnergy = ["-"] * longVoie
    mapMine = ["-"] * longVoie
    cargaison = 0
    nbSpot = 20
    nbRecharge = 5
    energy = 200
    regenEnergy = 50
    coutRun = 1
    coutCharge = 2
else:
    longVoie = int(input("longueur de la voie : "))
    maxCargaison = int(input("nombre de cargason max : "))
    mapNormal = ["="] * longVoie
    mapEnergy = ["-"] * longVoie
    mapMine = ["-"] * longVoie
    cargaison = 0
    nbSpot = int(input("nombre de spot : "))
    nbRecharge = int(input("nombre de recharge : "))
    energy = int(input("max energie : "))
    regenEnergy = int(input("regen energie : "))
    coutRun = int(input("cout d'energie par deplacement : "))
    coutCharge = int(input("cout d'energie par chargement : "))
positionTrain = 0
statut = "ok"

actionPossible = ["ramasser", "rouler", "livraison"]
mapPrintedEnergy = printMapEnergy.printMapEnergy(nbRecharge, mapEnergy)
mapPrintedMine = printMapMine.printMapMine(nbSpot, mapMine)



print(printMap.printMap(0, mapNormal))
print(mapPrintedEnergy)
print(mapPrintedMine)
print("Il vous reste " + str(printEnergy.printEnergy(energy, 0, coutRun)) + " energie")

while statut == "ok":
    if positionTrain == 0:
        if checkForTheWin.checkForTheWin(mapPrintedMine, longVoie):
            statut = "win"
    
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
            
        elif action == "ramasser":
            if mapPrintedMine[positionTrain] == "-" and mapPrintedEnergy[positionTrain] == "-":
                print("Il n'y a rien a ramsser ici")
            elif checkInt.checkInt(mapPrintedMine[positionTrain]) and mapPrintedEnergy[positionTrain] == "z":
                print("deux option s'offre avous, ramasser de l'energie ou des chargement")
                choixRammasser = str(input("que souhaitez vous prendre: energie ou chargement : "))
                choixPossible = ["energie", "chargement"]
                while choixRammasser not in choixPossible:
                    choixRammasser = str(input("energie ou chargement sont vos seuls option : "))
                if choixRammasser == "energie":
                    action = ramasserEnergy.ramasserEnergy(mapEnergy, energy, regenEnergy, positionTrain, coutCharge)
                    energy = action[1]
                    mapPrintedEnergy = action[0]
                else:
                    action = ramasserMine.ramasserMine(mapPrintedMine, energy, cargaison, positionTrain, coutCharge, maxCargaison)
                    energy = action[1]
                    mapPrintedMine = action[0]
                    cargaison = action[2]
            elif checkInt.checkInt(mapPrintedMine[positionTrain]):
                action = ramasserMine.ramasserMine(mapPrintedMine, energy, cargaison, positionTrain, coutCharge, maxCargaison)
                energy = action[1]
                mapPrintedMine = action[0]
                cargaison = action[2]
            else:
                action = ramasserEnergy.ramasserEnergy(mapEnergy, energy, regenEnergy, positionTrain, coutCharge)
                energy = action[1]
                mapPrintedEnergy = action[0]
        else:
            action = livraison.livraison(energy, positionTrain)
            energy = action
            cargaison = 0
            positionTrain = 0
        print(printMap.printMap(positionTrain, mapNormal))
        print(mapPrintedEnergy)
        print(mapPrintedMine)
        print()
        print("Il vous reste " + str(energy) + " energie")
        print("Votre chagement est de " + str(cargaison) + "/" + str(maxCargaison) + ".")
        if cargaison > 0:
            print("Si vous souhaitez vider votre chargement saisissez 'livraison'.")
        print()


if statut == "ko":
    print()
    print("   ________                        ________                      ")
    print("  /  _____/_____    _____   ____   \_____  \___  __ ___________  ")
    print(" /   \  ___\__  \  /     \_/ __ \   /   |   \  \/ // __ \_  __ \ ")
    print(" \    \_\  \/ __ \|  Y Y  \  ___/  /    |    \   /\  ___/|  | \/ ")
    print("  \______  (____  /__|_|  /\___  > \_______  /\_/  \___  >__|    ")
    print("         \/     \/      \/     \/          \/          \/        ")

elif statut == "win":
    print()
    print("                  _-====-__-======-__-========-_____-============-__")
    print("                _(                                                 _)")
    print("             OO(            Vous avez Gagné, BRAVO !!!               )_")
    print("            0  (_                                                   _)")
    print("          o0     (_                                                _)")
    print("         o         '=-___-===-_____-========-___________-===-dwb-='")
    print("       .o                                _________")
    print("      . ______          ______________  |         |      _____")
    print("    _()_||__|| ________ |            |  |_________|   __||___||__")
    print("   (         | |      | |            | __Y______00_| |_         _|")
    print("  /-OO----OO''=''OO--OO'='OO--------OO'='OO-------OO'='OO-------OO'=P")
    print("######################################################################")
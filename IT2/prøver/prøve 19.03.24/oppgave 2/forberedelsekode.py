import csv
import matplotlib.pyplot as plt

import os
def absRef(relRef): # funksjon for å finne absolutt referanse til en fil fra relativ referanse
    return os.path.join(os.path.dirname(__file__), relRef)


with open(absRef("treningsData.csv"), encoding="utf-8-sig") as fil:
    filinnhold = csv.reader(fil, delimiter=",")
    overskrifter = next(filinnhold)
    data = allData = list(filinnhold)[1:-1]

    with open(absRef('tempFil.csv'), 'w+') as tempFil:

        data = []
        for linje in allData:
            if linje[2] == '1':
                tempFil.write(str(linje) + '\n')
                data.append(linje)
        
    # with open(absRef('tempFil.csv'), 'w+') as tempFil:

    #     data = []
    #     for i in range(100000):
    #         linje = fil.readline()
    #         tempFil.write(linje)
    #         data.append(linje)

print('ferdig lastet inn')
print(overskrifter)



print(len(data))

lengder = []
tider = []
farter = []

for uke in data:
    lengder.append(float(uke[3]))
    tider.append(float(uke[4]))
    farter.append(float(uke[3])/float(uke[4]))



plt.plot(range(1,53), lengder)
plt.xlabel('uker')
plt.ylabel('lengde')
plt.show()

plt.plot(range(1,53), tider)
plt.xlabel('uker')
plt.ylabel('tid')
plt.show()

plt.plot(range(1,53), farter)
plt.xlabel('uker')
plt.ylabel('fart')
plt.show()






exit()


mannLand = []
kvinneLand = []

alleLandListe = []

for linje in data:
    
    if not linje[7] in alleLandListe:
        alleLandListe.append(linje[7])

    if linje[5] == 'M':
        mannLand.append(linje[7])
    else:
        kvinneLand.append(linje[7])


def tellLike(liste):
    tellere = {}
    for ting in liste:
        if ting in tellere:
            tellere[ting] +=1
        else:
            tellere[ting] = 1

    return tellere

antallLandM = tellLike(mannLand)
antallLandK = tellLike(kvinneLand)
print(antallLandM)
print(antallLandK)

nyAntallLand = {}
nyAntallLand['Andre Land Menn'] = 0
nyAntallLand['Andre Land Kvinner'] = 0



for land in alleLandListe:

    if land in antallLandM:
        if antallLandM[land] < 50 or land == '':
            nyAntallLand['Andre Land (Menn)'] += antallLandM[land]
        else:
            nyAntallLand[str(land) + ' (Menn)'] = antallLandM[land]

    if land in antallLandK:
        if antallLandK[land] < 50 or land == '':
            nyAntallLand['Andre Land (Kvinner)'] += antallLandK[land]
        else:
            nyAntallLand[str(land) + ' (Kvinner)'] = antallLandK[land]


        

plt.figure(figsize=(10, 10))          # Angir dimensjoner for figure-objektet
plt.barh(list(nyAntallLand.keys()), list(nyAntallLand.values()))   # Lager stolpediagrammet
plt.grid(axis='x')                   # Legger til rutenett (bare vertikale linjer)
plt.show()   
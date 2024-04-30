import csv
import matplotlib.pyplot as plt
import datetime

import os
def absRef(relRef): # funksjon for å finne absolutt referanse til en fil fra relativ referanse
    return os.path.join(os.path.dirname(__file__), relRef)


with open(absRef("treningsData.csv"), encoding="utf-8-sig") as fil:
    filinnhold = csv.reader(fil, delimiter=",")
    overskrifter = next(filinnhold)
    data = allData = list(filinnhold)[1:-1]

print('ferdig lastet inn')
print(overskrifter)

aldre = {}
for linje in data:
    if not linje[2] in aldre:
        aldre[linje[2]] = linje[6]
# lager et dictionary med alder for hver utøver

def tellLike(liste):
    tellere = {}
    for ting in liste:
        if ting in tellere:
            tellere[ting] +=1
        else:
            tellere[ting] = 1

    return tellere


aldersgrupper = tellLike(aldre.values())
for gruppe in aldersgrupper:
    print(f'I aldersgruppen {gruppe} er det {aldersgrupper[gruppe]} utøvere')



plt.figure(figsize=(10, 10))          # Angir dimensjoner
plt.barh(list(aldersgrupper.keys()), list(aldersgrupper.values()))   # Lager stolpediagrammet
plt.grid(axis='x')                   # Legger til rutenett (bare vertikale linjer)
plt.show()  


# langt fra ferdig svar på del 3
for i in range(10):
    ukenr = datetime.date(data[i][1]).strftime("%V")



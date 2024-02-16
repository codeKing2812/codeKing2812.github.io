import csv
import pandas as pd

import os
def absRef(relRef): # funksjon for å finne absolutt referanse til en fil fra relativ referanse
    return os.path.join(os.path.dirname(__file__), relRef)


with open(absRef("sykkel.csv"), encoding="utf-8-sig") as fil:
    filinnhold = csv.reader(fil, delimiter=";")

    overskrifter = next(filinnhold)
    print(overskrifter)


    data = list(filinnhold)[1:-1]
    

# skill ut startposisjon
    
start = []
for i in data: 
    rad = rad[0].split(',')
    start.append(rad[4])


# tell hvor mange turer som starter hver plass
    
tellere = {}
for plass in start:
    if plass in tellere:
        tellere[plass] +=1
    else:
        tellere[plass] = 1

print(tellere)
 

# sorteringsfunksjon

toppTre = [('',0)] * 3
print(toppTre)

for i in tellere:
    if tellere[i] >= toppTre[0][1]:

        toppTre[2] = toppTre[1]
        toppTre[1] = toppTre[0]
        # flytt ned de som allerede er på listen

        toppTre[0] = (i, tellere[i])
        # legg til ny toppplassering

        print(toppTre)


print(toppTre[0][0], 'er mest brukt, med', toppTre[0][1], 'turer')
print(toppTre[1][0], 'er nest mest brukt, med', toppTre[1][1], 'turer')
print(toppTre[2][0], 'er tredje mest brukt, med', toppTre[2][1], 'turer')


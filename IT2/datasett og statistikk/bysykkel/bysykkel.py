import csv

import os
def absRef(relRef): # funksjon for å finne absolutt referanse til en fil fra relativ referanse
    return os.path.join(os.path.dirname(__file__), relRef)


with open(absRef("sykkel.csv"), encoding="utf-8-sig") as fil:
    filinnhold = csv.reader(fil, delimiter=";")

    overskrifter = next(filinnhold)
    print(overskrifter)


    data = list(filinnhold)[1:-1]
    


start = []
for i in range(300): 
    rad = data[i][0].split(',')
    
    start.append(rad[4])



tellere = {}
for plass in start:
    if plass in tellere:
        tellere[plass] +=1
    else:
        tellere[plass] = 1
    
print(tellere)


# sortering som ikke funker enda:

# mest = 0
# for i in tellere.values():
#     if i > mest:
#         mest = i
#         mestNavn = tellere[tellere.values().index(i)]

# print(mestNavn, mest)


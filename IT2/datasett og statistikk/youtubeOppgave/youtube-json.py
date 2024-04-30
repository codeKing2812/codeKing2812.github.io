import json

import os
def absRef(relRef): # funksjon for å finne absolutt referanse til en fil fra relativ referanse
    return os.path.join(os.path.dirname(__file__), relRef)


with open(absRef("youtube.json"), encoding='utf-8') as fil:
    data = json.load(fil)



alleLand = []
for kanal in data:
    
    alleLand.append(kanal['Country'])
    

tellere = {}
for land in alleLand:
    if land in tellere:
        tellere[land] +=1
    else:
        tellere[land] = 1

print(tellere)


# sorteringsfunksjon

lengde = 3

toppListe = [('',0)] * lengde
print(toppListe)

for land in tellere:

    i = lengde - 1
    while tellere[land] >= toppListe[i][1]:
        
        if i > lengde-1:
            toppListe[i+1] = toppListe[i]
        
        toppListe[i] = (land, tellere[land])

        i+=1
    
    print(tellere)



if tellere[land] >= toppListe[2][1]:
    # hvis større enn tredjeplass

    if tellere[land] >= toppListe[1][1]:
    # hvis større enn andreplass
        
        toppListe[2] = toppListe[1]
        # flytt ned
        
        if tellere[land] >= toppListe[0][1]:
            # hvis større enn førsteplass
            
            toppListe[1] = toppListe[0]
            # flytt ned

            toppListe[0] = (land, tellere[land])
            # legg til ny plassering

        else:
            # ny andreplass
            toppListe[1] = (land, tellere[land])

    else:
        # ny tredjeplass
        toppListe[2] = (land, tellere[land])

    print(toppListe)



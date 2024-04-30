import csv

import os
def absRef(relRef): # funksjon for å finne absolutt referanse til en fil fra relativ referanse
    return os.path.join(os.path.dirname(__file__), relRef)


with open(absRef("sykkel.csv"), encoding="utf-8-sig") as fil:
    filinnhold = csv.reader(fil, delimiter=";")

    # overskrifter = next(filinnhold)
    # print(overskrifter)


    data = list(filinnhold)[1:-1]
    

# skill ut startposisjon
    
start = []
for rad in data: 
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

toppListe = [('',0)] * 3
print(toppListe)

for i in tellere:
    if tellere[i] >= toppListe[2][1]:
        # hvis større enn tredjeplass

        if tellere[i] >= toppListe[1][1]:
        # hvis større enn andreplass
            
            toppListe[2] = toppListe[1]
            # flytt ned
            
            if tellere[i] >= toppListe[0][1]:
                # hvis større enn førsteplass
                
                toppListe[1] = toppListe[0]
                # flytt ned

                toppListe[0] = (i, tellere[i])
                # legg til ny plassering

            else:
                # ny andreplass
                toppListe[1] = (i, tellere[i])
                
        else:
            # ny tredjeplass
            toppListe[2] = (i, tellere[i])

    
        print(toppListe)


print(toppListe[0][0], 'er mest brukt, med', toppListe[0][1], 'turer')
print(toppListe[1][0], 'er nest mest brukt, med', toppListe[1][1], 'turer')
print(toppListe[2][0], 'er tredje mest brukt, med', toppListe[2][1], 'turer')


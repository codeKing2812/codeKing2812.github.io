############################### DEL A ###############################

""" 
Problemtiske data i et slikt datasett kan være hvis noe av dataen inneholder komma.
Det vil gjøre at når vi leser csv-filen vil vi få for mange verdier, og de vil ikke treffe riktig i forhold til hva verdien representerer i første linje.

Et annet problem er hvis brukeren som har lagt inn data om sitt hjem ikke har fylt ut alle feltene.
Det burde ikke føre til feil i lesingen av dataene, men det kan skape feil i statistikken. 
 """



############################### DEL B ###############################

import csv

import os # Funksjon for å finne absolutt referanse til en fil fra relativ referanse.
def absRef(relRef): # Denne er hentet fra mange av egne tidligere oppgaver.
    return os.path.join(os.path.dirname(__file__), relRef)


with open(absRef('utleige.csv')) as fil:
    filinnhold = csv.reader(fil, delimiter=",")
    overskrifter = next(filinnhold)
    data = list(filinnhold)[1:-1]


sum = 0
priser = []
for linje in data:
    pris = int(linje[9])

    # etter å ha funnet min og max ser jeg at jeg må fjerne verdier jeg anser som urelalistiske og som feil.
    if 0 < pris and pris < 9999:

        priser.append(pris)
        sum += int(pris)




snitt = sum/len(priser)

print('snitt:', snitt)
print('høyeste pris:', max(priser))
print('laveste pris:', min(priser))

""" 
Resultat:
snitt: 151.54763073901302
høyeste pris: 8500
laveste pris: 10

Første gang jeg gjorde dette, altså før jeg fjernet problematiske verdier, fikk jeg:
snitt: 152.72204610066882
høyeste pris: 9999
laveste pris: 0
 """


############################### DEL C + D ###############################

import matplotlib.pyplot as plt


def tellLike(liste):
    tellere = {}
    for ting in liste:
        if ting in tellere:
            tellere[ting] +=1
        else:
            tellere[ting] = 1

    return tellere


def topp5(kolonneNavn):
    kolonne = overskrifter.index(kolonneNavn)

    verdiListe = []
    for linje in data:
        verdiListe.append(linje[kolonne])

    antall = tellLike(verdiListe)

    # Hentet 19.april fra https://www.freecodecamp.org/news/sort-dictionary-by-value-in-python/#howtosortdatawiththesortedmethod
    antall = sorted(antall.items(), key=lambda x:x[1], reverse=True)

    print(f'Den {kolonneNavn} som har flest hus på markedet er {antall[0][0]} med {antall[0][1]} stk')
    

    navnListe = []
    verdiListe = []
    for i in range(5):
        navnListe.append(antall[i][0])
        verdiListe.append(antall[i][1])
    
    plt.figure(figsize=(15, 5))
    plt.barh(navnListe, verdiListe)
    plt.show()

    

topp5("host_name")
topp5("neighbourhood")



############################### DEL E ###############################

'''
Her fikk jeg problemer med å installere osmnx for å lage et kart.

Forøvrig er den koden som står her hentet fra IT2 boken, fordi jeg ikke begynte på tilpasning fra mitt datasett, pga feilen.
Koder er hentet her: https://innhold.aunivers.no/fagpakker/realfag/informasjonsteknologi-1-2/it-2/3-databehandling/eksempel-kart-og-data
'''

import osmnx as ox
import folium as fol

punkter = [
  [59.9139, 10.7522],
  [55.6761, 12.5683],
  [59.3293, 18.0686]  
]

# Beregner snittet av breddegrader og lengdegrader for å finne 
# et punkt midt mellom alle byene.
bredde_sum = 0
lengde_sum = 0

for punkt in punkter:
  bredde_sum += punkt[0]
  lengde_sum += punkt[1]

bredde_snitt = bredde_sum / len(punkter)
lengde_snitt = lengde_sum / len(punkter)

# Lager et kart
m = fol.Map([bredde_snitt, lengde_snitt], zoom_start=6)

# Legger til byene
for punkt in punkter:
  fol.CircleMarker(punkt).add_to(m)

# Lagrer kartet
m.save("skandinavia.html")



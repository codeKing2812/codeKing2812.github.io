
import json


import os # Funksjon for å finne absolutt referanse til en fil fra relativ referanse.
def absRef(relRef): # Denne er hentet fra mange av egne tidligere oppgaver.
    return os.path.join(os.path.dirname(__file__), relRef)



# with open(absRef('samling.json'), 'r') as fil:
#     data = json.load(fil)



# lager en liste til å ha alle objektene i samlingen i 
objektListe = [] 


# brukeren kan legge inn nye objekter etterhvert som han legger til mer i samlingen sin
def inputNyttObjekt(): 
    type = input('Type objekt:')
    franchise = input('Franchise:')
    pris = int(input('Kjøpspris:'))
    verdi = int(input('Verdi for øyeblikket:'))
    nyttObjekt(type, franchise, pris, verdi)

# opretter et nytt objekt i listen over objekter
def nyttObjekt(type, franchise, pris, verdi=None): 
    if not verdi:
        verdi = pris
    
    objekt = Samleobjekt(type, franchise, pris, verdi)
    objektListe.append(objekt)



# lagrer alle objektene til en json-fil
def lagreTilFil():
    # jeg har hentet kode for filbehandling fra https://www.geeksforgeeks.org/reading-writing-text-files-python/ 
    with open(absRef('samling.json'), 'w') as fil:
        
        # jeg har hentet kode for behandling av json fra https://www.geeksforgeeks.org/read-json-file-using-python/ og https://www.geeksforgeeks.org/read-write-and-parse-json-using-python/ 

        data = '{"Samling":['
        for objekt in objektListe:
            data += json.dumps(objekt.lagDict())
            if not objekt == objektListe[-1]:
                data += ','
        data += ']}'

        print('Lagrer data...')
        fil.write(data)


def visSamling():
    i = 1
    for objekt in objektListe:
        print('\nObjekt nr', i, ':')
        objekt.printSelv()
        i+=1


# finner objekter med en egenskap(feks. franchaise) som er navn(feks. Minecraft)
def søk(egenskap, navn):
    for objekt in objektListe:
        if objekt.lagDict()[egenskap] == navn:
            objekt.printSelv()

        



class Samleobjekt:
    def __init__(self, type, franchise, pris, verdi):
        self.type = type
        self.franchise = franchise
        self.pris = pris
        self.verdi = verdi
    
    @property
    def fortjeneste(self):
        return self.verdi - self.pris

    def lagDict(self):
        return( {
            'type': self.type, 
            'franchise': self.franchise,
            'pris': self.pris,
            'verdi': self.verdi,
            'fortjeneste': self.fortjeneste
            } )
    
    def printSelv(self):
        dict = self.lagDict()
        for key in dict:
            print(key, ':', dict[key])
    




nyttObjekt('spill', 'minecraft', 200, 190)
nyttObjekt('blad', 'donald duck', 7.5, 100)
nyttObjekt('film', 'donald duck', 120)
nyttObjekt('spill', 'gta v', 400, 350)
nyttObjekt('film', 'jurassic park', 150, 300)
nyttObjekt('plakat', 'jurassic park', 50, 500)


######################### BRUKERGRENSESNITT ####################

os.system('clear')

print('-- __  S A M L E R A P P E N  __ --')
print()
print('Hva vil du gjøre i dag?')
print('Trykk V for å vise samlingen')
print('Trykk L for å legge til nye samleobjekter')
print('Trykk S for å søke etter en type objekter')


# jeg har brukt https://www.geeksforgeeks.org/python-match-case-statement/ for hjelp med match-case
def hvaSkalDuGjøre():
    inn = input()

    match inn.lower():
        case 'v':
            visSamling()

        case 'l':
            inputNyttObjekt()

        case 's':
            print('Hva vil du søke etter? Skriv type eller franchise')
            egenskap = input().lower()
            print(f'Skriv inn {egenskap}n du vil søke etter')
            navn = input().lower()
            søk(egenskap, navn)

        case _ :
            print('Skriv enten S, L eller F')
            hvaSkalDuGjøre()

hvaSkalDuGjøre()




lagreTilFil()
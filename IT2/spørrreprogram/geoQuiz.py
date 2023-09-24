import json
import random

fil = open('landData.json', 'r')

landListe = json.loads(fil.read())[1]

# print(type(landListe))


# fjerner alle land uten hovedstad
nyListe = [] 
for land in landListe:
    if land['capitalCity'] != "" :
        nyListe.append(land)
landListe = nyListe


# print(landListe[5]['incomeLevel']['value'])

# Quiz

def spørsmål(kategori, underkat=0):

    land = random.choice(landListe)
    fasit = ''

    svar = input(f'What is {kategori} in {land["name"]}?')

    if str(type(land[kategori])).find('dict') == -1:
        #hvis kategorien ikke er et dictionary
        fasit = land[kategori]
    else: 
        #hvis kategorien er et dictionary gå et hakk dypere
        fasit = land[kategori][underkat]

     

    if svar.casefold() == fasit.casefold() :
        print('Hurray! Correct!')
    else:
        print(f'You suck. The answer is{fasit}')

spørsmål("capitalCity")

spørsmål("incomeLevel", "value")


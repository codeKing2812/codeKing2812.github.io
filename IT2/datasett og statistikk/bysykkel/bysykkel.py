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
    for i in range(10): 
        rad = csv.reader(data[i][0], delimiter=',')

        print(type(rad))
        # print(len(rad))
        print(rad)
    


    

    # tellere = {}
    # for i in start:
    #     if tellere[i]:
    #         tellere[i] +=1
    #     else:
    #         tellere[i] = 0
    
    # print(tellere)

        


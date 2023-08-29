import os
import time

class design:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


plass = 0
def animerPikselrad(piksler, forskyvning):
        index = plass + forskyvning
        if index > len(piksler)-1:
            index -= len(piksler)

        piksler[index] =  (design.HEADER + 'o ' + design.END)
        piksler[index-1] = 'o '

        pikselString = ''
        for i in range(len(piksler)):
            pikselString += piksler[i]
        print(pikselString)
        
        

rader = []
for i in range(10):
    rad = ['o ']*30
    rader.append(rad)


for i in range(20):
    plass = 0
    while plass < len(rad):
        animerPikselrad(rader[0], -1)
        animerPikselrad(rader[1], 0)
        animerPikselrad(rader[2], 1)
        animerPikselrad(rader[3], 2)
        animerPikselrad(rader[4], 3)
        animerPikselrad(rader[5], 3)
        animerPikselrad(rader[6], 2)
        animerPikselrad(rader[7], 1)
        animerPikselrad(rader[8], 0)
        animerPikselrad(rader[9], -1)
        plass +=1

        time.sleep(0.05)
        os.system('cls')
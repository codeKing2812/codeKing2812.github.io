import os
import time
import keyboard

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
def animerPikselrad(vertikal, plass):
        
        rad = rader[vertikal]
        rad[plass] =  (design.HEADER + 'o ' + design.END)
        # gjør pikselen lilla

        
        
        pikselString = ''
        for i in range(len(rad)):
            pikselString += rad[i]
        print(pikselString) # skriver ut raden

        rad[plass] =  ('o ')
        # gjør den vanlig igjen



        
        

rader = []
for i in range(10):
    rad = ['o ']*30
    rader.append(rad)


tid = time.time()
for i in range(20):
    plass = 0
    while time.time() < tid + 30:
        if time.time() > tid + 0.1: # kjør hvert tiendedels sekund
            
            os.system('cls')
            tid += 0.1
            
            if keyboard.is_pressed('d'):
                plass += 1
            elif keyboard.is_pressed('a'):
                plass -= 1

            animerPikselrad(0, plass)
            animerPikselrad(1, plass)
            animerPikselrad(2, plass)
            animerPikselrad(3, plass)
            animerPikselrad(5, plass)
            animerPikselrad(6, plass)
            animerPikselrad(7, plass)
            animerPikselrad(8, plass)
            animerPikselrad(9, plass)
            animerPikselrad(4, plass + 5)



            



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

fargetpx = design.HEADER + 'o ' + design.END


def piksel(x, y, farge):
    if farge == 'l':
        rader[y][x] =  (design.HEADER)
    elif farge == 'b':
        rader[y][x] =  (design.BLUE)
    elif farge == 'g':
        rader[y][x] =  (design.GREEN)
        
    rader[y][x] += ('o ' + design.END)



xpos = 0
ypos = 0

tid = time.time()
for i in range(20):
    while time.time() < tid + 30:
        if time.time() > tid + 0.1: # kjør hvert tiendedels sekund
            
            rader = []
            for i in range(10):
                rad = ['o ']*25
                rader.append(rad)
            # Reset alle rader


            os.system('cls')
            tid += 0.1 
            #refresh skjermen

            
            if keyboard.is_pressed('d'):
                xpos += 1
            elif keyboard.is_pressed('a'):
                xpos -= 1
            if keyboard.is_pressed('w'):
                ypos -= 1
            elif keyboard.is_pressed('s'):
                ypos += 1
            # bevegelse/key lytter


            # piksel(xpos+3, ypos, 'l')
            # piksel(xpos+3, ypos+2, 'g')
            #
            #FUNKER IKKE (ENDA)

            rader[ypos][xpos] =  (fargetpx)
            rader[ypos+1][xpos+1] = (fargetpx)

            
            for rad in rader:
                pikselString = ''
                for piksel in rad:
                    pikselString += piksel #lager en string av raden
                print(pikselString) # skriver ut stringen
                



            



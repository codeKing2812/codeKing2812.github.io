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



def tegn(x, y, farge):
    if farge == 'l':
        rader[y][x] =  (design.HEADER)
    elif farge == 'r':
        rader[y][x] =  (design.FAIL)
    elif farge == 'b':
        rader[y][x] =  (design.CYAN)
        
    rader[y][x] += ('O ' + design.END)



y1 = 0
y2 = 0
ball = {'x': 12, 'y': 7, 'xv': 0, 'yv': 0}

tid = time.time()
startTid = tid
while time.time() < startTid + 60:
    if time.time() > tid + 0.1: # kjør hvert tiendedels sekund

        os.system('cls')
        tid += 0.1 
        # refresh skjermen
        
        rader = []
        for i in range(15):
            rad = ['O ']*25
            rader.append(rad)
        # nullstill alle rader

        
        if keyboard.is_pressed('w'):
            y1 -= 1
        elif keyboard.is_pressed('s'):
            y1 += 1

        if keyboard.is_pressed('Up'):
            y2 -= 1
        elif keyboard.is_pressed('Down'):
            y2 += 1
        # bevegelse/key lytter


        tegn(ball['x'], ball['y'], 'r')

        tegn(1, y1, 'b')
        tegn(1, y1+1, 'b')
        tegn(1, y1+2, 'b')

        tegn(-2, y2, 'l')
        tegn(-2, y2+1, 'l')
        tegn(-2, y2+2, 'l')


        for rad in rader:
            pikselString = ''
            for piksel in rad:
                pikselString += piksel #lager en string av raden
            print(pikselString) # skriver ut stringen
            
print(design.FAIL + 'G A M E  O V E R' + design.END)


            
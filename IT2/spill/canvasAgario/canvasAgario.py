from tkinter import *
from math import sqrt
from PIL import ImageTk,Image 
from random import randint
import time
import keyboard
import os


#
########################################################## TKINTER SETUP ##################################################################################
#

canvasBredde = 800
canvasHøyde = 500


app = Tk()
app.geometry(f"{canvasBredde}x{canvasHøyde}")
c = Canvas(app, width=canvasBredde, height=canvasHøyde, background='beige')
c.pack()


#
########################################################## DEFINERING AV KLASSER ############################################################################
#


class Boks:
    def __init__(self, x, y, masse, bilde=None, bildeBredde=0, bildeHøyde=0, bildeKolonne=0, bildeRad=0, tags=[], state=NORMAL, respawn='på'):
        self.x = x
        self.y = y
        self.masse = masse

        self.bilde = Image.open(absRef(bilde))
        self.bildeBredde = bildeBredde
        self.bildeHøyde = bildeHøyde
        self.bildeKolonne = bildeKolonne
        self.bildeRad = bildeRad
        self.bildeTk = None
        self.tags = tags + ['boks']
        self.state = state
        self.respawn = respawn

        self.respawnFrame = 0

        self.oppdaterBilde()
        self.tegnBilde()

    @property
    def bredde(self):
        return (sqrt(self.masse))/2
    
    
    def oppdaterBilde(self, rad=None, kolonne=None, bredde=None, høyde=None):
        if rad:
            self.bildeRad = rad
        if kolonne:
            self.bildeKolonne = kolonne
        if bredde:
            self.bildeBredde = bredde
        if høyde:
            self.bildeHøyde = høyde
        
        self.bildeCrop = spritesheet(self.bilde, self.bildeBredde, self.bildeHøyde, self.bildeKolonne, self.bildeRad)


    def tegnBilde(self):
        self.bildeTk = ImageTk.PhotoImage(self.bildeCrop.resize((round(self.bredde*2), round(self.bredde*2))))
        c.create_image(self.x, self.y, image=self.bildeTk, state=self.state, tags=tuple(self.tags))
        app.update()


    def endreState(self, state):
        self.state = state
        self.tegnBilde()


    def oppdater(self):
        if self.respawn == 'aktiv' and not spillSlutt:
            global frameNr
            if frameNr > self.respawnFrame:
                self.x = randint(0,canvasBredde)
                self.y = randint(0,canvasHøyde)
                c.coords(self.tags[0], self.x, self.y)
                self.endreState(NORMAL)
                self.respawn = 'på'
                if 'bot' in self.tags:
                    self.masse = 500

    

    def dø(self):
        self.endreState(HIDDEN)

        if self.respawn == 'på':
            global frameNr
            self.respawnFrame = frameNr + randint(600, 1200)
            self.respawn = 'aktiv'


    def avstand(self, annen):
        if annen == self:
            return 1000000

        xAvstand = abs(self.x - annen.x)
        yAvstand = abs(self.y - annen.y)

        totalBredde = self.bredde + annen.bredde

        xAvstand -= totalBredde
        yAvstand -= totalBredde

        if xAvstand < 0:
            xAvstand = 0
        
        if yAvstand < 0:
            yAvstand = 0

        return xAvstand+yAvstand




class Spiller(Boks):
    def __init__(self, x, y, masse, bilde, bildeBredde, bildeHøyde, bildeKolonne, bildeRad, tags=[], state=NORMAL, respawn='av', xv=0, yv=0):
        super().__init__(x, y, masse, bilde, bildeBredde=bildeBredde, bildeHøyde=bildeHøyde, bildeKolonne=bildeKolonne, bildeRad=bildeRad, respawn=respawn, state=state, tags=tags+['spiller'])
        self.xv = xv
        self.yv = yv


    def oppdater(self):
        super().oppdater()

        if self.state == NORMAL:
            self.flytt()


    def holdPåKartet(self):   
        if self.x - self.bredde <= 0:
            self.xv = 1
        elif self.x + self.bredde >= canvasBredde:
            self.xv = -1

        if self.y - self.bredde<= 0:
            self.yv = 1
        elif self.y + self.bredde >= canvasHøyde:
            self.yv = -1
    

    def flytt(self): 

        self.xv = self.xv * 1.3*(self.masse)**-0.3
        self.yv = self.yv * 1.3*(self.masse)**-0.3

        self.holdPåKartet()

        self.x = self.x + self.xv
        self.y = self.y + self.yv
        
        c.coords(self.tags[0], self.x, self.y)
        self.tegnBilde()


    def spis(self, annen):
        if annen.state == self.state == NORMAL and self.masse > annen.masse:
            self.masse += annen.masse
            print(self.tags[0], self.masse)
            annen.dø()
            self.tegnBilde()



class Bot(Spiller):
    def __init__(self, x, y, masse, bilde, bildeBredde, bildeHøyde, bildeKolonne, bildeRad, tags=[], state=NORMAL, respawn='på', xv=0, yv=0):
        super().__init__(x, y, masse, bilde, bildeBredde=bildeBredde, bildeHøyde=bildeHøyde, bildeKolonne=bildeKolonne, bildeRad=bildeRad, state=state, respawn=respawn, xv=xv, yv=yv, tags=tags+['bot'])

 
    def jakt(self, alleMål, hovedMål):
        minsteAvstand = 100000
        mål = None

        
        for annen in hovedMål: # finn den nærmeste av hovedmålene
            avstand = self.avstand(annen)
            if avstand < minsteAvstand and annen.state == NORMAL:
                minsteAvstand = avstand
                mål = annen 

        if not mål or mål.masse >= self.masse : # hvis den ikke er spiselig
            minsteAvstand = 100000
            
            for annen in alleMål: #finn det nærmeste som er spiselig 
                avstand = self.avstand(annen)
                if avstand < minsteAvstand and annen.masse < self.masse and annen.state == NORMAL:
                    minsteAvstand = avstand
                    mål = annen

        if self.x < mål.x:
            self.xv = 3
            self.oppdaterBilde(kolonne=4)
        else :
            self.xv = -3
            self.oppdaterBilde(kolonne=3)
            
        if self.y < mål.y:
            self.yv = 3
            self.oppdaterBilde(kolonne=2)
        else :
            self.yv = -3
            self.oppdaterBilde(kolonne=1)


#
########################################################## DEFINERING AV FUNKSJONER ############################################################################
#


def absRef(relRef): # funksjon for å finne absolutt referanse til en fil fra relativ referanse
    return os.path.join(os.path.dirname(__file__), relRef)


spillSlutt = False
def gameOver():
    global spillSlutt, alleBokser

    if spillSlutt == False:
        for bokstav in gameOverBokstaver:
            bokstav.endreState(NORMAL) 
        spillSlutt = True
        alleBokser = gameOverBokstaver + spillerListe + matListe


def spritesheet(sheet, bredde, bildeHøyde, kolonne, rad):
    bilde = sheet.crop([kolonne*bredde, rad*bildeHøyde, kolonne*bredde+bredde, rad*bildeHøyde+bildeHøyde])
    return bilde


#
########################################################## OPPRETTING AV OBJEKTER ############################################################################
#


bot1 = Bot(randint(0, canvasBredde), randint(0, canvasHøyde), 500, 'bilder/spillere2.png', 320, 320, 0, 1, tags=['bot1'])
bot2 = Bot(randint(0, canvasBredde), randint(0, canvasHøyde), 500, 'bilder/spillere2.png', 320, 320, 0, 1, tags=['bot2'])
bot3 = Bot(randint(0, canvasBredde), randint(0, canvasHøyde), 500, 'bilder/spillere2.png', 320, 320, 0, 1, tags=['bot3'])
bot4 = Bot(randint(0, canvasBredde), randint(0, canvasHøyde), 500, 'bilder/spillere2.png', 320, 320, 0, 1, tags=['bot4'])

botListe = [bot1, bot2, bot3, bot4]

blå = Spiller(250, 250, 600, 'bilder/spillere2.png', 320, 320, 0, 0, tags=['blå'])

spillerListe = [blå] + botListe

matListe = []
for i in range(25):
    tag = 'mat' + str(i)
    mat = Boks(randint(0, canvasBredde),randint(0, canvasHøyde), 150, 'bilder/mat.png', 320, 320, 0, 0, tags=[tag, 'mat'])
    matListe.append(mat)

alleBokser = spillerListe + matListe 



gameOverBokstaver = []
for i in range(8):
    bokstavBoks = Boks((i+1)*55, 200, 2500, 'bilder/game_over2.png', 320, 320, 0, i, state=HIDDEN, respawn='av', tags=['gameoverBokstav'])
    gameOverBokstaver.append(bokstavBoks)



#
########################################################## GAMELOOP ############################################################################
#


def gameloop():
    global frameNr
    frameNr+=1 


    if blå.state != NORMAL:
        gameOver()
    elif all(bot.state != NORMAL for bot in botListe):
        gameOver()
    

    for spiller in spillerListe:
        for boks in alleBokser:
            if spiller.avstand(boks) == 0:
                spiller.spis(boks)


    for bot in botListe:
        bot.jakt(alleBokser, spillerListe)
        
    for boks in alleBokser:
        boks.oppdater()


    if keyboard.is_pressed('Right') or keyboard.is_pressed('d'):
        blå.xv = 3
        blå.oppdaterBilde(kolonne=4)
    elif keyboard.is_pressed('Left') or keyboard.is_pressed('a'):
        blå.xv = -3
        blå.oppdaterBilde(kolonne=3)
    else: blå.xv = 0

    if keyboard.is_pressed('Down') or keyboard.is_pressed('s'):
        blå.yv = 3
        blå.oppdaterBilde(kolonne=2)
    elif keyboard.is_pressed('Up') or keyboard.is_pressed('w'):
        blå.yv = -3
        blå.oppdaterBilde(kolonne=1)
        
    else: blå.yv = 0



frameNr = 0
spillLengde = 300
framerate = 1/60
tid = startTid = time.time()

while time.time() < startTid + spillLengde: # til tiden er ute
    if time.time() > tid: # kjør frame
        gameloop()
        tid += framerate 

        app.update()
        app.update_idletasks()

gameOver()
time.sleep(2)
         

print('fps:', frameNr/spillLengde)
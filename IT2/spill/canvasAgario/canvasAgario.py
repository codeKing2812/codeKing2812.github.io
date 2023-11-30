from tkinter import *
from math import sqrt
from PIL import ImageTk,Image 
from random import randint
import time
import keyboard
import os


#
########################################################## TKINTER SETUP ############################################################################
#


app = Tk()
app.geometry("500x500")
c = Canvas(app, width=500, height=500, background='beige')
c.pack()


#
########################################################## DEFINERING AV KLASSER ############################################################################
#


class Boks:
    def __init__(self, farge, x, y, masse, state=NORMAL, respawn='på', bilde=None, tags=[]):
        self.farge = farge
        self.x = x
        self.y = y
        self.masse = masse
        self.state = state
        self.respawn = respawn
        self.bilde = bilde
        self.bildeTk = None
        self.tags = tags + ['boks']
        self.startFrame = 0

        self.tegn()


    @property
    def bredde(self):
        return (sqrt(self.masse))/2


    def resizeBilde(self):
        self.bilde = self.bilde.resize((round(self.bredde*2), round(self.bredde*2)))
        self.bildeTk = ImageTk.PhotoImage(self.bilde)


    def tegn(self):
        if self.bilde:
            self.resizeBilde()
            c.create_image(self.x, self.y, image=self.bildeTk, state=self.state, tags=tuple(self.tags))
        else: 
            c.create_rectangle(self.x-self.bredde, self.y-self.bredde, self.x+self.bredde, self.y+self.bredde, fill=self.farge, state=self.state, tags=tuple(self.tags))
    

    def endreState(self, state):
        self.state = state
        c.itemconfig(self.tags[0], state=state)


    def oppdater(self):
        if self.respawn == 'aktiv':
            global frameNr
            if frameNr > self.startFrame + randint(600, 1200):
                if self.tags.index('mat') > 0:
                    c.coords(self.tags[0], randint(0, 500), randint(0, 500))
                self.endreState(NORMAL)
                self.respawn = 'på'
    

    def dø(self):
        self.endreState(HIDDEN)

        if self.respawn == 'på':
            global frameNr
            self.startFrame = frameNr
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
    def __init__(self, farge, x, y, masse, xv=0, yv=0, respawn='av', bilde=None, tags=[]): 
        super().__init__(farge, x, y, masse, respawn=respawn, bilde=bilde, tags=tags+['spiller'])
        self.xv = xv
        self.yv = yv


    def oppdater(self):
        super().oppdater()

        if self.state == NORMAL:
            self.flytt()


    def holdPåKartet(self):   
        if self.x <= 0:
            self.xv = 0.1
        elif self.x >= 500:
            self.xv = -0.1

        if self.y <= 0:
            self.yv = 0.1
        elif self.y >= 500:
            self.yv = -0.1
    

    def flytt(self):

        self.holdPåKartet()

        self.x = self.x + self.xv
        self.y = self.y + self.yv
        
        if self.bilde:
            # self.bilde.resize((round(self.bredde*2), round(self.bredde*2)))
            c.coords(self.tags[0], self.x, self.y)

        else: 
            c.coords(self.tags[0], self.x-self.bredde, self.y-self.bredde, self.x+self.bredde, self.y+self.bredde)
    

    def spis(self, annen):
        if annen.state == self.state == NORMAL and self.masse > annen.masse:
            self.masse += annen.masse
            annen.dø()

            # if self.bilde: # gjør bildet større siden massen er større
            #     self.bilde = ImageTk.PhotoImage(ImageTk.getimage(self.bilde).resize((round(self.bredde*2), round(self.bredde*2))))




class Bot(Spiller):
    def __init__(self, farge, x, y, masse, xv=0, yv=0, respawn='av', bilde=None, tags=[]):
        super().__init__(farge, x, y, masse, xv, yv, respawn, bilde=bilde, tags=tags+['bot'])

 
    def jakt(self, alleMål, hovedMål):
        minsteAvstand = 100000

        for annen in hovedMål: # finn den nærmeste av hovedmålene
            avstand = self.avstand(annen)
            if avstand < minsteAvstand and annen.state == NORMAL:
                minsteAvstand = avstand
                mål = annen 

        if mål.masse >= self.masse : # hvis den ikke er spiselig
            minsteAvstand = 100000
            for annen in alleMål: #finn det nærmeste som er spiselig 
                avstand = self.avstand(annen)
                if avstand < minsteAvstand and annen.masse < self.masse and annen.state == NORMAL:
                    minsteAvstand = avstand
                    mål = annen

        if self.x < mål.x:
            self.xv = 0.3
        else :
            self.xv = -0.3
            
        if self.y < mål.y:
            self.yv = 0.3
        else :
            self.yv = -0.3


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


def spritesheet(sheetRef, bildeBredde, bildeHøyde, bildeNr, bildeRad):
    sheet = Image.open(absRef(sheetRef))
    bilde = sheet.crop([bildeNr*bildeBredde, bildeRad*bildeHøyde, bildeNr*bildeBredde+bildeBredde, bildeRad*bildeHøyde+bildeHøyde])
    return bilde


#
########################################################## OPPRETTING AV OBJEKTER ############################################################################
#


bot1 = Bot('red', randint(0, 500), 100, 500, tags=['bot1'])
bot2 = Bot('red', randint(0, 500), 200, 500, tags=['bot2'])
bot3 = Bot('red', randint(0, 500), 300, 500, tags=['bot3'])
bot4 = Bot('red', randint(0, 500), 400, 500, tags=['bot4'])

botListe = [bot1, bot2, bot3, bot4]

blå = Spiller(None, 250, 250, 500, bilde=spritesheet('bilder/spillere2.png', 320, 320, 0, 0), tags=['blå'])

spillerListe = [blå] + botListe

matListe = []
for i in range(25):
    tag = 'mat' + str(i)
    mat = Boks('green', randint(0, 500), randint(0, 500), 25, tags=[tag, 'mat'])
    matListe.append(mat)

alleBokser = spillerListe + matListe 



gameOverBokstaver = []
for i in range(8):
    bokstavBoks = Boks(None, (i+1)*55, 200, 2500, state=HIDDEN, respawn='av', bilde=spritesheet('bilder/game_over2.png', 320, 320, 0, i), tags=['gameoverBokstaver'])
    gameOverBokstaver.append(bokstavBoks)



#
########################################################## GAMELOOP ############################################################################
#


def gameloop(): 
    global frameNr

    for spiller in spillerListe:
        for boks in alleBokser:
            if spiller.avstand(boks) == 0:
                spiller.spis(boks)


    for bot in botListe:
        bot.jakt(alleBokser, spillerListe)
        
    for boks in alleBokser:
        boks.oppdater()


    if keyboard.is_pressed('Right'):
        blå.xv = 0.5
    elif keyboard.is_pressed('Left'):
        blå.xv = -0.5
    else: blå.xv = 0

    if keyboard.is_pressed('Down'):
        blå.yv = 0.5
    elif keyboard.is_pressed('Up'):
        blå.yv = -0.5
    else: blå.yv = 0


    if blå.state != NORMAL:
        gameOver()
    elif all(bot.state != NORMAL for bot in botListe):
        gameOver()

    frameNr+=1


frameNr = 0
spillLengde = 90
framerate = 1/60
tid = startTid = time.time()

while tid < startTid + spillLengde: # til tiden er ute
    if time.time() > tid: # kjør frame
        gameloop()
        tid += framerate 

        app.update_idletasks()
        app.update()

gameOver()
         

print('fps:', frameNr/spillLengde)
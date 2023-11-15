from tkinter import *
from math import sqrt
import random 
import time
import keyboard


# NIO: k3mscqfx

app = Tk()
app.geometry("500x500")
c = Canvas(app, width=500, height=500, background='beige')
c.pack()


class Boks:
    def __init__(self, farge, x, y, masse, state=NORMAL):
        self.farge = farge
        self.x = x
        self.y = y
        self.masse = masse
        self.state = state
        self.respawn = 'på'
        self.startFrame = 0

    @property
    def bredde(self):
        return (sqrt(self.masse))/2
    
    def tegn(self):
        self.id = c.create_rectangle(self.x-self.bredde, self.y-self.bredde, self.x+self.bredde, self.y+self.bredde, fill=self.farge, state=self.state)
    
    def endreState(self, state):
        # print(state)
        self.state = state
        c.itemconfigure(self.id, state=state)

    def oppdater(self):
        if self.respawn == 'aktiv':
            global frameNr
            if frameNr > self.startFrame + random.randint(360, 1080):
                self.endreState(NORMAL)
                self.respawn = 'på'
    
    def slett(self):
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
    def __init__(self, farge, x, y, masse, xv=0, yv=0): 
        super().__init__(farge, x, y, masse)
        self.xv = xv
        self.yv = yv

        self.respawn = 'av'

        self.tegn()

    def oppdater(self):
        self.flytt()

        if self.respawn == 'aktiv':
            global frameNr
            if frameNr > self.startFrame + random.randint(60, 600):
                self.endreState(NORMAL)

    def flytt(self):

        self.x = self.x + self.xv
        self.y = self.y + self.yv
        
        c.coords(self.id, self.x-self.bredde, self.y-self.bredde, self.x+self.bredde, self.y+self.bredde)
    
    def spis(self, annen):
        if annen.state == self.state == NORMAL and self.masse > annen.masse:
            self.masse += annen.masse
            annen.slett()



class Bot(Spiller):
    def __init__(self, farge, x, y, masse, xv=0, yv=0):
        super().__init__(farge, x, y, masse, xv, yv)

    def jakt(self, alleMål, hovedMål):
        minsteAvstand = 100000

        for annen in hovedMål: # finn den nærmeste av hovedmålene
            avstand = self.avstand(annen)
            if avstand < minsteAvstand and annen.state == NORMAL:
                minsteAvstand = avstand
                mål = annen 

        if annen.masse > self.masse : # hvis den ikke er spiselig
            for annen in alleMål: #finn det nærmeste som er spiselig 
                avstand = self.avstand(annen)
                if avstand < minsteAvstand and annen.masse < self.masse and annen.state == NORMAL:
                    minsteAvstand = avstand
                    mål = annen

        if self.x < mål.x:
            self.xv = 0.15
        else :
            self.xv = -0.15
            
        if self.y < mål.y:
            self.yv = 0.15
        else :
            self.yv = -0.15



bot1 = Bot('red', 60, 100, 450)
bot2 = Bot('red', 470, 130, 450)
bot3 = Bot('red', 390, 480, 450)
bot4 = Bot('red', 200, 360, 450)

botListe = [bot1, bot2, bot3, bot4]

blå = Spiller('blue', 50, 200, 400)

spillerListe = [blå] + botListe


matListe = []
for y in range(5):
    for x in range(5):
        mat = Boks('green', 100*x+50, 100*y+50, 20)
        matListe.append(mat)
        mat.tegn()

alleBokser = spillerListe + matListe

frameNr = 0
def gameloop() :
    global frameNr

    for spiller in spillerListe:
        for mat in matListe:
            if spiller.avstand(mat) == 0:
                spiller.spis(mat)
        
        for bot in botListe:
            if spiller.avstand(bot) == 0:
                spiller.spis(bot)
                bot.spis(spiller)


        
    for bot in botListe:
        bot.jakt(alleBokser, spillerListe)

    for boks in alleBokser:
        boks.oppdater()


    if keyboard.is_pressed('Right'):
        blå.xv = 0.2
        blå.flytt()
    elif keyboard.is_pressed('Left'):
        blå.xv = -0.2
        blå.flytt()
    else: blå.xv = 0

    if keyboard.is_pressed('Down'):
        blå.yv = 0.2
        blå.flytt()
    elif keyboard.is_pressed('Up'):
        blå.yv = -0.2
        blå.flytt()
    else: blå.yv = 0

    

    app.update_idletasks()
    app.update()

    frameNr+=1



spillLengde = 45
framerate = 1/60
tid = startTid = time.time()

while tid < startTid + spillLengde: # til tiden er ute
    if time.time() > tid: # kjør frame
        gameloop()
        tid += framerate 
         

print('fps:', frameNr/spillLengde)
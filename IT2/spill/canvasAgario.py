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
    def __init__(self, farge, x, y, masse, state=NORMAL, respawn='på'):
        self.farge = farge
        self.x = x
        self.y = y
        self.masse = masse
        self.state = state
        self.respawn = respawn
        self.startFrame = 0


    @property
    def bredde(self):
        return (sqrt(self.masse))/2
    

    def tegn(self):
        self.id = c.create_rectangle(self.x-self.bredde, self.y-self.bredde, self.x+self.bredde, self.y+self.bredde, fill=self.farge, state=self.state)
    

    def endreState(self, state):
        self.state = state
        c.itemconfigure(self.id, state=state)


    def oppdater(self):
        if self.respawn == 'aktiv':
            global frameNr
            if frameNr > self.startFrame + random.randint(360, 1080):
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
    def __init__(self, farge, x, y, masse, xv=0, yv=0, respawn='av'): 
        super().__init__(farge, x, y, masse, respawn=respawn)
        self.xv = xv
        self.yv = yv

        self.tegn()


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
        
        c.coords(self.id, self.x-self.bredde, self.y-self.bredde, self.x+self.bredde, self.y+self.bredde)
    

    def spis(self, annen):
        if annen.state == self.state == NORMAL and self.masse > annen.masse:
            self.masse += annen.masse
            annen.dø()



class Bot(Spiller):
    def __init__(self, farge, x, y, masse, xv=0, yv=0, respawn='av'):
        super().__init__(farge, x, y, masse, xv, yv, respawn)


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



bot1 = Bot('red', random.randint(0, 500), 100, 500)
bot2 = Bot('red', random.randint(0, 500), 200, 500)
bot3 = Bot('red', random.randint(0, 500), 300, 500)
bot4 = Bot('red', random.randint(0, 500), 400, 500)

botListe = [bot1, bot2, bot3, bot4]

blå = Spiller('blue', 50, 200, 500)

spillerListe = [blå] + botListe

matListe = []
for y in range(5):
    for x in range(5):
        mat = Boks('green', 100*x+50, 100*y+50, 20)
        matListe.append(mat)
        mat.tegn()

alleBokser = spillerListe + matListe


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
        blå.xv = 0.5
    elif keyboard.is_pressed('Left'):
        blå.xv = -0.5
    else: blå.xv = 0

    if keyboard.is_pressed('Down'):
        blå.yv = 0.5
    elif keyboard.is_pressed('Up'):
        blå.yv = -0.5
    else: blå.yv = 0

    frameNr+=1


frameNr = 0
spillLengde = 30
framerate = 1/60
tid = startTid = time.time()

while tid < startTid + spillLengde: # til tiden er ute
    if time.time() > tid: # kjør frame
        gameloop()
        tid += framerate 

        app.update_idletasks()
        app.update()
         

print('fps:', frameNr/spillLengde)
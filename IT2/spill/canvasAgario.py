from tkinter import *
from math import *
import keyboard


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

    @property
    def bredde(self):
        return (sqrt(self.masse))/2

    def hentForm(self):
        self.id = c.create_rectangle(self.x-self.bredde, self.y-self.bredde, self.x+self.bredde, self.y+self.bredde, fill=self.farge, state=self.state)
    
    def er_over(self, annen):
        avstandX = abs(self.x - annen.x)
        avstandY = abs(self.y - annen.y)

        totalBredde = self.bredde + annen.bredde
        
        if avstandX < totalBredde and avstandY < totalBredde:
            return True

        # if self.x + 10 > annen.x and self.x < annen.x + 10 and self.y + 10 > annen.y and self.y < annen.y + 10:
        #     return True
        
    def slett(self):
        self.state = DISABLED
        c.delete(self.id)
        
        


class Spiller(Boks):
    def __init__(self, farge, x, y, masse, xv=0, yv=0): 
        super().__init__(farge, x, y, masse)
        self.xv = xv
        self.yv = yv

        self.hentForm()


    def flytt(self):

        self.x = self.x + self.xv
        self.y = self.y + self.yv
        
        c.coords(self.id, self.x-self.bredde, self.y-self.bredde, self.x+self.bredde, self.y+self.bredde)


    def tp(self, x, y):
        c.coords(self.id, x, y, self.x+self.bredde, self.y+self.bredde)
    
    def spis(self, annen):
        if annen.state == self.state == NORMAL and self.masse > annen.masse*1.05:
            self.masse += annen.masse
            annen.slett()



class Bot(Spiller):
    def __init__(self, farge, x, y, masse, xv=0, yv=0):
        super().__init__(farge, x, y, masse, xv, yv)

    def jakt(self, annen):
        if self.x < annen.x:
            self.xv = 0.05
        else :
            self.xv = -0.05
            
        if self.y < annen.y:
            self.yv = 0.05
        else :
            self.yv = -0.05


bot1 = Bot('red', 60, 100, 450)
bot2 = Bot('red', 470, 130, 450)
bot3 = Bot('red', 390, 480, 450)
bot4 = Bot('red', 200, 360, 450)

botListe = [bot1, bot2, bot3, bot4]

blå = Spiller('blue', 50, 200, 400)

spillerListe = [blå,] + botListe

print(spillerListe)


matListe = []
for y in range(5):
    for x in range(5):
        mat = Boks('green', 100*x+50, 100*y+50, 20)
        matListe.append(mat)
        mat.hentForm()



while True: # gameloop

    for spiller in spillerListe:
        for mat in matListe:
            if spiller.er_over(mat):
                spiller.spis(mat)
        
        for bot in botListe:
            if spiller.er_over(bot):
                spiller.spis(bot)
                bot.spis(spiller)


        
    for bot in botListe:
        bot.jakt(blå)
        bot.flytt()
    


    if keyboard.is_pressed('Right'):
        blå.xv = 0.1
        blå.flytt()
    elif keyboard.is_pressed('Left'):
        blå.xv = -0.1
        blå.flytt()
    else: blå.xv = 0

    if keyboard.is_pressed('Down'):
        blå.yv = 0.1
        blå.flytt()
    elif keyboard.is_pressed('Up'):
        blå.yv = -0.1
        blå.flytt()
    else: blå.yv = 0

    

    app.update_idletasks()
    app.update()


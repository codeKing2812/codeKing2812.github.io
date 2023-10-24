from tkinter import *
import keyboard

app = Tk()
app.geometry("500x500")
c = Canvas(app, width=500, height=500, background='beige')
c.pack()


class kule:
    def __init__(self, farge, x, y, masse):
        self.farge = farge
        self.x = x
        self.y = y
        self.masse = masse
    
    def tegn(self):
        self.id = c.create_oval(self.x, self.y, self.x+self.masse, self.y+self.masse, fill=self.farge)
    
    def er_over(self, annen):
        if self.x + self.masse > annen.x and self.x < annen.x + annen.masse and self.y + self.masse > annen.y and self.y < annen.y + annen.masse:
            return True


class spiller(kule):
    def __init__(self, farge, x, y, xv, yv, masse): 
        super().__init__(farge, x, y, masse)
        self.xv = xv
        self.yv = yv

        self.tegn()

    def flytt(self):

        self.x = self.x + self.xv
        self.y = self.y + self.yv
        
        c.move(self.id, self.xv, self.yv)
    


blå = spiller('blue', 50, 200, 0, 0, 50)
rød = spiller('red', 400, 250, 0, 0, 50)

matListe = []
# for y in range(5):
#     for x in range(5):
#         mat = kule('green', 100*x+50, 100*y+50, 10)
#         matListe.append(mat)

while True: # gameloop

    if blå.er_over(rød) :
        print('er over')

    # for mat in matListe:
    #     print(len(matListe))
    #     if not mat.er_over(blå) :
    #         matListe.remove(mat)
    #     mat.tegn()

    if keyboard.is_pressed('Right'):
        blå.xv = 0.1
    elif keyboard.is_pressed('Left'):
        blå.xv = -0.1
    else: blå.xv = 0


    if keyboard.is_pressed('Down'):
        blå.yv = 0.1
    elif keyboard.is_pressed('Up'):
        blå.yv = -0.1
    else: blå.yv = 0

    if rød.x < blå.x :
        rød.xv = 0.05
    else :
        rød.xv = -0.05
        
    if rød.y < blå.y :
        rød.yv = 0.05
    else :
        rød.yv = -0.05

    
    blå.flytt()
    rød.flytt()
    app.update_idletasks()
    app.update()

from tkinter import *
from PIL import Image, ImageTk
import os
import time

win=Tk()
win.geometry("400x1000")


def absRef(relRef): # funksjon for å finne absolutt referanse til en fil fra relativ referanse
    return os.path.join(os.path.dirname(__file__), relRef)


class Objekt:
    def __init__(self, bilde):
        self.bilde = bilde
        self.bildeTk = None

    def visbilde(self, size):
        
        self.bildeTk = ImageTk.PhotoImage(self.bilde.resize((size, size)))

        label=Label(win, image=self.bildeTk)
        label.pack()

        win.update()


objekt1 = Objekt(Image.open(absRef('bilder/spillere2.png')))
objekt2 = Objekt(Image.open(absRef('bilder/spillere2.png')))
objekt3 = Objekt(Image.open(absRef('bilder/game_over2.png')))


while True:
    objekt1.visbilde(50)
    time.sleep(1)
    
    objekt1.visbilde(30)
    time.sleep(1)

    # win.update()
    win.update_idletasks()
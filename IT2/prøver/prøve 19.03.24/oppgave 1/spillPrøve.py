import pygame as pg
import sys
from random import randint
from math import sqrt


# definerer noen variabler før oprettelsen av klasser
skjermBredde = 600
skjermHøyde = 500

ondListe = []

class Player:
    def __init__(self, x, y, fart, radius, farge):
        self.x = x
        self.y = y
        self.fart = fart
        self.radius = radius
        self.farge = farge
        self.sistAngrep = 0
        self.klarTilAngrep = False
        self.nå = pg.time.get_ticks()

    def update(self):
        self.keyLytter(pg.key.get_pressed())
        self.holdPåKartet()
        self.cooldown()
        self.kræsj(ondListe)


    def tegn(self, screen):
        pg.draw.circle(screen, self.farge, (self.x, self.y), self.radius)


    def holdPåKartet(self):   
        if self.x - self.radius <= 0:
            self.x += self.fart
        elif self.x + self.radius >= skjermBredde:
            self.x -= self.fart

        if self.y - self.radius<= 0:
            self.y += self.fart
        elif self.y + self.radius >= skjermHøyde:
            self.y -= self.fart


    def keyLytter(self, key):
        if key[pg.K_w]:
            self.y -= self.fart
        if key[pg.K_s]:
            self.y += self.fart
        if key[pg.K_a]:
            self.x -= self.fart
        if key[pg.K_d]:
            self.x += self.fart
        
        if key[pg.K_SPACE]:
            global ondListe
            self.angrip(ondListe)
    
    def cooldown(self):
        self.nå = pg.time.get_ticks()
        if self.nå - self.sistAngrep > 15000:
            self.klarTilAngrep = True
            self.farge = 'green'


    def angrip(self, offerListe):
        if self.klarTilAngrep:
            self.sistAngrep = self.nå # reset cooldown
            self.farge = 'white'

            for annen in offerListe:
                xAvstand = abs(self.x - annen.x)
                yAvstand = abs(self.y - annen.y)
                totAvstand = sqrt(xAvstand**2 + yAvstand**2) # pytagoras for å finne total avstand

                if totAvstand < 50:
                    annen.dø(offerListe)
    
    def kræsj(self, liste):
        for annen in liste:
                xAvstand = abs(self.x - annen.x)
                yAvstand = abs(self.y - annen.y)
                totAvstand = sqrt(xAvstand**2 + yAvstand**2) # pytagoras for å finne total avstand

                if totAvstand < self.radius + annen.radius:
                    print('G A M E   O V E R')
                    pg.quit()
                    sys.exit()



class Ond(Player):
    def __init__(self, x, y, fart, radius):
        super().__init__(x, y, fart, radius, 'red')
    
    def dø(self, liste):
        liste.remove(self)

    def jakt(self, annen):

        if self.x < annen.x:
            self.x += self.fart
        else :
            self.x -= self.fart
            
        if self.y < annen.y:
            self.y += self.fart
        else :
            self.y -= self.fart


def main():

    pg.init()
    screen = pg.display.set_mode((skjermBredde, skjermHøyde))
    clock = pg.time.Clock()

    spiller = Player(300, 250, 4, 15, 'white')

    sisteSpawn = pg.time.get_ticks()
    ond = Ond(100, 100, 2, 10)
    ondListe.append(ond)

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

        ondRad = 10
        nå = pg.time.get_ticks()
        if nå - sisteSpawn > 10000:
            ondRad += 5
            ond = Ond(randint(0, skjermBredde), randint(0, skjermHøyde), 2, ondRad)
            ondListe.append(ond)
            sisteSpawn = nå

        screen.fill((0, 0, 0))

        spiller.update()
        spiller.tegn(screen)
        
        for ond in ondListe:
            ond.holdPåKartet()
            ond.jakt(spiller)
            ond.tegn(screen)


        pg.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
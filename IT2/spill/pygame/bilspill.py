import pygame as pg
from pygame.locals import *
import time
import os


######################### funksjoner ###################################

def absRef(relRef): # funksjon for å finne absolutt referanse til en fil fra relativ referanse
    return os.path.join(os.path.dirname(__file__), relRef)


def spritesheet(sheet, sheetBredde, sheetHøyde, kolonne, rad):    
    bilde = pg.Surface((sheetBredde, sheetHøyde), pg.SRCALPHA)
    bilde.blit(sheet, (0, 0), (kolonne*sheetBredde, rad*sheetHøyde, kolonne*sheetBredde+sheetBredde, rad*sheetHøyde+sheetHøyde))
    return bilde

def spritesheetTilListe(sheetRef, bredde, høyde, antall, skalar):
    sheet = pg.image.load(sheetRef)
    tempListe = []
    for i in range(antall):
        bilde = spritesheet(sheet, bredde, høyde, 0, i)
        bilde = pg.transform.scale_by(bilde, skalar)
        tempListe.append(bilde)

    return tempListe


######################### pygame setup ###################################


pg.init()

# Angir hvilken skrifttype og tekststørrelse vi vil bruke på tekst
font = pg.font.Font(absRef('fonter/ka1.ttf'), 24)

# Oppretter et vindu
vinduBredde = 700
vinduHøyde  = 700
vindu = pg.display.set_mode([vinduBredde, vinduHøyde])


######################### definering av klasser ###################################




class Sprite(pg.sprite.Sprite):
    def __init__(self, bildeListe, bildeNr, x, y, posisjon, skalar=1, synlig=True):
        pg.sprite.Sprite.__init__(self)
        
        self.bildeListe = bildeListe
        self.bildeNr = bildeNr
        self.x = x
        self.y = y
        self.posisjon = posisjon
        self.skalar = skalar
        self.synlig = synlig
        self.xv = 0
        self.yv = 0

        self.bilde = bildeListe[bildeNr]
        self.originalBilde = self.bilde


    @property
    def bredde(self):
        return self.skalar*self.originalBilde.get_width()
    
    @property
    def høyde(self):
        return self.skalar*self.originalBilde.get_height()
        

    def update(self):
        self.originalBilde = self.bildeListe[self.bildeNr]

        self.spesifikOppdater()

        self.x += self.xv
        self.y += self.yv

        self.rect = self.bilde.get_rect(center=(self.x, self.y))

        if self.synlig:
            vindu.blit(self.bilde, self.rect)


    def animer(self, msPerFrame, startFrame=0, sluttFrame=None):
        if not sluttFrame:
            sluttFrame=len(self.bildeListe)-1

        global tid
        print(tid, msPerFrame)
        self.frameNr = startFrame + (tid // msPerFrame) #% (sluttFrame - startFrame)
        print(self.frameNr)


        

class Hindring(Sprite):
    def __init__(self, bildeListe, bildeNr, x, y, fart, posisjon, skalar, synlig=False):
        super().__init__(bildeListe, bildeNr, x, y, posisjon, skalar, synlig)

        self.orginal_x = x
        self.orginal_y = y
        self.fart = fart
    

    def spesifikOppdater(self):
        if f40.posisjon + 10 > self.posisjon:
            self.komIMot()


    def komIMot(self):
        if self.y > vinduHøyde or self.x + self.bredde < 0 or self.x > vinduBredde:
            # hvis utenfor
            self.xv = 0
            self.yv = 0
            self.synlig = False

        else: # hvis den er på skjermen
            self.synlig = True

            self.yv = f40.fart/50
            if self.x < vinduBredde/2:
                self.xv = - self.yv*3.5
            else:
                self.xv = self.yv*3.5
            
            self.skalar += f40.fart*0.0004
            self.bilde = pg.transform.scale_by(self.originalBilde, self.skalar)
               



class Bil(Sprite):
    def __init__(self, bildeListe, bildeNr, x, y, fart):
        super().__init__(bildeListe, bildeNr, x, y, 0)

        self.fart = fart


    def spesifikOppdater(self):
        global målPosisjon

        self.posisjon += self.fart/fps

        if self.posisjon >= målPosisjon:
            self.gameOver()
    

    def gameOver(self):
        global PAUSE
        PAUSE = True


    def oppdaterVeifart(self, fartsendring):
        global veifart
        if veifart > 30 and veifart < 185:
            self.fart += fartsendring
            veifart = 200-self.fart
 
            if fartsendring > 0:
                self.skalar -= 0.007
                self.y -= 2
            else:
                self.skalar += 0.007
                self.y += 2
        
            self.bilde = pg.transform.scale_by(self.originalBilde, self.skalar)



######################### oprettelse av objekter ###################################


bgListe = spritesheetTilListe(absRef('bilder/veiBred.png'), 140, 140, 3, 5)
bakgrunn = Sprite(bgListe, 0, vinduBredde/2, vinduHøyde/2, 0)


bilBilde = spritesheetTilListe(absRef('bilder/f40.png'), 32, 32, 1, 8)
f40 = Bil(bilBilde, 0, bakgrunn.x, 550, 100)


kaktusBilde = spritesheetTilListe(absRef('bilder/kaktus2.png'), 16, 24, 2, 3)
kaktuser = pg.sprite.Group()
for i in range(10):
    if i//2 == i/2:
        nr = 0
    else: 
        nr = 1
    kaktuser.add(Hindring(kaktusBilde, nr, 300, 300, 0, 600*i, 0.1))
    

buskBilde = spritesheetTilListe(absRef('bilder/busk.png'), 16, 16, 1, 3)
busker = pg.sprite.Group()
for i in range(20):
    busker.add(Hindring(buskBilde, 0, 500, 300, 0, 400*i+100, 0.1))


######################### gameloop ###################################


clock = pg.time.Clock()
fps = 60
PAUSE = False
spillSlutt = False

målPosisjon = 3000
veifart = 100

OPPDATERBG = pg.USEREVENT + 1
pg.time.set_timer(OPPDATERBG, veifart)

while not spillSlutt and not PAUSE: 
    tid = pg.time.get_ticks()

    for event in pg.event.get():

        # slutt spillet hvis vinduet lukkes
        if event.type == pg.QUIT:
            spillSlutt = True


    # knappetrykk
    trykkedeTaster = pg.key.get_pressed()

    if trykkedeTaster[K_UP]:
        f40.oppdaterVeifart(1)
    if trykkedeTaster[K_DOWN]:
        f40.oppdaterVeifart(-1)
    
    
    if trykkedeTaster[K_LEFT] and trykkedeTaster[K_RIGHT]:
        f40.xv = 0
    elif trykkedeTaster[K_LEFT]:
        f40.xv = -5
    elif trykkedeTaster[K_RIGHT]:
        f40.xv = 5
    else: f40.xv = 0
        
    if trykkedeTaster[K_SPACE]:
        PAUSE = not PAUSE


    fartTekst = font.render(str(f40.fart) + ' kmt', True, (0,0,0), None)
    posisjonTekst = font.render(str(round(f40.posisjon)) + ' m', True, (0,0,0), None)

    # print(veifart)
    bakgrunn.animer(veifart)
    vindu.blit(bgListe[bakgrunn.bildeNr], (0,0))

    vindu.blit(fartTekst, (10, 10))
    vindu.blit(posisjonTekst, (10, 40))

    kaktuser.update()
    busker.update()
    f40.update()
        

    pg.display.flip()
    clock.tick(fps)


pg.quit()
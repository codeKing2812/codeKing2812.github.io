import pygame as pg
from pygame.locals import *
import random
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
pg.display.set_caption('RETRO RACER')


######################### musikk og lyder ###################################


pg.mixer.music.load(absRef('lyd/theme.mp3'))
pg.mixer.music.set_volume(0.3)
pg.mixer.music.play()

skrens = pg.mixer.Sound(absRef('lyd/skrens.mp3'))
skrens.set_volume(0.5)


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

        self.rect = self.bilde.get_rect(center=(self.x, self.y))
        self.kræsjRect = (self.rect.w, self.rect.h/2)


    @property
    def bredde(self):
        return self.skalar*self.originalBilde.get_width()
    
    @property
    def høyde(self):
        return self.skalar*self.originalBilde.get_height()
        

    def update(self):
        self.originalBilde = self.bildeListe[self.bildeNr]

        try:
            self.spesifikOppdater()
        except:
            None

        self.x += self.xv
        self.y += self.yv

        self.rect = self.bilde.get_rect(center=(self.x, self.y))
        self.kræsjRect = (self.rect.w, self.rect.h/2)

        if self.synlig:
            vindu.blit(self.bilde, self.rect)


    def animer(self, msPerBilde, startBilde=0, sluttBilde=None):
        if not sluttBilde:
            sluttBilde=len(self.bildeListe)-1

        global tid
        self.bildeNr = startBilde + (tid // msPerBilde) % (sluttBilde + 1 - startBilde)
        self.bilde = self.bildeListe[self.bildeNr]



        

class Hindring(Sprite):
    def __init__(self, bildeListe, bildeNr, x, y, fart, posisjon, skalar, synlig=False):
        super().__init__(bildeListe, bildeNr, x, y, posisjon, skalar, synlig)

        self.orginal_x = x
        self.orginal_y = y
        self.avstandFraSenter = self.orginal_x - vinduBredde/2
        print(self.avstandFraSenter)

        self.fart = fart
    

    def spesifikOppdater(self):
        if self.kræsjRect.colliderect(f40.kræsjRect) and self.synlig:
            f40.kræsj()

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

            self.xv = self.avstandFraSenter/100 * self.yv*3.5 
            
            self.skalar += f40.fart*0.0004
            self.bilde = pg.transform.scale_by(self.originalBilde, self.skalar)
               



class Bil(Sprite):
    def __init__(self, bildeListe, bildeNr, x, y, fart):
        super().__init__(bildeListe, bildeNr, x, y, 0)
        self.kræsjer = False
        self.fart = fart


    def spesifikOppdater(self):
        global målPosisjon

        self.posisjon += self.fart/fps

        if self.posisjon >= målPosisjon:
            global IMÅL
            IMÅL = True
        
        if self.kræsjer:
            if self.fart > 10:
                self.oppdaterVeifart(-5)
            else: 
                self.oppdaterVeifart(-self.fart)
                self.kræsjer = False
            
    
    def kræsj(self):
        pg.mixer.Channel(0).play(skrens)
        self.kræsjer = True

        

    def oppdaterVeifart(self, fartsendring):
        global veifart
        if self.fart > 5 and self.fart < 180:
            self.fart += fartsendring

            # veifart = 200-self.fart
            veifart = int(323*0.99**self.fart)
 
            self.skalar += 0.007*-fartsendring
            self.y += 2*-fartsendring
             

        elif self.fart <= 5 and fartsendring > 0:
            self.fart += fartsendring

            veifart = int(323*0.99**self.fart)
 
            self.skalar += 0.007*-fartsendring
            self.y += 2*-fartsendring
        
        elif self.fart >= 180 and fartsendring < 0:
            self.fart += fartsendring

            veifart = int(323*0.99**self.fart)
 
            self.skalar += 0.007*-fartsendring
            self.y += 2*-fartsendring

        if self.fart == 0:
            veifart = 10000000000

        self.bilde = pg.transform.scale_by(self.originalBilde, self.skalar)



######################### oprettelse av objekter ###################################


bgListe = spritesheetTilListe(absRef('bilder/veiBred.png'), 140, 140, 3, 5)
bakgrunn = Sprite(bgListe, 0, vinduBredde/2, vinduHøyde/2, 0)


bilBilde = spritesheetTilListe(absRef('bilder/f40.png'), 32, 32, 1, 8)
f40 = Bil(bilBilde, 0, bakgrunn.x, 550, 100)


kaktusBilder = spritesheetTilListe(absRef('bilder/kaktus.png'), 16, 24, 2, 3)
kaktuser = pg.sprite.Group()
for i in range(10):
    if i//2 == i/2:
        nr = 0
    else: 
        nr = 1
    kaktuser.add(Hindring(kaktusBilder, nr, 250, 300, 0, 600*i, 0.1))


buskBilde = spritesheetTilListe(absRef('bilder/busk.png'), 16, 16, 1, 3)
busker = pg.sprite.Group()
for i in range(20):
    busker.add(Hindring(buskBilde, 0, 450, 300, 0, 400*i+100, 0.1))

sperringBilder = spritesheetTilListe(absRef('bilder/sperring.png'), 16, 16, 3, 3)
sperringer = pg.sprite.Group()
for i in range(20):
    sperringer.add(Hindring(sperringBilder, 0, random.randint(300, 400), 300, 0, 500*i+200, 0.1))

######################### gameloop ###################################


clock = pg.time.Clock()
fps = 60
PAUSE = False
IMÅL = False
spillSlutt = False


målPosisjon = 10000
veifart = 100

while not spillSlutt:
    tid = pg.time.get_ticks()

    for event in pg.event.get():
            # slutt spillet hvis vinduet lukkes
            if event.type == pg.QUIT:
                spillSlutt = True

            # pause eller omstart på mellomrom
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:

                    if IMÅL:
                        IMÅL = False
                        PAUSE = False
                        f40.posisjon = 0
                        f40.oppdaterVeifart(100-f40.fart)
                        pg.mixer.music.play()


                    elif PAUSE:
                        PAUSE = False
                        pg.mixer.music.set_volume(0.3)

                    else:
                        PAUSE = True
                
            


    if PAUSE:
        pg.mixer.music.set_volume(0.1)

        pauseTekst1 = font.render('pause', True, (0,0,0), None)
        pauseTekst2 = font.render('trykk space for mer action', True, (0,0,0), None)
        vindu.blit(pauseTekst1, pauseTekst1.get_rect(center=(bakgrunn.x, 200)))
        vindu.blit(pauseTekst2, pauseTekst2.get_rect(center=(bakgrunn.x, 250)))


    elif IMÅL:
        målTekst = font.render('du er fremme! trykk space for omstart', True, (0,0,0), None)
        vindu.blit(målTekst, målTekst.get_rect(center=(bakgrunn.x, 300)))



    else:  
        # knappetrykk
        trykkedeTaster = pg.key.get_pressed()

        if trykkedeTaster[K_UP]:
            f40.oppdaterVeifart(1)
        if trykkedeTaster[K_DOWN]:
            f40.oppdaterVeifart(-1)
        
        
        if trykkedeTaster[K_LEFT] and trykkedeTaster[K_RIGHT]:
            f40.xv = 0
        elif trykkedeTaster[K_LEFT] and f40.x > 0 and f40.fart > 0:
            f40.xv = -5
        elif trykkedeTaster[K_RIGHT] and f40.x < vinduBredde and f40.fart > 0:
            f40.xv = 5
        else: f40.xv = 0
            

        
        # print(veifart)
        bakgrunn.animer(veifart)
        bakgrunn.update()

        fartTekst = font.render(str(f40.fart) + ' kmt', True, (0,0,0), None)
        posisjonTekst = font.render(str(round(f40.posisjon)) + ' m', True, (0,0,0), None)
        vindu.blit(fartTekst, (10, 10))
        vindu.blit(posisjonTekst, (10, 40))

        kaktuser.update()
        busker.update()
        sperringer.update()
        f40.update()
            


    pg.display.flip()
    clock.tick(fps)


pg.quit()
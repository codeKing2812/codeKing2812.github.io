import pygame as pg
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
vinduBredde = 800
vinduHøyde  = 600
vindu = pg.display.set_mode([vinduBredde, vinduHøyde])

bgListe = spritesheetTilListe(absRef('bilder/veiSmal.png'), 80, 60, 3, 10)
bgBildeNr = 0


######################### klasser ###################################


class Sprite(pg.sprite.Sprite):
    def __init__(self, bildeListe, bildeNr, x, y, posisjon, skalar=1):
        self.bildeListe = bildeListe
        self.x = x
        self.y = y
        self.posisjon = posisjon
        self.skalar = skalar
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
        
    def oppdater(self):
        self.x += self.xv
        self.y += self.yv
        vindu.blit(self.bilde, (self.x, self.y))

        self.spesifikOppdater()



class Hindring(Sprite):
    def __init__(self, bildeListe, bildeNr, x, y, fart, posisjon, skalar):
        super().__init__(bildeListe, bildeNr, x, y, posisjon, skalar)

        # self.xv = xv
        # self.yv = yv
        self.orginal_x = x
        self.orginal_y = y
        self.fart = fart
    
    def spesifikOppdater(self):
        if f40.posisjon + 10 > self.posisjon:
            self.komIMot()

    def komIMot(self):
        if self.y > vinduHøyde or self.x + self.bredde < 0 or self.x > vinduBredde:
            self.xv = 0
            self.yv = 0

        

        self.yv = f40.fart/100
        if self.x < vinduBredde/2:
            self.xv = - self.yv/10
        else:
            self.xv = self.yv/10
        
        self.skalar += 0.02
        self.bilde = pg.transform.scale_by(self.originalBilde, self.skalar)
        self.x += -(self.bredde/2 - (self.skalar-0.02)*self.originalBilde.get_width()/2)
        
        




class Bil(Sprite):
    def __init__(self, bildeListe, bildeNr, x, y, fart):
        super().__init__(bildeListe, bildeNr, x, y, 0)

        self.fart = fart

    def spesifikOppdater(self):
        self.posisjon += self.fart/fps

    def oppdaterVeifart(self, fartsendring):
        global veifart
        self.fart += fartsendring
        veifart = 200-self.fart
 
        if fartsendring > 0:
            self.skalar -= 0.05
        else:
            self.skalar += 0.05
        
        self.bilde = pg.transform.scale_by(self.originalBilde, self.skalar)

        print('oppdaterVeifart',  veifart)

        pg.time.set_timer(OPPDATERBG, veifart)


bilBilde = spritesheetTilListe(absRef('bilder/f40.png'), 32, 16, 1, 8)
f40 = Bil(bilBilde, 0, vinduBredde/2, 450, 100)
kaktusBilde = spritesheetTilListe(absRef('bilder/kaktus.png'), 16, 16, 1, 4)
kaktus = Hindring(kaktusBilde, 0, 400, 300, 0, 1000, 0.1)

buskBilde = spritesheetTilListe(absRef('bilder/busk.png'), 16, 16, 1, 3)
busk = Hindring(buskBilde, 0, 600, 300, 0, 2000, 0.1)


######################### gameloop ###################################


clock = pg.time.Clock()
fps = 60
PAUSE = False
spillSlutt = False

veifart = 100
OPPDATERBG = pg.USEREVENT + 1
pg.time.set_timer(OPPDATERBG, veifart)

while not spillSlutt and not PAUSE: 

    for event in pg.event.get():

        # slutt spillet hvis vinduet lukkes
        if event.type == pg.QUIT:
            spillSlutt = True
        
            
        # animer bakgrunnen
        if event.type == OPPDATERBG:
            if bgBildeNr < len(bgListe)-1:
                bgBildeNr += 1
            else: bgBildeNr = 0


        # knappetrykk
        if event.type == pg.KEYDOWN:

            if event.key == pg.K_UP or event.key == pg.K_w:
                f40.oppdaterVeifart(5)
            if event.key == pg.K_DOWN or event.key == pg.K_s:
                f40.oppdaterVeifart(-5)
            

            if event.key == pg.K_LEFT or event.key == pg.K_a:
                f40.xv = -4
            if event.key == pg.K_RIGHT or event.key == pg.K_d:
                f40.xv = 4

            if event.key == pg.K_SPACE:
                PAUSE = not PAUSE    

        if event.type == pg.KEYUP:
            if event.key == pg.K_LEFT or event.key == pg.K_RIGHT or event.key == pg.K_a or event.key == pg.K_d:
                f40.xv = 0


    fartTekst = font.render(str(f40.fart) + ' kmt', True, (0,0,0), None)
    posisjonTekst = font.render(str(round(f40.posisjon)) + ' m', True, (0,0,0), None)



    vindu.blit(bgListe[bgBildeNr], (0,0))

    vindu.blit(fartTekst, (10, 10))
    vindu.blit(posisjonTekst, (10, 40))

    f40.oppdater()
    kaktus.oppdater()
    busk.oppdater()
        
    pg.display.flip()
    clock.tick(fps)


pg.quit()
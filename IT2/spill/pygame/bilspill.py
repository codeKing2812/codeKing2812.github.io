import pygame as pg
import os




def absRef(relRef): # funksjon for å finne absolutt referanse til en fil fra relativ referanse
    return os.path.join(os.path.dirname(__file__), relRef)


def spritesheet(sheet, sheetBredde, sheetHøyde, kolonne, rad):    
    bilde = pg.Surface((sheetBredde, sheetHøyde), pg.SRCALPHA)
    bilde.blit(sheet, (0, 0), (kolonne*sheetBredde, rad*sheetHøyde, kolonne*sheetBredde+sheetBredde, rad*sheetHøyde+sheetHøyde))
    return bilde

def spritesheetTilListe(sheetRef, bredde, høyde, antall, skaler):
    sheet = pg.image.load(sheetRef)
    tempListe = []
    for i in range(antall):
        bilde = spritesheet(sheet, bredde, høyde, 0, i)
        bilde = pg.transform.scale_by(bilde, skaler)
        tempListe.append(bilde)

    return tempListe


    



pg.init()

# Angir hvilken skrifttype og tekststørrelse vi vil bruke på tekst
font = pg.font.SysFont("Arial", 24)

# Oppretter et vindu
vinduBredde = 1000
vinduHøyde  = 600
vindu = pg.display.set_mode([vinduBredde, vinduHøyde])

bgListe = spritesheetTilListe(absRef('bilder/bakgrunn.png'), 100, 60, 3, 10)
bgBildeNr = 0




class Ting(pg.sprite.Sprite):
    def __init__(self, bildeListe, bildeNr, x, y, fart):
        self.bildeListe = bildeListe
        self.x = x
        self.y = y
        self.xv = 0
        self.yv = 0
        self.fart = fart

        self.bilde = bildeListe[bildeNr]
        # self.bilde = bildeListe
        
    def oppdater(self):
        self.x += self.xv

        vindu.blit(self.bilde, (self.x, self.y))

bilBilder = spritesheetTilListe(absRef('bilder/f40.png'), 32, 16, 1, 8)
# bilBilder = pg.transform.scale_by(pg.image.load(absRef('bilder/f40.png')), 8)

bil = Ting(bilBilder, 0, vinduBredde/2, 450, 0)





# Gameloop
clock = pg.time.Clock()
PAUSE = False
spillSlutt = False

OPPDATERBG = pg.USEREVENT + 1
pg.time.set_timer(OPPDATERBG, 100)

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

            if event.key == pg.K_LEFT:
                bil.xv = -2
            elif event.key == pg.K_RIGHT:
                bil.xv = 2

            if event.key == pg.K_SPACE:
                PAUSE = not PAUSE    

        if event.type == pg.KEYUP:
            if event.key == pg.K_LEFT or event.key == pg.K_RIGHT:
                bil.xv = 0


    vindu.blit(bgListe[bgBildeNr], (0,0))
    bil.oppdater()
        
    pg.display.flip()
    clock.tick(60)


pg.quit()
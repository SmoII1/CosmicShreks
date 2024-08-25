import pygame
import settings
import random
import pygame.freetype
pygame.init()


class Corabl:
    def __init__(self):
        self.kartinka = pygame.image.load("resurse/korabl.png")
        self.kartinka = pygame.transform.scale(self.kartinka, [350, 250])
        shirina = self.kartinka.get_width()
        visota = self.kartinka.get_height()
        self.hitbox = pygame.Rect([175, 650], [shirina, visota])
        self.xp = 3

    def otrisofka(self, okno):
        okno.blit(self.kartinka, self.hitbox)

    def ypravlenie(self):

        klavishi = pygame.key.get_pressed()
        if klavishi[pygame.K_LEFT] is True and self.hitbox.x > 0:
            self.hitbox.x = self.hitbox.x - 6
        if klavishi[pygame.K_RIGHT] is True and \
                self.hitbox.right < settings.SHIRINA:
            self.hitbox.x = self.hitbox.x + 6


kartinka = pygame.image.load("resurse/shrek.png")
kartinka = pygame.transform.scale(kartinka, [150, 150])


class meteorit:
    def __init__(self):
        self.skorosty = random.randint(1, 4)
        self.skotostx = random.randint(-3, 3)
        shirina = kartinka.get_width()
        visota = kartinka.get_height()
        self.hitbox = pygame.Rect([random.randint(0, settings.SHIRINA), 0], [shirina, visota])

    def otrissofka(self, okno):
        okno.blit(kartinka, self.hitbox)

    def dvishenie(self):
        self.hitbox.y = self.hitbox.y + self.skorosty
        self.hitbox.x = self.hitbox.x + self.skotostx


kartinkalaser = pygame.image.load("resurse/laser.png")
kartinkalaser = pygame.transform.scale(kartinkalaser, [40, 80])


class Laser:
    def __init__(self, koorditati):
        self.skorost = 5
        shirina = kartinkalaser.get_width()
        visota = kartinkalaser.get_height()
        self.hitbox = pygame.Rect(koorditati, [shirina, visota])

    def otrisovka(self, okno):
        okno.blit(kartinkalaser, self.hitbox)

    def dvishenie(self):
        self.hitbox.y = self.hitbox.y - self.skorost


kartinka3 = pygame.image.load("assets/PNG/UI/buttonBlue.png")
kartinka3 = pygame.transform.scale(kartinka3, [300, 150])
shrift = pygame.freetype.Font("resurse/shrift.otf", 25)


class Knopka:
    def __init__(self, koordinati, tekst):
        self.tekst = tekst
        shirina = kartinka3.get_width()
        visota = kartinka3.get_height()
        self.hitbox = pygame.Rect(koordinati, [shirina, visota])
        spisok = shrift.render(tekst)
        self.kartinkastekstom = spisok[0]
        self.hitbox2 = spisok[1]
        self.hitbox2.center = self.hitbox.center

    def otrisovka(self, okno):
        okno.blit(kartinka3, self.hitbox)
        okno.blit(self.kartinkastekstom, self.hitbox2)


kartinka4 = pygame.image.load("resurse/serdche.png")
kartinka4 = pygame.transform.scale(kartinka4, [100, 100])


class Cerdcha:
    def __init__(self, koordinati):
        shirina = kartinka4.get_width()
        visota = kartinka4.get_height()
        self.hitbox = pygame.Rect(koordinati, [shirina, visota])

    def otrisovka(self, okno):
        okno.blit(kartinka4, self.hitbox)

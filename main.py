import pygame
import settings
import sprites

korabl = sprites.Corabl()

Laseri = []

meteor = []

okno = pygame.display.set_mode([settings.SHIRINA, settings.VISOTA])

clock = pygame.time.Clock()

chikl = 0

serdche1 = sprites.Cerdcha([50, 0])

serdche2 = sprites.Cerdcha([150, 0])

serdche3 = sprites.Cerdcha([250, 0])

serdcha = []

serdcha.append(serdche1)
serdcha.append(serdche2)
serdcha.append(serdche3)

knopka = sprites.Knopka([400, 250], "Продолжить игру")

knopka2 = sprites.Knopka([400, 450], "Выйти из игры")

knopka3 = sprites.Knopka([400, 650], "Начать заново")

doshdmeteoritov = pygame.USEREVENT
pygame.time.set_timer(doshdmeteoritov, 700)

vremiaigri = 0
vremiavistrila = 0

sostoyanie = 1

music = pygame.mixer.Sound("resurse/music.wav")
zvyklazera = pygame.mixer.Sound("resurse/zvyk lazera.wav")

fon = pygame.image.load("resurse/fon.png")
fon = pygame.transform.scale(fon, [settings.SHIRINA, settings.VISOTA])
fon2 = pygame.image.load("resurse/fon2.jpg")
fon2 = pygame.transform.scale(fon2, [settings.SHIRINA, settings.VISOTA])

music.set_volume(0.05)
zvyklazera.set_volume(0.1)

music.play(-1)

while chikl == 0:

    vremiaigri = pygame.time.get_ticks()

    if sostoyanie == 1:
        okno.blit(fon, [0, 0])
        korabl.otrisofka(okno)
        for meteorit in meteor:
            meteorit.otrissofka(okno)
        for laser in Laseri:
            laser.otrisovka(okno)
        for serdca in serdcha:
            serdca.otrisovka(okno)
    else:
        okno.blit(fon2, [0, 0])
        if korabl.xp > 0:
            knopka.otrisovka(okno)
        knopka2.otrisovka(okno)
        knopka3.otrisovka(okno)

    fps = clock.get_fps()
    pygame.display.set_caption(str(int(fps)))
    pygame.display.update()

    if sostoyanie == 1:
        korabl.ypravlenie()
        for meterit in meteor:
            meterit.dvishenie()
        for laser in Laseri:
            laser.dvishenie()
        for Laserii in Laseri:
            for meteoriti in meteor:
                if meteoriti.hitbox.colliderect(Laserii.hitbox):
                    meteor.remove(meteoriti)
                    Laseri.remove(Laserii)
        for meteoritbI in meteor:
            if korabl.hitbox.colliderect(meteoritbI.hitbox):
                serdcha.remove(serdcha[-1])
                meteor.remove(meteoritbI)
                korabl.xp = korabl.xp - 1
                if korabl.xp == 0:
                    print("Вы проиграли хапхахпах")
                    sostoyanie = 2

    spisok_sabiti = pygame.event.get()
    for sobitie in spisok_sabiti:
        if sobitie.type == doshdmeteoritov and sostoyanie == 1:
            meteoryte = sprites.meteorit()
            meteor.append(meteoryte)
        if sobitie.type == pygame.QUIT:
            chikl = chikl + 1
        if sobitie.type == pygame.MOUSEBUTTONDOWN and vremiaigri - vremiavistrila >= 300:
            if sostoyanie == 1:
                zvyklazera.play()
            Laser = sprites.Laser(korabl.hitbox.center)
            vremiavistrila = pygame.time.get_ticks()
            Laseri.append(Laser)
        if sobitie.type == pygame.KEYDOWN:
            if sobitie.key == pygame.K_ESCAPE:
                if sostoyanie == 1:
                    sostoyanie = 2
                else:
                    sostoyanie = 1
        if sobitie.type == pygame.MOUSEBUTTONDOWN and sostoyanie == 2:
            if knopka.hitbox.collidepoint(sobitie.pos) is True and korabl.xp > 0:
                sostoyanie = 1
            if knopka2.hitbox.collidepoint(sobitie.pos) is True:
                chikl = chikl + 1
            if knopka3.hitbox.collidepoint(sobitie.pos) is True:
                korabl.xp = 3
                meteor.clear()
                Laseri.clear()
                sostoyanie = 1
                serdcha.append(serdche1)
                serdcha.append(serdche2)
                serdcha.append(serdche3)
    clock.tick(144)

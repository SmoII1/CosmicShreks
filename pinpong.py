import pygame

okno = pygame.display.set_mode([1080, 650])

machik = pygame.rect.Rect([0, 0], [100, 100])
raketka1 = pygame.rect.Rect([0, 200], [25, 200])
raketka2 = pygame.rect.Rect([1055, 200], [25, 200])

clock = pygame.time.Clock()

igrok1 = 0
igrok2 = 0

chikl = 0
f = 2
a = 2
k = 2
while chikl == 0:
    machik.y = machik.y+f
    if machik.bottom >= 650:
        f = -2
    if machik.y <= 0:
        f = 2
    machik.x = machik.x+a
    if machik.right >= 1080:
        a = -2
        machik.x = 540
        machik.y = 325
        igrok1 = igrok1 + 1
    if machik.x <= 0:
        a = 2
        machik.x = 540
        machik.y = 325
        igrok2 = igrok2 + 1

    if igrok1 == 5:
        print("Победил игрок 1")
        chikl = chikl + 1
    if igrok2 == 5:
        print("Победил игрок 2")
        chikl = chikl + 1

    if raketka1.colliderect(machik):
        a = 2
    if raketka2.colliderect(machik):
        a = -2

    klavishi = pygame.key.get_pressed()
    if klavishi[pygame.K_UP] is True and raketka1.y > 0:
        raketka1.y = raketka1.y-k
    if klavishi[pygame.K_DOWN] is True and raketka1.bottom < 650:
        raketka1.y = raketka1.y+k

    okno.fill([105, 22, 204])
    pygame.draw.ellipse(okno, [255, 255, 255], machik)
    pygame.draw.rect(okno, [55, 55, 55], raketka1)
    pygame.draw.rect(okno, [55, 55, 55], raketka2)
    fps = clock.get_fps()
    pygame.display.set_caption(str(int(fps)))
    pygame.display.update()

    spisok_sabiti = pygame.event.get()
    for sobitie in spisok_sabiti:
        if sobitie.type == pygame.QUIT:
            chikl = chikl + 1
    clock.tick(144)

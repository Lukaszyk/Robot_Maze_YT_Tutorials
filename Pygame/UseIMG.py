import pygame

pygame.init()

window = pygame.display.set_mode((650, 650))
pygame.display.set_caption("Robot") #zmiana nazwy okna

spin = 0 # obrót

def draw_image():
    triant = pygame.image.load("Robot_Maze_YT_Tutorials/IMG/triant.png")
    triant = pygame.transform.scale(triant, (300, 300))
    triant = pygame.transform.flip(triant, False, True)
    #triant = pygame.transform.rotate(triant, 45)
    triant = pygame.transform.rotate(triant, spin)

    triant_rect = triant.get_rect(center = (650/2, 650/2))

    window.fill((0, 0, 0))
    window.blit(triant, triant_rect)


run = True
while run:
    pygame.time.delay(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    spin += 1
    draw_image()

    pygame.display.update()

pygame.quit()
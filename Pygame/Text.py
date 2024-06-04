import pygame

pygame.init()

window = pygame.display.set_mode((650, 650))
pygame.display.set_caption("Text") #zmiana nazwy okna

FONT = pygame.font.SysFont("cambria", 25)

def draw_text(text, font, color, x, y):
    window.fill((0, 0, 0))

    TEXT = font.render(text, True, color)
    window.blit(TEXT, (x, y))


run = True

while run:
    pygame.time.delay(30)

    draw_text("Dawid Łukaszyk!", FONT, (255, 255, 255), 250, 300)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
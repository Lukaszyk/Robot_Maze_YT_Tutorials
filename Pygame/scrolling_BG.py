import pygame

pygame.init()

window = pygame.display.set_mode((1000, 650))
pygame.display.set_caption("Scrolling BG") #zmiana nazwy okna

bg = pygame.image.load("Robot_Maze_YT_Tutorials/IMG/tree.jpg")
bg2 = pygame.transform.scale(bg, (1000, 650))
position = 0

def background():
    global position

    window.fill((0, 0, 0))

    #sposób drugi
    for num in range(0, 2): # 0 i 1
        window.blit(bg2, (bg2.get_width() * num + position, 0)) #wyrysowanie tła w pozycji rozmiar * 0 daje 0 + 0(5,10,15...600) taka jest pozycja startowa, następnie będzie rozmiar * 1 + 0(5,10,15,...,600)
        

    #sposób pierwszy
    #window.blit(bg2, (position, 0))
    #window.blit(bg2, (bg2.get_width() + position, 0)) #.get_width() pozwala pobrać szerokość elementu, w tym wypadku tła

    position -= 5

    if abs(position) > bg2.get_width():
        position = 0

run = True

while run:
    pygame.time.delay(60)

    background()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()

pygame.quit()
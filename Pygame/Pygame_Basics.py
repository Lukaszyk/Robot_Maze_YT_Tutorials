import pygame

pygame.init()

window = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Cool Game") #zmiana nazwy okna
x = 50
y = 50
width = 50
height = 50

Jump = False
jump_height = 20
jump_vel = jump_height
gravity = 5



run = True

while run:
    pygame.time.delay(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > 0:
        x -= 5
    if keys[pygame.K_RIGHT] and x < 600 - width:
        x += 5
    if keys[pygame.K_UP] and y > 0:
        y -= 5
    if keys[pygame.K_DOWN] and y < 600 - height:
        y += 5

    if keys[pygame.K_SPACE]:
        Jump = True
    
    if Jump:
        y -= jump_vel
        jump_vel -= gravity
        if jump_vel < -jump_height:
            Jump = False
            jump_vel = jump_height

    window.fill((0, 0, 0))

    pygame.draw.rect(window, (0, 0, 255), (x, y, width, height))
    pygame.display.update()

pygame.quit()
import pygame
pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width,screen_height))

pygame.display.set_caption("nado game")

background = pygame.image.load("C:/Users/ab/source/repos/week_1/background.png")

running = True
while running :
    for event in pygame.event.get() : 
        if event.type == pygame.QUIT:
            running = False
    #screen.fill((0,0,,255))
    screen.blit(background, (0,0))

    pygame.display.update()

pygame.quit()
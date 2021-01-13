import pygame
pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width,screen_height))

pygame.display.set_caption("nado game")

background = pygame.image.load("C:/Users/ab/source/repos/week_1/background.png")

#character
character = pygame.image.load("C:/Users/ab/source/repos/week_1/character.png")
character_size = character.get_rect().size 
character_width = character_size[0]
character_height = character_size[1]
character_x_position = (screen_width - character_width)/ 2
character_y_position = screen_height - character_height

running = True
while running :
    for event in pygame.event.get() : 
        if event.type == pygame.QUIT:
            running = False
    
    screen.blit(background, (0,0))
    screen.blit(character,(character_x_position,character_y_position))
    pygame.display.update()

pygame.quit()
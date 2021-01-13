import pygame
pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width,screen_height))

pygame.display.set_caption("nado game")

background = pygame.image.load("C:/Users/ab/source/repos/week_1/background.png")

#fps 

clock = pygame.time.Clock()
#character
character = pygame.image.load("C:/Users/ab/source/repos/week_1/character.png")
character_size = character.get_rect().size 
character_width = character_size[0]
character_height = character_size[1]
character_x_position = (screen_width - character_width)/ 2
character_y_position = screen_height - character_height

to_x = 0 
to_y = 0

character_speed = 0.6


# enemy
enemy = pygame.image.load("C:/Users/ab/source/repos/week_1/enemy.png")
enemy_size = enemy.get_rect().size 
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_x_position = (screen_width - enemy_width)/ 2
enemy_y_position = (screen_height - enemy_height)/2

running = True
while running :
    dt = clock.tick(60)

    #print("fps: " + str(clock.get_fps()))
    for event in pygame.event.get() : 
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_LEFT :
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT :
                to_x += character_speed
            elif event.key == pygame.K_UP :
                to_y -= character_speed
            elif event.key == pygame.K_DOWN :
                to_y += character_speed

        if event.type == pygame.KEYUP :
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT :
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN :
                to_y = 0

    character_x_position += to_x * dt
    character_y_position += to_y * dt

    if character_x_position < 0 :
        character_x_position = 0
    elif character_x_position > screen_width - character_width :
            character_x_position = screen_width - character_width
    if character_y_position < 0 :
        character_y_position = 0
    elif character_y_position > screen_height - character_height :
        character_y_position = screen_height - character_height

    character_rect = character.get_rect()
    character_rect.left = character_x_position
    character_rect.top = character_y_position


    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_position
    enemy_rect.top = enemy_y_position
    
    if character_rect.colliderect(enemy_rect) :
        print("collision!")
        running = False

    screen.blit(background, (0,0))
    screen.blit(character,(character_x_position, character_y_position))
    screen.blit(enemy, (enemy_x_position, enemy_y_position))
    pygame.display.update()

pygame.quit()
import pygame, sys, random

#setup
pygame.init()
pygame.display.set_caption("Science Fair")
timer = pygame.time.Clock()
WINDOW_SIZE = (400,400)
screen = pygame.display.set_mode(WINDOW_SIZE, 0, 32)

# player
player = pygame.image.load("assets/regular_guy.png")
player_location = [50, 50]

# Science Fair Changing Variables

# npcs
infected1 = pygame.image.load("assets/infected_guy.png")
infected1_location = [0, 0]
infected2 = pygame.image.load("assets/infected_guy.png")
infected2_location = [100, 0]
infected3 = pygame.image.load("assets/infected_guy.png")
infected3_location = [200, 0]
infected4 = pygame.image.load("assets/infected_guy.png")
infected4_location = [300, 0]
infected5 = pygame.image.load("assets/infected_guy.png")
infected5_location = [0, 100]

regular1 = pygame.image.load("assets/cured_guy.png")
regular1_location = (400, 0)
regular2 = pygame.image.load("assets/cured_guy.png")
regular2_location = (100, 100)
infected6 = pygame.image.load("assets/infected_guy.png")
infected6_location = [200, 100]
regular3 = pygame.image.load("assets/cured_guy.png")
regular3_location = (300, 100)
regular4 = pygame.image.load("assets/cured_guy.png")
regular4_location = (400, 100)
regular5 = pygame.image.load("assets/cured_guy.png")
regular5_location = (0, 200)
infected7 = pygame.image.load("assets/infected_guy.png")
infected7_location = [100, 200]
infected8 = pygame.image.load("assets/infected_guy.png")
infected8_location = [200, 200]
regular6 = pygame.image.load("assets/cured_guy.png")
regular6_location = (300, 200)
infected9 = pygame.image.load("assets/infected_guy.png")
infected9_location = [400, 200]


# game loop
while True:
    screen.fill(pygame.Color("grey"))
    screen.blit(player, player_location)

    
    screen.blit(infected1, infected1_location)
    screen.blit(infected2, infected2_location)
    screen.blit(infected3, infected3_location)
    screen.blit(infected4, infected4_location)
    screen.blit(infected5, infected5_location)
    screen.blit(infected6, infected6_location)
    screen.blit(infected7, infected7_location)
    screen.blit(infected8, infected8_location) 
    screen.blit(infected9, infected9_location)  


    screen.blit(regular1, regular1_location)
    screen.blit(regular2, regular2_location)
    screen.blit(regular3, regular3_location)
    screen.blit(regular4, regular4_location)
    screen.blit(regular5, regular5_location)
    screen.blit(regular6, regular6_location)

    moving_right = False
    moving_left = False
    moving_up = False
    moving_down = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                moving_right = True
            if event.key == pygame.K_LEFT:
                moving_left = True
            if event.key == pygame.K_UP:
                moving_up = True
            if event.key == pygame.K_DOWN:
                moving_down = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                moving_right = False
            if event.key == pygame.K_LEFT:
                moving_left = False
            if event.key == pygame.K_UP:
                moving_up = False
            if event.key == pygame.K_DOWN:
                moving_down = False
    if moving_right == True:
        player_location[0] += 50
    if moving_left == True:
        player_location[0] -= 50
    if moving_up == True:
        player_location[1] -= 50
    if moving_down == True:
        player_location[1] += 50

    if player_location == infected1_location:
        pygame.quit()
        sys.exit()
    if player_location == infected2_location:
        pygame.quit()
        sys.exit()
    if player_location == infected3_location:
        pygame.quit()
        sys.exit()
    if player_location == infected4_location:
        pygame.quit()
        sys.exit()
    if player_location == infected5_location:
        pygame.quit()
        sys.exit()
    if player_location == infected6_location:
        pygame.quit()
        sys.exit()
    if player_location == infected7_location:
        pygame.quit()
        sys.exit()
    if player_location == infected8_location:
        pygame.quit()
        sys.exit()
    if player_location == infected9_location:
        pygame.quit()
        sys.exit()

    pygame.display.update()
    timer.tick(60)
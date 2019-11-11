# 1 - Import library
import pygame
from pygame.locals import *

# 2 - Initialize the game
pygame.init()
width, height = 1280, 480
screen = pygame.display.set_mode((width, height))

# 3 - Load images
pikachu = pygame.image.load("resources/images/pikachu.png")
squirtle = pygame.image.load("resources/images/squirtle.png")
charmander = pygame.image.load("resources/images/charmander.png")
meowth = pygame.image.load("resources/images/meowth.png")
james = pygame.image.load("resources/images/james.png")
jessie = pygame.image.load("resources/images/jessie.png")
go = pygame.image.load("resources/images/pokeball.png")
background = pygame.image.load("resources/images/background.jpg")
boat = pygame.image.load("resources/images/boat.png")
grass = pygame.image.load("resources/images/grass.png")

# 4 - keep looping through
while 1:
    # 5 - clear the screen before drawing it again
    screen.fill(0)
    # 6 - draw the screen elements
    screen.blit(background, (0, 0))
    screen.blit(pikachu, (950,307))
    screen.blit(squirtle, (1000, 307))
    screen.blit(charmander, (1050, 303))
    screen.blit(meowth, (1100, 300))
    screen.blit(james, (1150, 205))
    screen.blit(jessie, (1200, 207))
    screen.blit(go, (640, 50))
    screen.blit(grass, (960,182))
    screen.blit(boat, (840, 350))
    screen.blit(grass, (0, 182))
    # 7 - update the screen
    pygame.display.flip()
    # 8 - loop through the events
    for event in pygame.event.get():
        # check if the event is the X button
        if event.type == pygame.QUIT:
            # if it is quit the game
            pygame.quit()
            exit(0)

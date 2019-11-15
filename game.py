# 1 - Import library
import os
import tkinter as tk

import pyautogui
import pygame

root = tk.Tk()

screen_width = root.winfo_screenwidth()  # getting width of screen resolution
screen_height = root.winfo_screenheight()  # getting height of screen resolution

print(screen_width, screen_height)

# 2 - Initialize the game
pygame.init()
width, height = 1280, 480
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Pokemon Team-Rocket Game')
clock = pygame.time.Clock()  # for limiting FPS
FPS = 30
exit_demo = False

pos_x = screen_width - width
pos_y = screen_height - height
os.environ['SDL_VIDEO_WINDOW_POS'] = '%i,%i' % (pos_x, pos_y)
os.environ['SDL_VIDEO_CENTERED'] = '0'

print(pos_x, pos_y)

# 3 - Load images
pikachu = pygame.image.load("resources/images/pikachu.png")
squirtle = pygame.image.load("resources/images/squirtle.png")
charmander = pygame.image.load("resources/images/charmander.png")
meowth = pygame.image.load("resources/images/meowth.png")
james = pygame.image.load("resources/images/james.png")
jessie = pygame.image.load("resources/images/jessie.png")
go = pygame.image.load("resources/images/pokeball.png")
background = pygame.image.load("resources/images/background.png")
boat = pygame.image.load("resources/images/boat.png")
grass = pygame.image.load("resources/images/grass.png")

# positions

w, h = pygame.display.get_surface().get_size()  # w = width, h = height

pikachuPos = (w - 320, h - 170)
pikachuFlag = True

squirtlePos = (w - 270, h - 170)
squirtleFlag = True

charmanderPos = (w - 220, h - 170)
charmanderFlag = True

meowthPos = (w - 170, h - 175)
meowthFlag = True

jamesPos = (w - 120, h - 260)
jamesFlag = True

jessiePos = (w - 70, h - 260)
jessieFlag = True

boatPos = (w - 440, h - 150)
boatFlag = True

# 4 - keep looping through
while not exit_demo:
    # 5 - clear the screen before drawing it again
    screen.fill(0)
    # 6 - draw the screen elements
    screen.blit(background, (0, 0))

    if pikachuFlag:
        screen.blit(pikachu, pikachuPos)
    if squirtleFlag:
        screen.blit(squirtle, squirtlePos)
    if charmanderFlag:
        screen.blit(charmander, charmanderPos)
    if meowthFlag:
        screen.blit(meowth, meowthPos)
    if jamesFlag:
        screen.blit(james, jamesPos)
    if jessieFlag:
        screen.blit(jessie, jessiePos)
    screen.blit(go, (640, 50))
    screen.blit(grass, (960, 182))
    if boatFlag:
        screen.blit(boat, boatPos)
    screen.blit(grass, (0, 182))
    # 7 - update the screen
    pygame.display.flip()
    # 8 - loop through the events

    x = pyautogui.position().x
    y = pyautogui.position().y

    for event in pygame.event.get():
        # check if the event is the X button
        if event.type == pygame.QUIT:
            # if it is quit the game
            pygame.quit()
            exit_demo = True

        elif event.type == pygame.MOUSEBUTTONUP:
            if (event.button == 1) and (w - x > event.pos[0] > w - x - 270) and (w - y > event.pos[
                1] > w - y - 240) and pikachuFlag:  # 1-left, 2-middle, 3-right, 4-height, 5-wheel up, 6-wheel down
                pikachuPos = (event.pos[0] - 50, 307)
                pikachuFlag = False

            print(x, y)

            if event.button == 1 and 795 > event.pos[0] > 725 and 220 > event.pos[1] > 150:
                boatPos = (320, 350)

    # draw the image here
    screen.blit(pikachu, pikachuPos)
    screen.blit(boat, boatPos)
    # update screen
    pygame.display.update()
    clock.tick(FPS)
pygame.quit()
quit()

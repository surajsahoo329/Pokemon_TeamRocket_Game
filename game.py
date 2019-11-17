# 1 - Import library
import os
import tkinter as tk
from ctypes import POINTER, WINFUNCTYPE, windll
from ctypes.wintypes import BOOL, HWND, RECT

import pyautogui
import pygame

os.environ['SDL_VIDEO_CENTERED'] = '1'  # setting pygame window to centre

root = tk.Tk()

screen_width = root.winfo_screenwidth()  # getting width of screen resolution
screen_height = root.winfo_screenheight()  # getting height of screen resolution

if screen_height < 480 or screen_width < 1280:
    print("Game doesn't minimum screen resolution requirements.Quitting game...")
    print("Minimum screen resolution requirements : 1280x480")
    exit(0)

pygame.init()  # 2 - Initialize the game
width, height = 1280, 480
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Pokemon Team-Rocket Game')
clock = pygame.time.Clock()  # for limiting FPS
FPS = 10
exit_demo = False

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

w, h = pygame.display.get_surface().get_size()  # w = width of pygame window, h = height of pygame window

pikachuPos = (w - 320, h - 170)
pikachuLeftFlag = False
pikachuRightFlag = False

squirtlePos = (w - 270, h - 170)
squirtleLeftFlag = False
squirtleRightFlag = False

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

leftSeatBoatRHS = (840, 292)  # left seat of right hand side boat
rightSeatBoatRHS = (900, 292)  # right seat of right hand side boat

leftSeatFlag = True
rightSeatFlag = True

while not exit_demo:  # 4 - keep looping through
    screen.fill(0)  # 5 - clear the screen before drawing it again
    screen.blit(background, (0, 0))  # 6 - draw the screen elements

    hwnd = pygame.display.get_wm_info()["window"]  # get our window ID:
    prototype = WINFUNCTYPE(BOOL, HWND, POINTER(RECT))  # Jump through all the ctypes hoops:
    paramflags = (1, "hwnd"), (2, "lprect")
    GetWindowRect = prototype(("GetWindowRect", windll.user32), paramflags)
    rect = GetWindowRect(hwnd)  # finally get our data!

    if not pikachuLeftFlag or not pikachuRightFlag:
        screen.blit(pikachu, pikachuPos)
    if not squirtleLeftFlag or not squirtleRightFlag:
        screen.blit(squirtle, squirtlePos)
    if charmanderFlag:
        screen.blit(charmander, charmanderPos)
    if meowthFlag:
        screen.blit(meowth, meowthPos)
    if jamesFlag:
        screen.blit(james, jamesPos)
    if jessieFlag:
        screen.blit(jessie, jessiePos)

    screen.blit(grass, (0, 182))  # left side grass
    screen.blit(go, (640, 50))
    if boatFlag:
        screen.blit(boat, boatPos)
    screen.blit(grass, (960, 182))  # right side grass 7 - update the screen
    pygame.display.flip()  # 8 - loop through the events

    x = pyautogui.position().x  # x-coordinate of mouse position on screen not window
    y = pyautogui.position().y  # y-coordinate of mouse position

    # print("x, y ", x,y)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # check if the event is the X button
            pygame.quit()  # if it is quit the game
            exit_demo = True
            exit(1)

        elif pygame.MOUSEBUTTONUP == event.type:
            # print(x, y)
            # print("rect.right", rect.right - 10 - 270)
            # print("rect.right lesser", rect.right - 10 - 320)
            # print("rect.bottom", rect.bottom - 10 - 130)
            # print("rect.bottom lesser", rect.bottom - 10 - 160)

            # Pikachu movements

            if event.button == 1 and rect.right - 10 - 270 > x > rect.right - 10 - 320 and rect.bottom - 10 - 130 > y > rect.bottom - 10 - 160 and (
                    not pikachuLeftFlag or not pikachuRightFlag):  # 1-left, 2-middle, 3-right, 4-height, 5-wheel up, 6-wheel down
                if leftSeatFlag:
                    pikachuPos = leftSeatBoatRHS
                    leftSeatFlag = False
                    pikachuLeftFlag = True
                elif rightSeatFlag:
                    pikachuPos = rightSeatBoatRHS
                    rightSeatFlag = False
                    pikachuRightFlag = True  # On Boarding boat pikachu
            if event.button == 1 and rect.right - 10 - 370 > x > rect.right - 10 - 420 and rect.bottom - 10 - 140 > y > rect.bottom - 10 - 180 and pikachuLeftFlag:
                pikachuPos = (960, 312)
                leftSeatFlag = True
                pikachuLeftFlag = False
            if event.button == 1 and rect.right - 10 - 320 > x > rect.right - 10 - 370 and rect.bottom - 10 - 140 > y > rect.bottom - 10 - 180 and pikachuRightFlag:
                pikachuPos = (960, 312)
                rightSeatFlag = True
                pikachuRightFlag = False  # Off boarding boat pikachu

            # Squirtle movements

            if event.button == 1 and rect.right - 10 - 220 > x > rect.right - 10 - 270 and rect.bottom - 10 - 130 > y > rect.bottom - 10 - 170 and (
                    not squirtleLeftFlag or not squirtleRightFlag):
                if leftSeatFlag:
                    squirtlePos = leftSeatBoatRHS
                    leftSeatFlag = False
                    squirtleLeftFlag = True
                elif rightSeatFlag:
                    squirtlePos = rightSeatBoatRHS
                    rightSeatFlag = False
                    squirtleRightFlag = True  # On Boarding boat squirtle
            if event.button == 1 and rect.right - 10 - 370 > x > rect.right - 10 - 420 and rect.bottom - 10 - 140 > y > rect.bottom - 10 - 180 and squirtleLeftFlag:
                squirtlePos = (1010, 312)
                leftSeatFlag = True
                squirtleLeftFlag = False
            if event.button == 1 and rect.right - 10 - 320 > x > rect.right - 10 - 370 and rect.bottom - 10 - 140 > y > rect.bottom - 10 - 180 and squirtleRightFlag:
                squirtlePos = (1010, 312)
                rightSeatFlag = True
                squirtleRightFlag = False  # Off boarding boat squirtle

    screen.blit(boat, boatPos)  # draw boat image here
    screen.blit(pikachu, pikachuPos)  # draw the pikachu image here
    screen.blit(squirtle, squirtlePos)  # draw the squirtle image here
    pygame.display.update()  # update screen
    clock.tick(FPS)

# 1 - Import library
import os
import tkinter as tk
from ctypes import POINTER, WINFUNCTYPE, windll
from ctypes.wintypes import BOOL, HWND, RECT

import numpy
import pyautogui
import pygame

import main

os.environ['SDL_VIDEO_CENTERED'] = '1'  # setting pygame window to centre

root = tk.Tk()

moves_list = main.main()  # Storing steps with another list

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
reset = pygame.image.load("resources/images/reset.png")
go = pygame.image.load("resources/images/pokeball.png")
solution = pygame.image.load("resources/images/solution.png")
background = pygame.image.load("resources/images/background.png")
boat = pygame.image.load("resources/images/boat.png")
grass = pygame.image.load("resources/images/grass.png")
water = pygame.image.load("resources/images/water.png")
win = pygame.image.load("resources/images/win_background.png")
lost = pygame.image.load("resources/images/lost_background.png")


# positions

def reset_values():
    global pikachuPos, pikachuLeftFlag, pikachuRightFlag
    pikachuPos = (960, 310)
    pikachuLeftFlag = False
    pikachuRightFlag = False

    global squirtlePos, squirtleLeftFlag, squirtleRightFlag
    squirtlePos = (1010, 310)
    squirtleLeftFlag = False
    squirtleRightFlag = False

    global charmanderPos, charmanderLeftFlag, charmanderRightFlag
    charmanderPos = (1060, 310)
    charmanderLeftFlag = False
    charmanderRightFlag = False

    global meowthPos, meowthLeftFlag, meowthRightFlag
    meowthPos = (1110, 305)
    meowthLeftFlag = False
    meowthRightFlag = False

    global jamesPos, jamesLeftFlag, jamesRightFlag
    jamesPos = (1160, 215)
    jamesLeftFlag = False
    jamesRightFlag = False

    global jessiePos, jessieLeftFlag, jessieRightFlag
    jessiePos = (1210, 215)
    jessieLeftFlag = False
    jessieRightFlag = False

    global boatPos, boatRightFlag, boatLeftFlag
    boatPos = (840, 332)
    boatRightFlag = True
    boatLeftFlag = False

    global leftSeatFlag, rightSeatFlag
    leftSeatFlag = True
    rightSeatFlag = True


reset_values()  # Reset/Initialize values of players and boat
leftSeatBoatRHS = (850, 292)  # left seat of right hand side boat
rightSeatBoatRHS = (900, 292)  # right seat of right hand side boat
leftSeatBoatLHS = (340, 292)  # left seat of left hand side boat
rightSeatBoatLHS = (390, 292)  # right seat of left hand side boat

state = [3, 3, 1]  # (left 3 = number of missionaries), (middle 3 = number of cannibals), (right 1 = right side of


# river)

def solve():
    global exit_demo
    global event
    i = 1  # moves list position
    global pikachuPos, squirtlePos, charmanderPos, meowthPos, jamesPos, jessiePos, boatPos
    global pikachuLeftFlag, pikachuRightFlag, squirtleLeftFlag, squirtleRightFlag, charmanderLeftFlag, charmanderRightFlag
    global meowthLeftFlag, meowthRightFlag, jamesLeftFlag, jamesRightFlag, jessieLeftFlag, jessieRightFlag

    # Initially all the people are on RHS of the river

    pikachuRHS = True
    squirtleRHS = True
    charmanderRHS = True
    meowthRHS = True
    jamesRHS = True
    jessieRHS = True

    reset_values()
    while not exit_demo:  # 4 - keep looping through
        screen.fill(0)  # 5 - clear the screen before drawing it again
        screen.blit(background, (0, 0))  # 6 - draw the screen elements

        if not pikachuLeftFlag or not pikachuRightFlag:
            screen.blit(pikachu, pikachuPos)
        if not squirtleLeftFlag or not squirtleRightFlag:
            screen.blit(squirtle, squirtlePos)
        if not charmanderLeftFlag or not charmanderRightFlag:
            screen.blit(charmander, charmanderPos)
        if not meowthLeftFlag or not meowthRightFlag:
            screen.blit(meowth, meowthPos)
        if not jamesLeftFlag or not jamesRightFlag:
            screen.blit(james, jamesPos)
        if not jessieLeftFlag or not jessieRightFlag:
            screen.blit(jessie, jessiePos)

        screen.blit(grass, (0, 182))  # left side grass
        screen.blit(solution, (240, 50))  # Solution button
        screen.blit(go, (640, 50))  # Go pokeball boat rowing signal
        screen.blit(reset, (1040, 50))  # Reset button
        screen.blit(water, (330, 240))  # water position
        screen.blit(boat, boatPos)
        screen.blit(grass, (960, 177))  # right side grass 7 - update the screen

        for event in pygame.event.get():

            if event.type == pygame.QUIT:  # check if the event is the X button
                pygame.quit()  # if it is quit the game
                exit_demo = True
                exit(1)

        if moves_list[i][2] == 0:  # boat is in RHS and will move to LHS
            missionary = moves_list[i - 1][0] - moves_list[i][0]  # number of missionaries to be moved
            cannibal = moves_list[i - 1][1] - moves_list[i][1]  # number of cannibals to be moved

            if missionary == 1:
                if pikachuRHS:
                    pikachuPos = (20, 312)
                    pikachuRHS = False
                    pass
                elif squirtleRHS:
                    squirtlePos = (70, 312)
                    squirtleRHS = False
                    pass
                elif charmanderRHS:
                    charmanderPos = (120, 312)
                    charmanderRHS = False
                    pass
            elif missionary == 2:
                if pikachuRHS and squirtleRHS:
                    pikachuPos = (20, 312)
                    squirtlePos = (70, 312)
                    pikachuRHS = False
                    squirtleRHS = False
                    pass
                elif pikachuRHS and charmanderRHS:
                    pikachuPos = (20, 312)
                    charmanderPos = (120, 312)
                    pikachuRHS = False
                    charmanderRHS = False
                    pass
                elif squirtleRHS and charmanderRHS:
                    squirtlePos = (70, 312)
                    charmanderPos = (120, 312)
                    squirtleRHS = False
                    charmanderRHS = False
                    pass

            if cannibal == 1:
                if meowthRHS:
                    meowthPos = (170, 307)
                    meowthRHS = False
                    pass
                elif jamesRHS:
                    jamesPos = (220, 210)
                    jamesRHS = False
                    pass
                elif jessieRHS:
                    jessiePos = (270, 210)
                    jessieRHS = False
                    pass
            elif cannibal == 2:
                if meowthRHS and jamesRHS:
                    meowthPos = (170, 307)
                    jamesPos = (220, 210)
                    meowthRHS = False
                    jamesRHS = False
                    pass
                elif meowthRHS and jessieRHS:
                    meowthPos = (170, 307)
                    jessiePos = (270, 210)
                    meowthRHS = False
                    jessieRHS = False
                    pass
                elif jamesRHS and jessiePos:
                    jamesPos = (220, 210)
                    jessiePos = (270, 210)
                    jamesRHS = False
                    jessieRHS = False
                    pass

            boatPos = (330, 332)  # Finally update boat position to go LHS

        if moves_list[i][2] == 1:  # boat is in LHS and will move to RHS
            missionary = moves_list[i][0] - moves_list[i - 1][0]  # number of missionaries to be moved
            cannibal = moves_list[i][1] - moves_list[i - 1][1]  # number of cannibals to be moved

            if missionary == 1:
                if not pikachuRHS:
                    pikachuPos = (960, 312)
                    pikachuRHS = True
                    pass
                elif not squirtleRHS:
                    squirtlePos = (1010, 312)
                    squirtleRHS = True
                    pass
                elif not charmanderRHS:
                    charmanderPos = (1060, 312)
                    charmanderRHS = True
                    pass
            elif missionary == 2:
                if not pikachuRHS and not squirtleRHS:
                    pikachuPos = (20, 312)
                    squirtlePos = (70, 312)
                    pikachuRHS = True
                    squirtleRHS = True
                    pass
                elif not pikachuRHS and not charmanderRHS:
                    pikachuPos = (20, 312)
                    charmanderPos = (120, 312)
                    pikachuRHS = True
                    charmanderRHS = True
                    pass
                elif not squirtleRHS and not charmanderRHS:
                    squirtlePos = (70, 312)
                    charmanderPos = (120, 312)
                    squirtleRHS = True
                    charmanderRHS = True
                    pass

            if cannibal == 1:
                if not meowthRHS:
                    meowthPos = (1110, 307)
                    meowthRHS = True
                    pass
                elif not jamesRHS:
                    jamesPos = (1160, 210)
                    jamesRHS = True
                    pass
                elif not jessieRHS:
                    jessiePos = (1210, 210)
                    jessieRHS = True
                    pass
            elif cannibal == 2:
                if not meowthRHS and not jamesRHS:
                    meowthPos = (170, 307)
                    jamesPos = (220, 210)
                    meowthRHS = True
                    jamesRHS = True
                    pass
                elif not meowthRHS and not jessieRHS:
                    meowthPos = (170, 307)
                    jessiePos = (270, 210)
                    meowthRHS = True
                    jessieRHS = True
                    pass
                elif not jamesRHS and not jessiePos:
                    jamesPos = (220, 210)
                    jessiePos = (270, 210)
                    jamesRHS = True
                    jessieRHS = True
                    pass
            boatPos = (840, 332)  # Finally update boat position to go RHS

        i += 1

        screen.blit(boat, boatPos)  # draw boat image here
        screen.blit(pikachu, pikachuPos)  # draw pikachu image here
        screen.blit(squirtle, squirtlePos)  # draw squirtle image here
        screen.blit(charmander, charmanderPos)  # draw charmander image here
        screen.blit(meowth, meowthPos)  # draw meowth image here
        screen.blit(james, jamesPos)  # draw james image here
        screen.blit(jessie, jessiePos)  # draw jessie image here
        if moves_list[i][1] > moves_list[i][0] >= 1:
            screen.blit(lost, (0, 0))
        elif moves_list[i][0] == 0 and moves_list[i][1] == 0 and moves_list[i][2] == 0:
            screen.blit(win, (0, 0))
            break
        pygame.display.flip()  # 8 - loop through the events
        pygame.display.update()  # update screen
        clock.tick(FPS)


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
    if not charmanderLeftFlag or not charmanderRightFlag:
        screen.blit(charmander, charmanderPos)
    if not meowthLeftFlag or not meowthRightFlag:
        screen.blit(meowth, meowthPos)
    if not jamesLeftFlag or not jamesRightFlag:
        screen.blit(james, jamesPos)
    if not jessieLeftFlag or not jessieRightFlag:
        screen.blit(jessie, jessiePos)

    screen.blit(grass, (0, 182))  # left side grass
    screen.blit(solution, (240, 50))  # Solution button
    screen.blit(go, (640, 50))  # Go pokeball boat rowing signal
    screen.blit(reset, (1040, 50))  # Reset button
    screen.blit(water, (330, 240))  # water position
    screen.blit(boat, boatPos)
    screen.blit(grass, (960, 177))  # right side grass 7 - update the screen'''

    x = pyautogui.position().x  # x-coordinate of mouse position on screen not window
    y = pyautogui.position().y  # y-coordinate of mouse position

    for event in pygame.event.get():

        # Storing boolean values for which pokemons and Team Rocket positions on boat

        bool_arr = numpy.array(
            [pikachuLeftFlag, pikachuRightFlag, squirtleLeftFlag, squirtleRightFlag, charmanderLeftFlag,
             charmanderRightFlag, meowthLeftFlag, meowthRightFlag, jamesLeftFlag, jamesRightFlag, jessieLeftFlag,
             jessieRightFlag], dtype=bool)

        if event.type == pygame.QUIT:  # check if the event is the X button
            pygame.quit()  # if it is quit the game
            exit_demo = True
            exit(1)

        elif pygame.MOUSEBUTTONUP == event.type:

            # reset button coordinates

            if event.button == 1 and rect.right - 10 - 190 > x > rect.right - 10 - 240 and rect.top + 30 + 120 > y > rect.top + 30 + 50:
                reset_values()

            # solution button coordinates

            if event.button == 1 and rect.left + 10 + 285 > x > rect.left + 10 + 235 and rect.top + 30 + 120 > y > rect.top + 30 + 50:
                solve()  # call solve function to solve the problem using iterative deepening search

            if boatRightFlag:

                # Pikachu movements

                if event.button == 1 and rect.right - 10 - 270 > x > rect.right - 10 - 320 and rect.bottom - 10 - 130 > y > rect.bottom - 10 - 160 and (
                        not pikachuLeftFlag or not pikachuRightFlag):  # 1-left, 2-middle, 3-right, 4-height, 5-wheel
                    # up,
                    # 6-wheel down
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

                # Charmander movements

                if event.button == 1 and rect.right - 10 - 170 > x > rect.right - 10 - 220 and rect.bottom - 10 - 130 > y > rect.bottom - 10 - 170 and (
                        not charmanderLeftFlag or not charmanderRightFlag):
                    if leftSeatFlag:
                        charmanderPos = leftSeatBoatRHS
                        leftSeatFlag = False
                        charmanderLeftFlag = True
                    elif rightSeatFlag:
                        charmanderPos = rightSeatBoatRHS
                        rightSeatFlag = False
                        charmanderRightFlag = True  # On Boarding boat charmander
                if event.button == 1 and rect.right - 10 - 370 > x > rect.right - 10 - 420 and rect.bottom - 10 - 140 > y > rect.bottom - 10 - 180 and charmanderLeftFlag:
                    charmanderPos = (1060, 312)
                    leftSeatFlag = True
                    charmanderLeftFlag = False
                if event.button == 1 and rect.right - 10 - 320 > x > rect.right - 10 - 370 and rect.bottom - 10 - 140 > y > rect.bottom - 10 - 180 and charmanderRightFlag:
                    charmanderPos = (1060, 312)
                    rightSeatFlag = True
                    charmanderRightFlag = False  # Off boarding boat charmander

                # Meowth movements

                if event.button == 1 and rect.right - 10 - 120 > x > rect.right - 10 - 170 and rect.bottom - 10 - 130 > y > rect.bottom - 10 - 170 and (
                        not meowthLeftFlag or not meowthRightFlag):
                    if leftSeatFlag:
                        meowthPos = leftSeatBoatRHS
                        leftSeatFlag = False
                        meowthLeftFlag = True
                    elif rightSeatFlag:
                        meowthPos = rightSeatBoatRHS
                        rightSeatFlag = False
                        meowthRightFlag = True  # On Boarding boat meowth
                if event.button == 1 and rect.right - 10 - 370 > x > rect.right - 10 - 420 and rect.bottom - 10 - 140 > y > rect.bottom - 10 - 180 and meowthLeftFlag:
                    meowthPos = (1110, 307)
                    leftSeatFlag = True
                    meowthLeftFlag = False
                if event.button == 1 and rect.right - 10 - 320 > x > rect.right - 10 - 370 and rect.bottom - 10 - 140 > y > rect.bottom - 10 - 180 and meowthRightFlag:
                    meowthPos = (1110, 307)
                    rightSeatFlag = True
                    meowthRightFlag = False  # Off boarding boat meowth

                # James movements

                if event.button == 1 and rect.right - 10 - 70 > x > rect.right - 10 - 120 and rect.bottom - 10 - 130 > y > rect.bottom - 10 - 270 and (
                        not jamesLeftFlag or not jamesRightFlag):
                    if leftSeatFlag:
                        jamesPos = (850, 192)
                        leftSeatFlag = False
                        jamesLeftFlag = True
                    elif rightSeatFlag:
                        jamesPos = (900, 192)
                        rightSeatFlag = False
                        jamesRightFlag = True  # On Boarding boat james
                if event.button == 1 and rect.right - 10 - 370 > x > rect.right - 10 - 420 and rect.bottom - 10 - 140 > y > rect.bottom - 10 - 280 and jamesLeftFlag:
                    jamesPos = (1160, 210)
                    leftSeatFlag = True
                    jamesLeftFlag = False
                if event.button == 1 and rect.right - 10 - 320 > x > rect.right - 10 - 370 and rect.bottom - 10 - 140 > y > rect.bottom - 10 - 280 and jamesRightFlag:
                    jamesPos = (1160, 210)
                    rightSeatFlag = True
                    jamesRightFlag = False  # Off boarding boat james

                # Jessie movements

                if event.button == 1 and rect.right - 10 - 20 > x > rect.right - 10 - 70 and rect.bottom - 10 - 130 > y > rect.bottom - 10 - 270 and (
                        not jessieLeftFlag or not jessieRightFlag):
                    if leftSeatFlag:
                        jessiePos = (850, 192)
                        leftSeatFlag = False
                        jessieLeftFlag = True
                    elif rightSeatFlag:
                        jessiePos = (900, 192)
                        rightSeatFlag = False
                        jessieRightFlag = True  # On Boarding boat jessie
                if event.button == 1 and rect.right - 10 - 370 > x > rect.right - 10 - 420 and rect.bottom - 10 - 140 > y > rect.bottom - 10 - 280 and jessieLeftFlag:
                    jessiePos = (1210, 210)
                    leftSeatFlag = True
                    jessieLeftFlag = False
                if event.button == 1 and rect.right - 10 - 320 > x > rect.right - 10 - 370 and rect.bottom - 10 - 140 > y > rect.bottom - 10 - 280 and jessieRightFlag:
                    jessiePos = (1210, 210)
                    rightSeatFlag = True
                    jessieRightFlag = False  # Off boarding boat jessie

            else:

                if event.button == 1 and rect.left + 10 + 70 > x > rect.left + 10 + 20 and rect.bottom - 10 - 130 > y > rect.bottom - 10 - 160 and (
                        not pikachuLeftFlag or not pikachuRightFlag):  # 1-left, 2-middle, 3-right, 4-height, 5-wheel
                    # up,
                    # 6-wheel down
                    if leftSeatFlag:
                        pikachuPos = leftSeatBoatLHS
                        leftSeatFlag = False
                        pikachuLeftFlag = True
                    elif rightSeatFlag:
                        pikachuPos = rightSeatBoatLHS
                        rightSeatFlag = False
                        pikachuRightFlag = True  # On Boarding boat pikachu
                if event.button == 1 and rect.left + 10 + 370 > x > rect.left + 10 + 320 and rect.bottom - 10 - 140 > y > rect.bottom - 10 - 180 and pikachuLeftFlag:
                    pikachuPos = (20, 312)
                    leftSeatFlag = True
                    pikachuLeftFlag = False
                if event.button == 1 and rect.left + 10 + 420 > x > rect.left + 10 + 370 and rect.bottom - 10 - 140 > y > rect.bottom - 10 - 180 and pikachuRightFlag:
                    pikachuPos = (20, 312)
                    rightSeatFlag = True
                    pikachuRightFlag = False  # Off boarding boat pikachu

                # Squirtle movements

                if event.button == 1 and rect.left + 10 + 120 > x > rect.left + 10 + 70 and rect.bottom - 10 - 130 > y > rect.bottom - 10 - 170 and (
                        not squirtleLeftFlag or not squirtleRightFlag):
                    if leftSeatFlag:
                        squirtlePos = leftSeatBoatLHS
                        leftSeatFlag = False
                        squirtleLeftFlag = True
                    elif rightSeatFlag:
                        squirtlePos = rightSeatBoatLHS
                        rightSeatFlag = False
                        squirtleRightFlag = True  # On Boarding boat squirtle
                if event.button == 1 and rect.left + 10 + 370 > x > rect.left + 10 + 320 and rect.bottom - 10 - 140 > y > rect.bottom - 10 - 180 and squirtleLeftFlag:
                    squirtlePos = (70, 312)
                    leftSeatFlag = True
                    squirtleLeftFlag = False
                if event.button == 1 and rect.left + 10 + 420 > x > rect.left + 10 + 370 and rect.bottom - 10 - 140 > y > rect.bottom - 10 - 180 and squirtleRightFlag:
                    squirtlePos = (70, 312)
                    rightSeatFlag = True
                    squirtleRightFlag = False  # Off boarding boat squirtle

                # Charmander movements

                if event.button == 1 and rect.left + 10 + 170 > x > rect.left + 10 + 120 and rect.bottom - 10 - 130 > y > rect.bottom - 10 - 170 and (
                        not charmanderLeftFlag or not charmanderRightFlag):
                    if leftSeatFlag:
                        charmanderPos = leftSeatBoatLHS
                        leftSeatFlag = False
                        charmanderLeftFlag = True
                    elif rightSeatFlag:
                        charmanderPos = rightSeatBoatLHS
                        rightSeatFlag = False
                        charmanderRightFlag = True  # On Boarding boat charmander
                if event.button == 1 and rect.left + 10 + 370 > x > rect.left + 10 + 320 and rect.bottom - 10 - 140 > y > rect.bottom - 10 - 180 and charmanderLeftFlag:
                    charmanderPos = (120, 312)
                    leftSeatFlag = True
                    charmanderLeftFlag = False
                if event.button == 1 and rect.left + 10 + 420 > x > rect.left + 10 + 370 and rect.bottom - 10 - 140 > y > rect.bottom - 10 - 180 and charmanderRightFlag:
                    charmanderPos = (120, 312)
                    rightSeatFlag = True
                    charmanderRightFlag = False  # Off boarding boat charmander

                # Meowth movements

                if event.button == 1 and rect.left + 10 + 220 > x > rect.left + 10 + 170 and rect.bottom - 10 - 130 > y > rect.bottom - 10 - 170 and (
                        not meowthLeftFlag or not meowthRightFlag):
                    if leftSeatFlag:
                        meowthPos = leftSeatBoatLHS
                        leftSeatFlag = False
                        meowthLeftFlag = True
                    elif rightSeatFlag:
                        meowthPos = rightSeatBoatLHS
                        rightSeatFlag = False
                        meowthRightFlag = True  # On Boarding boat meowth
                if event.button == 1 and rect.left + 10 + 370 > x > rect.left + 10 + 320 and rect.bottom - 10 - 140 > y > rect.bottom - 10 - 180 and meowthLeftFlag:
                    meowthPos = (170, 307)
                    leftSeatFlag = True
                    meowthLeftFlag = False
                if event.button == 1 and rect.left + 10 + 420 > x > rect.left + 10 + 370 and rect.bottom - 10 - 140 > y > rect.bottom - 10 - 180 and meowthRightFlag:
                    meowthPos = (170, 307)
                    rightSeatFlag = True
                    meowthRightFlag = False  # Off boarding boat meowth

                # James movements

                if event.button == 1 and rect.left + 10 + 270 > x > rect.left + 10 + 220 and rect.bottom - 10 - 130 > y > rect.bottom - 10 - 270 and (
                        not jamesLeftFlag or not jamesRightFlag):
                    if leftSeatFlag:
                        jamesPos = (340, 192)
                        leftSeatFlag = False
                        jamesLeftFlag = True
                    elif rightSeatFlag:
                        jamesPos = (390, 192)
                        rightSeatFlag = False
                        jamesRightFlag = True  # On Boarding boat james
                if event.button == 1 and rect.left + 10 + 370 > x > rect.left + 10 + 320 and rect.bottom - 10 - 140 > y > rect.bottom - 10 - 280 and jamesLeftFlag:
                    jamesPos = (220, 210)
                    leftSeatFlag = True
                    jamesLeftFlag = False
                if event.button == 1 and rect.left + 10 + 420 > x > rect.left + 10 + 370 and rect.bottom - 10 - 140 > y > rect.bottom - 10 - 280 and jamesRightFlag:
                    jamesPos = (220, 210)
                    rightSeatFlag = True
                    jamesRightFlag = False  # Off boarding boat james

                # Jessie movements

                if event.button == 1 and rect.left + 10 + 320 > x > rect.left + 10 + 270 and rect.bottom - 10 - 130 > y > rect.bottom - 10 - 270 and (
                        not jessieLeftFlag or not jessieRightFlag):
                    if leftSeatFlag:
                        jessiePos = (340, 192)
                        leftSeatFlag = False
                        jessieLeftFlag = True
                    elif rightSeatFlag:
                        jessiePos = (390, 192)
                        rightSeatFlag = False
                        jessieRightFlag = True  # On Boarding boat jessie
                if event.button == 1 and rect.left + 10 + 370 > x > rect.left + 10 + 320 and rect.bottom - 10 - 140 > y > rect.bottom - 10 - 280 and jessieLeftFlag:
                    jessiePos = (270, 210)
                    leftSeatFlag = True
                    jessieLeftFlag = False
                if event.button == 1 and rect.left + 10 + 420 > x > rect.left + 10 + 370 and rect.bottom - 10 - 140 > y > rect.bottom - 10 - 280 and jessieRightFlag:
                    jessiePos = (270, 210)
                    rightSeatFlag = True
                    jessieRightFlag = False  # Off boarding boat jessie

            #  row boat condition

            if event.button == 1 and rect.left + 10 + 705 > x > rect.left + 10 + 555 and rect.top + 30 + 120 > y > rect.top + 30 + 50 and (
                    not leftSeatFlag or not rightSeatFlag):

                if boatRightFlag:
                    boatLeftFlag = True
                    boatRightFlag = False
                    boatPos = (330, 332)

                    for j in range(len(bool_arr)):
                        if bool_arr[j]:
                            if j == 0:
                                pikachuPos = leftSeatBoatLHS
                            elif j == 1:
                                pikachuPos = rightSeatBoatLHS
                            elif j == 2:
                                squirtlePos = leftSeatBoatLHS
                            elif j == 3:
                                squirtlePos = rightSeatBoatLHS
                            elif j == 4:
                                charmanderPos = leftSeatBoatLHS
                            elif j == 5:
                                charmanderPos = rightSeatBoatLHS
                            elif j == 6:
                                meowthPos = leftSeatBoatLHS
                            elif j == 7:
                                meowthPos = rightSeatBoatLHS
                            elif j == 8:
                                jamesPos = (340, 192)
                            elif j == 9:
                                jamesPos = (390, 192)
                            elif j == 10:
                                jessiePos = (340, 192)
                            else:
                                jessiePos = (390, 192)
                        if bool_arr[j] and 0 <= j <= 5:
                            state[0] -= 1
                        elif bool_arr[j] and j > 5:
                            state[1] -= 1
                    state[2] = 0
                else:  # else boatLeftFlag
                    boatLeftFlag = False
                    boatRightFlag = True
                    boatPos = (840, 332)

                    for j in range(len(bool_arr)):
                        if bool_arr[j]:
                            if j == 0:
                                pikachuPos = leftSeatBoatRHS
                            elif j == 1:
                                pikachuPos = rightSeatBoatRHS
                            elif j == 2:
                                squirtlePos = leftSeatBoatRHS
                            elif j == 3:
                                squirtlePos = rightSeatBoatRHS
                            elif j == 4:
                                charmanderPos = leftSeatBoatRHS
                            elif j == 5:
                                charmanderPos = rightSeatBoatRHS
                            elif j == 6:
                                meowthPos = leftSeatBoatRHS
                            elif j == 7:
                                meowthPos = rightSeatBoatRHS
                            elif j == 8:
                                jamesPos = (850, 192)
                            elif j == 9:
                                jamesPos = (900, 192)
                            elif j == 10:
                                jessiePos = (850, 192)
                            else:
                                jessiePos = (900, 192)
                        if bool_arr[j] and 0 <= j <= 5:
                            state[0] += 1
                        elif bool_arr[j] and j > 5:
                            state[1] += 1
                        state[2] = 1

    screen.blit(boat, boatPos)  # draw boat image here
    screen.blit(pikachu, pikachuPos)  # draw pikachu image here
    screen.blit(squirtle, squirtlePos)  # draw squirtle image here
    screen.blit(charmander, charmanderPos)  # draw charmander image here
    screen.blit(meowth, meowthPos)  # draw meowth image here
    screen.blit(james, jamesPos)  # draw james image here
    screen.blit(jessie, jessiePos)  # draw jessie image here
    if state[1] > state[0] >= 1:
        screen.blit(lost, (0, 0))
    elif state[0] == 0 and state[1] == 0 and state[2] == 0:
        screen.blit(win, (0, 0))
    pygame.display.flip()  # 8 - loop through the events
    pygame.display.update()  # update screen
    clock.tick(FPS)
import pygame
from pygame.locals import *

pygame.init()

menufont = pygame.font.SysFont("monospace", 24)
dotfont = pygame.font.SysFont("monospace", 72)

width = 640
height = 480

InGame = False

LawrenceSpeed = 10
EnemyExist = []

ButtonOneImg = pygame.image.load("dude.png")
Image = [pygame.image.load("dude.png"), pygame.image.load("dude.png")]
ButtonOnePos = [160, 80]
ButtonTwoPos = [160, 200]
ButtonThreePos = [160, 320]
DotPos = [140, 75]
ButtonSelection = 0

keys = [False, False, False, False, False]
PlayerCoords = [0, 0]
PlayerDrawCoords = [288,208]
EntityCoords = []
Player = pygame.image.load("dude.png")

screen=pygame.display.set_mode((width, height))

screen.fill((0,0,0))
while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:    #A key was pressed
                if event.key == K_a:
                    keys[0] = True
                elif event.key == K_d:
                    keys[1] = True
                elif event.key == K_w:
                    keys[2] = True
                elif event.key == K_s:
                    keys[3] = True
                elif event.key == K_RETURN:
                    keys[4] = True
        if event.type == pygame.KEYUP:      #A key was released
                if event.key == K_a:
                    keys[0] = False
                elif event.key == K_d:
                    keys[1] = False
                elif event.key == K_w:
                    keys[2] = False
                elif event.key == K_s:
                    keys[3] = False
                elif event.key == K_RETURN:
                    keys[4] = False
        if event.type == pygame.QUIT:       #The user quit
            pygame.quit()

    if InGame == False:

        screen.fill((0,0,0))
        
        dot = menufont.render(".", 1, (255,255,0))
        screen.blit(dot, (DotPos[0],(DotPos[1])))
        
        menu1 = menufont.render("RUN LIKE A HERO", 1, (255,255,0))
        screen.blit(menu1, (ButtonOnePos[0],(ButtonOnePos[1])))

        menu2 = menufont.render("HELP", 1, (255,255,0))
        screen.blit(menu2, (ButtonTwoPos[0],(ButtonTwoPos[1])))
        
        menu3 = menufont.render("RUN LIKE A COWARD", 1, (255,255,0))
        screen.blit(menu3, (ButtonThreePos[0],(ButtonThreePos[1])))



        if keys[2] == True and DotPos[1] != 75:
            DotPos[1] -= 120
            keys[2] = False
            ButtonSelection -=1

        if keys[3] == True and DotPos[1] != 315:
            DotPos[1] += 120
            keys[3] = False
            ButtonSelection +=1

        if keys[4] == True:
            if ButtonSelection == 0:
                InGame = True
            elif ButtonSelection == 1:
                print("WASD controls, ENTER/RETURN to jump")
            elif ButtonSelection == 2:
                pygame.quit()
            keys[4] = False
        
        
    if InGame == True:
        screen.fill((51,153,51))
        screen.blit(Player, PlayerDrawCoords)
        
        
        

    pygame.display.flip()



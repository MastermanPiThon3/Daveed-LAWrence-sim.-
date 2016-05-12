import pygame
from PIL import Image, ImageFilter
import random
from pygame.locals import *

pygame.init()

width = 640
height = 480

screen=pygame.display.set_mode((width, height))
font = pygame.font.SysFont("monospace", 24)

choicemain = '0'

PlayerUnitsID = [1]
PlayerUnitsHP = [30]
PlayerUnitsAttack = [1]

PlayerUnitsCoordX=[0]
PlayerUnitsCoordY=[0]




#Unit list
#0 = Null
Image_null = pygame.image.load("dude.png")
#2 = Stormwind Champion
Image_schamps = pygame.image.load("stormwind_champion.jpg")
#3 = Wolfriders
Image_wriders = pygame.image.load("wolfrider.jpg")
#4 = Boulderfist Ogres
Image_ogres = pygame.image.load("boulderfist_ogre.jpg")
#1 = Player
Image_player = pygame.image.load("Paladin_Lawrence.png")

ImagesStock=[Image_null, Image_player, Image_schamps, Image_wriders, Image_ogres]
ImagesScale=[]

for x in range(0,4):
    ImagesScale.append(pygame.transform.scale(ImagesStock[x], (72,72)))
    


LocationID = [0,1,2,3,4,5,6]
LocationNames = ["Ten-Four Village", "Laab 402", "The Mastermandia Gin Nasium", "Cafataria", "The Dark Forest of Bas' Ment", "South Filladefia", "And'ul's Lair"]        

LocationCoordsX = [0,0,0,0,0,0,0]
for x in range(0,6):
    LocationCoordsX[x] = random.randint (-50,50)
LocationCoordsY = [0,0,0,0,0,0,0]
for x in range(0,6):
    LocationCoordsY[x] = random.randint (-50,50)

RNGDice = 0

RNGDice = random.randint(0,5)
QuestLocationID = LocationID[RNGDice]


status = 0

#0 = Event
#1 = Travel
#2 = Battle
intro = True
while intro == True:

    print("Sir Lawrence, the Dread Lord And'ul Villians marches on Mastermandia with his army of 1 million Murlocs!")
    print("We must muster all the men we can to aid the forces of %s." %(LocationNames[QuestLocationID]))
    print("Who should we bring?")
    print("1. A small band of Stormwind Champions...")
    print("2. a company of Wolfriders...")
    print('3. ...or a pair of Boulderfist Ogres?')

    choicemain = input('Well?')
    print(choicemain)
    if choicemain == 1:
        RNGDice = random.randint (3,4)
        print('%d Stormwind Champions added to your army.'%(RNGDice))
        for x in range(0, RNGDice):
            PlayerUnitsID.append(2)
            PlayerUnitsCoordX.append(0)
            PlayerUnitsCoordY.append(0)
            PlayerUnitsHP.append(6)
            PlayerUnitsAttack.append(6)
        intro = False

    elif choicemain == 2:
        RNGDice = random.randint (6,8)
        print('%d Wolfriders added to your army.'%(RNGDice))
        for x in range(0, RNGDice):
            PlayerUnitsID.append(3)
            PlayerUnitsCoordX.append(0)
            PlayerUnitsCoordY.append(0)
            PlayerUnitsHP.append(3)
            PlayerUnitsAttack.append(1)
        intro = False
        
    elif choicemain == 3:
        print("Two Boulderfist Ogres added to your army.")
        PlayerUnitsID.append(4)
        PlayerUnitsID.append(4)
        PlayerUnitsCoordX.append(0)
        PlayerUnitsCoordX.append(0)
        PlayerUnitsCoordY.append(0)
        PlayerUnitsCoordY.append(0)
        PlayerUnitsHP.append(12)
        PlayerUnitsAttack.append(8)
        intro = False

    else:
        print("That doesn't make sense")

print(PlayerUnitsID)
print(PlayerUnitsCoordX)
print(len(PlayerUnitsID))

z = 0

for y in range (0,5):
    for x in range (0,5):
        PlayerUnitsCoordX[z] = x
        PlayerUnitsCoordY[z] = y
        z += 1
        print("I learn")
        if z == len(PlayerUnitsID):
            break
    if z == len(PlayerUnitsID):
            break

print(PlayerUnitsCoordX)
print(PlayerUnitsCoordY)

stage = 1  #Seasons (1=Spring)
status = 2 #0 Talking #1 Travel #2 Battle
substatus = 0 #0 Acting #1 Menu
day = 0
UnitSelection = 0

EnemyUnitsID = [3,3,3]
EnemyUnitsAttack = [2,2,2]
EnemyUnitsHP = [1,1,1]
EnemyUnitsCoordX = [0,0,0]
EnemyUnitsCoordY = [0,0,0]


z=0

for y in range (0,5):
    for x in range (0,5):
        EnemyUnitsCoordX[z] = 5-x
        EnemyUnitsCoordY[z] = 5-y
        z += 1
        print("I learn")
        if z == len(EnemyUnitsID):
            break
    if z == len(EnemyUnitsID):
            break

location = 'Start'
distancetolocations = [10, 10, 10]

print("Let us get moving then, time is of the essence!")

while stage == 1:

    
    while status == 0:
        print('Where shall we be headed?')
        print('1. Fast march to %s!(straight to the action, dangerous)(%d days.)' %(LocationNames[QuestLocationID],distancetolocations[0]))
        print('2. Keep along the main road')
        choicemain = input('Well?')

    while status == 1:
        print('andu')
##len(PlayerUnitsID)
    while status == 2:
        screen.fill((230,153,36))
        turn = 0
        for x in range (0,(len(PlayerUnitsID))):
            if PlayerUnitsID[x] != 0:
                screen.blit(ImagesScale[PlayerUnitsID[x]], ((PlayerUnitsCoordX[x])*80, (PlayerUnitsCoordY[x])*80))
                screen.blit(font.render(str(PlayerUnitsAttack[x]), 1, (230,230,0)), ((PlayerUnitsCoordX[x])*80, (PlayerUnitsCoordY[x])*80))
                screen.blit(font.render(str(PlayerUnitsHP[x]), 1, (202,8,44)), (((PlayerUnitsCoordX[x])*80+50), (PlayerUnitsCoordY[x])*80))
                screen.blit(font.render(str(x), 1, (0,0,0)), ((PlayerUnitsCoordX[x])*80, ((PlayerUnitsCoordY[x])*80+50)))

        for x in range (0,(len(EnemyUnitsID))):
            if PlayerUnitsID[x] != 0:
                screen.blit(ImagesScale[EnemyUnitsID[x]], ((EnemyUnitsCoordX[x])*80, (EnemyUnitsCoordY[x])*80))
                screen.blit(font.render(str(EnemyUnitsAttack[x]), 1, (230,230,0)), ((EnemyUnitsCoordX[x])*80, (EnemyUnitsCoordY[x])*80))
                screen.blit(font.render(str(EnemyUnitsHP[x]), 1, (202,8,44)), (((EnemyUnitsCoordX[x])*80+50), (EnemyUnitsCoordY[x])*80))
                screen.blit(font.render(str(x), 1, (0,0,0)), ((EnemyUnitsCoordX[x])*80, ((EnemyUnitsCoordY[x])*80+50)))

        pygame.display.flip()

        if turn == 0:
            substatus = 1
            
            while substatus == 1:
                choicemain = input('Select a minion')

                if 0 <= choicemain <= len(PlayerUnitsID):
                    screen.blit(font.render('Selected', 1, (0,0,200)), (((PlayerUnitsCoordX[x])*80+50), ((PlayerUnitsCoordY[x])*80+50)))
                    substatus = 0
                    UnitSelection = choicemain

                else:
                    print('Invalid selection')

            substatus = 1

            while substatus == 1:
                choicemain = input('Select move direction')

                if choicemain == 8 and PlayerUnitsCoordY[UnitSelection] > 1:
                    PlayerUnitsCoordY[UnitSelection] -= 1
                    substatus = 0

                elif choicemain == 2:
                    PlayerUnitsCoordY[UnitSelection] += 1
                    substatus = 0

                elif choicemain == 4:
                    PlayerUnitsCoordX[UnitSelection] -= 1
                    substatus = 0

                elif choicemain == 6:
                    PlayerUnitsCoordX[UnitSelection] += 1
                    substatus = 0

                else:
                    print('Invalid move')

            substatus = 1

            while substatus == 1:
                validtargets = 0
                choicemain = input('Select action')

                if choicemain == "wait" or choicemain == "Wait":
                    substatus = 0

                elif choicemain == "attack" or choicemain == "Attack":
                    print("Valid Targets...")
                    for y in range (0, len(EnemyUnitsID)):
                        if abs(PlayerUnitsCoordX[UnitSelection] - EnemyUnitsCoordX[y]) = 1 or abs(PlayerUnitsCoordY[UnitSelection] - EnemyUnitsCoordY[y]) = 1:
                            validtargets += 1
                            print
                            

                    choicemain = input('Select target
                    
                turn = 1

        if turn == 1:
            choicemain = random.randint(0, len(EnemyUnitsID)-1)

            if EnemyUnitsID[choicemain] == 2>0:
                EnemyUnitsCoordY[choicemain] -= 1

            
            elif EnemyUnitsID[choicemain] == 3 and EnemyUnitsCoordY[choicemain]>0:
                EnemyUnitsCoordY[choicemain] -= 2
                
            else:
                turn = 0


        for x in range (0, len(PlayerUnitsID)):
            for y in range (0, len(EnemyUnitsID)):
                if PlayerUnitsCoordX[x] == EnemyUnitsCoordX[y] and PlayerUnitsCoordY[x] == EnemyUnitsCoordY[y]:
                    if PlayerUnitsAttack[x] > EnemyUnitsAttack[y]:
                        EnemyUnitsHP[y] -= 999
                    elif PlayerUnitsAttack[x] < EnemyUnitsAttack[y]:
                        PlayerUnitsHP[x] -= 999
                    else:
                        EnemyUnitsCoordY[y] += 1

                if PlayerUnitsHP[x] <= 0:
                    PlayerUnitsID.pop(x)

                if EnemyUnitsHP[y] <= 0:
                    EnemyUnitsID.pop(y)

        #END OF BATTLE MUST DELETE AND REORGANIZE UNIT LIST

        
        



    
    

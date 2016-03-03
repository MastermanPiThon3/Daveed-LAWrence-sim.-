import pygame
import random
from pygame.locals import *

pygame.init()

width = 640
height = 480

screen=pygame.display.set_mode((width, height))

choicemain = '0'

PlayerUnitsID = [99]
PlayerUnitsHP = [30]
PlayerUnitsAttack = [0]
PlayerUnitsDefense = [1]

#Unit list
#0 = Null
#1 = Stormwind Champion
#2 = Wolfriders
#3 = Boulderfist Ogres
#99 = Player

LocationID = [0,1,2,3,4,5,6]
LocationNames = ["Ten-Four Village", "Laab 402", "The Mastermandia Gin Nasium", "Cafataria", "The Dark Forest of Bas' Ment", "And'ul's Lair", "South Filladefia"]        

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

print("Sir Lawrence, the Dread Lord And'ul Villians marches on Mastermandia with his army of 1 million Murlocs!")
print("We must muster all the men we can to aid the forces of %s." %(LocationNames[QuestLocationID]))
print("Who should we bring?")
print("1. A small band of Stormwind Champions...")
print("2. a company of Wolfriders...")
print('3. ...or a pair of Boulderfist Ogres?')

choicemain = input('Well?')

if choicemain == "1":
    RNGDice = random.randint (3,4)
    print('%d Stormwind Champions added to your army.'%(RNGDice))
    for x in range(0, RNGDice):
        PlayerUnitsID.append([1])

if choicemain == "2":
    RNGDice = random.randint (6,8)
    print('%d Wolfriders added to your army.'%(RNGDice))
    for x in range(0, RNGDice):
        PlayerUnitsID.append([2])

if choicemain == "3":
    print("Two Boulderfist Ogres added to your army.")
    PlayerUnitsID.append([3,3])

print(PlayerUnitsID)

stage = 1  #Seasons (1=Spring)
status = 1 #0 Talking #1 Travel #2 Battle
day = 0

location = 'Start'
distancetolocations = [10, 10, 10]

print("Let us get moving then, time is of the essence!")

while stage == 1:
    while status == 0:
        print('Where shall we be headed?')
        print('1. Fast march to %s! (%d days (straight to the action, dangerous))' %(LocationNames[QuestLocationID],distancetolocations[0]))
        print('2. Keep along the main road')
        choicemain = input('Well?')

    while status == 1:
        print('andu')
    while status == 2:
        print('andu')
        



    
    

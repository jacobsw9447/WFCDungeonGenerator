# Generator Code for the Wave Function Collapse Algorithm
# [ ] Proccessing Method to take in an array of data and set up the rotations and new array of tiled data
# [ ] Generation Method that takes the above array and a map array to fill and processes the tiles into the array for viewing
# [ ] ADD - Generation Method needs to handle backtracking


import pygame
from pygame.math import Vector2
from pygame.locals import *
import math
import SpriteHolder
import random
import copy

importedInfo = []

# get_data  -   Description here
# RETURNS
#                   none.
# PARAMETERS
#   data:           dict list of strings.
def get_data(data):
    #data should come in as a dict list of strings
    importedInfo = data

    
# Processing - generate a new dictionary with the new rotated data.
# RETURNS
#                   dictionary list of strings.
# PARAMETERS
#   images:         list of images
#   dataTable:      
def Processing(images, dataTable):
    #new dictionary of data
    dictData = []

    #rotate current structs
    for i in range(images.__len__()):
        newImg = images[i]
        tempData=dataTable[i]

        # For each cardinal direction
        for j in range(4):
            # Further explanation for this block is required.
            # Sorta kinda understand what's going on here, but not super confident.
            # - WJ
            tempImg = pygame.transform.rotate(newImg,j*90)
            print(j*90)
            tempD = tempData.copy()
            tempD.append(tempD.pop(0))
            dictData.append(SpriteHolder.ImageData(tempImg,tempData))
            tempData = tempD
    
    return dictData


# Generation - takes the array of ImageData and turns it into a 2-D array of
#                   sprite locations by use of integers.
# RETURNS
#                   A 2D array of integers. ?
# PARAMETERS
#   data:           ImageData (SpriteHolder.py)
def Generation(data, screen, tileSize):
    # Placeholder
    #random.seed(1)
    tiles = (int(screen[0]/tileSize),int(screen[1]/tileSize))
    print(tiles)
    map = []
    #Generate the map size for the size of the screen/sprite size
    for t in range(tiles[1]):
        map.append([])
        for s in range(tiles[0]):
            map[t].append(-1)
    mapHeight = map.__len__()
    tempMap = []
    for i in range(mapHeight-1): # vertical = i
        mapWidth = map[i].__len__()
        # for k in range(tempMap.__len__()):
        #     map[k] = tempMap[k]
        for j in range(map[i].__len__()-1): # horizontal = j
          # check to see if at edge of map/out of range on looks
            requirements = ["!!!","!!!","!!!","!!!"]
            if i>0:
                check = map[i-1][j]
                if check != -1:
                    requirements[0] = copy.deepcopy(data[check].passConnects()[2])
                    print("Look Up = "  + str(data[check].passConnects()))
                    pass
                #look up
                pass
            if i<=mapHeight:
                check = map[i+1][j]
                if check != -1:
                    requirements[2] = copy.deepcopy(data[check].passConnects()[0])
                    pass
                # look down
                pass
            if j>0:
                check = map[i][j-1]
                if check != -1:
                    requirements[3] = copy.deepcopy(data[check].passConnects()[1])
                    print("Look Left = "  + str(data[check].passConnects()))
                    pass
                # look left
                pass
            if j<=mapWidth:
                check = map[i][j+1]
                if check != -1:
                    requirements[1] = copy.deepcopy(data[check].passConnects()[3])
                    pass               
                # look right
                pass
            iterD = -1
            possibleData = []
            for d in data:
                iterD+=1
                faces = d.passConnects()
                match = True
                for p in range(4):
                    if requirements[p] != "!!!" and requirements[p] != faces[p]:
                        match = False
                if match:
                    possibleData.append(iterD)
                    print(str(faces)+ "   " + str(requirements))
            print(possibleData)
            if possibleData.__len__()>0:
                map[i][j] = copy.deepcopy(possibleData[random.randint(0,possibleData.__len__()-1)])
        print(str(map[i])+"\n\n")
        #tempMap.append(map[i].copy())

    return map
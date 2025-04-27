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
            tempImg = pygame.transform.rotate(newImg,-j*90)
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
    tiles = (int(screen[0]/tileSize),int(screen[1]/tileSize))
    print(tiles)
    #Generate the map size for the size of the screen/sprite size
    map = [[-1]*tiles[0]]*tiles[1]
    mapHeight = map.__len__()-1
    for i in range(mapHeight): # vertical = i
        mapWidth = map[i].__len__()-1
        for j in range(map[i].__len__()-1): # horizontal = j
          # check to see if at edge of map/out of range on looks
            if i>1:
                # look up
                pass
            elif i<mapHeight:
                # look down
                pass
            if j>1:
                # look left
                pass
            if j<mapWidth:
                # look right
                pass

    return map
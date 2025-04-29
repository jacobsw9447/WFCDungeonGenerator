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

        # For loop to provide the 4 rotated tiles for each individual sprite
        #   - This works for symetrical faces but asymetrical faces do not work properly right now.
        #   - The rotation method is a bit confusing and looking at pygame documentation will help if you are still confused.
        for j in range(4):
            # rotates the sprite into a new orientation
            tempImg = pygame.transform.rotate(newImg,j*90)
            # makes a deepcopy of the data
            tempD = tempData.copy()
            # rotates the data in the array of faces
            tempD.append(tempD.pop(0))
            #---------NEEDS TO IMPLEMENT A MIRRORING METHOD FOR ASYMETRICAL TILES---------------------
            # appends the data to the new dictionary of tile sprites
            dictData.append(SpriteHolder.ImageData(tempImg,tempData))
            # takes the face data and copies it for the next run.
            tempData = tempD
    
    return dictData


# Generation - takes the array of ImageData and turns it into a 2-D array of
#                   sprite locations by use of integers.
# RETURNS
#                   It returns the 2-D array of indexes for the positions of the tiles on screen.
# PARAMETERS
#   data:           ImageData (SpriteHolder.py)
def Generation(data, screen, tileSize):
    random.seed(3)  #random seed used for testing.
    # sets the ammound of tiles for the screen size
    tiles = (int(screen[0]/tileSize),int(screen[1]/tileSize))
    # initiates the map of integers
    map = []
    #Generate the map size for the size of the screen/sprite size
    for t in range(tiles[1]):
        map.append([])
        for s in range(tiles[0]):
            #default is -1 for all cells
            map[t].append(-1)
    # variable for map height
    mapHeight = map.__len__()
    for i in range(mapHeight): # vertical = i
        #variable for map width
        mapWidth = map[i].__len__()
        for j in range(map[i].__len__()): # horizontal = j
          # check to see if at edge of map/out of range on looks
            #sets a default value for all faces
            requirements = ["!!!","!!!","!!!","!!!"]
            #look up for top face requirement
            if i>0:
                check = map[i-1][j]
                if check != -1:
                    requirements[0] = copy.deepcopy(data[check].passConnects()[2])
            # look down for bottom face requirement
            if i+1<mapHeight:
                check = map[i+1][j]
                if check != -1:
                    requirements[2] = copy.deepcopy(data[check].passConnects()[0])
            # look left for left face requirement
            if j>0:
                check = map[i][j-1]
                if check != -1:
                    requirements[3] = copy.deepcopy(data[check].passConnects()[1])
            # look right for right face requirement
            if j+1<mapWidth:
                check = map[i][j+1]
                if check != -1:
                    requirements[1] = copy.deepcopy(data[check].passConnects()[3])
            # iterator for the list of all tiles
            iterD = -1
            #list of potential tiles
            possibleData = []
            # cycles through all tiles
            for d in data:
                iterD+=1
                # gets the face data for the tiles
                faces = d.passConnects()
                # default match true
                match = True
                for p in range(4):
                    # if the face is not a default and the face does not match the tile
                    if requirements[p] != "!!!" and requirements[p] != faces[p]:
                        match = False
                # if it is a possible solution for the tile put it in the potential tile list
                if match:
                    possibleData.append(iterD)
            # randomly select a tile out of the potentials and put the index in the map
            if possibleData.__len__()>0:
                map[i][j] = copy.deepcopy(possibleData[random.randint(0,possibleData.__len__()-1)])
    # return the index map
    return map
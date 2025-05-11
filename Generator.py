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

#checks if there is continuity between the faces and prints an error message
def errorprinter(s1,s2,dir):
    if s1 != s2:
        print(dir+ ": " +s1 + " is not equal to " +s2)

    
# Processing - generate a list with the new rotated sprites held in spriteholder objects.
# RETURNS : list of spriteholder objects
# PARAMETERS : images(list of images), dataTable(list of all faces for associated images)      
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
# RETURNS : 2-D array of integers associated with sprites
# PARAMETERS : ImageData(dictionary of SpriteHolder Objects)
def Generation(data, screen, tileSize):
    forcedeath = False
    #random.seed(3)  #random seed used for testing.
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
    i = 0
    previousStop = (0,0)
    cycles = 0
    while i<mapHeight:
        if forcedeath: break
        #variable for map width
        mapWidth = map[i].__len__()
        j=0
        while j<mapWidth: # horizontal = j
            #print("Starto J loop")
            if forcedeath: break
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
            #print(possibleData)
            # randomly select a tile out of the potentials and put the index in the map
            if possibleData.__len__()>0:
                randomindex = random.randint(0,possibleData.__len__()-1)
                #print(str(possibleData[randomindex]) +"("+ str(i) + "," +str(j)+")")
                map[i][j] = copy.deepcopy(possibleData[randomindex])
            else:
                tempI=0
                tempJ=0
                if previousStop == (i,j):
                    cycles+=1
                if j==0 and i>1:
                    tempI, tempJ = i - 2, j
                elif i<2 or previousStop == (i,j) and cycles == 5:
                    tempI, tempJ = 0, 0
                    cycles = 0
                else:
                    tempI, tempJ = i - 1, j - 1
                previousStop = (i,j)
                while i>=tempI:
                    while (0<tempJ and i>tempI) or (i==tempI and j>tempJ):
                        map[i][j] = -1
                        j-=1
                        if j==0:
                            break
                    j = map[i].__len__()-1
                    i-=1
            j+=1
        i+=1
    # return the index map
    print("Printing map!!\n")
    print(map)
    return map
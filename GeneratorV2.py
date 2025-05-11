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
import Tile
import time
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
def tester(s1,s2,dir):
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
    random.seed()  #random seed used for testing.
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
            if j>0:
                tester(data[map[i][j]].passConnects()[3],data[map[i][j-1]].passConnects()[1],"Left")
    # return the index map
    return map



# Generation - takes the array of ImageData and turns it into a 2-D array of
#                   sprite locations by use of integers.
# RETURNS : 2-D array of integers associated with sprites
# PARAMETERS : ImageData(dictionary of SpriteHolder Objects)
def NewGeneration(data, screen, tileSize):
    random.seed(time.time())  #random seed used for testing.

    # sets the ammound of tiles for the screen size
    tiles = (int(screen[0]/tileSize),int(screen[1]/tileSize))

    # initiates the map
    map = Tile.Tile(None, None, None, None).create_grid(8, 8) ## Change this 
    
    # variable for map height
    mapHeight = map.__len__()

    #variable for map width
    mapWidth = map[0].__len__()

    for i in range(mapHeight): # vertical = i

        for j in range(mapWidth): # horizontal = j

          # check to see if at edge of map/out of range on looks
            #sets a default value for all faces
            requirements = ["!!!","!!!","!!!","!!!"]

            # Gather information about neighboring tiles.
            up = map[i][j].up
            down = map[i][j].down
            left = map[i][j].left
            right = map[i][j].right

            # Check and fill requirements.
            # Up = 0, Right = 1, Down = 2, Left = 3
            if up != None:
                requirements[0] = copy.deepcopy(data[up.image].passConnects()[2])
            if down != None:
                requirements[2] = copy.deepcopy(data[down.image].passConnects()[0])
            if left != None:
                requirements[3] = copy.deepcopy(data[left.image].passConnects()[1])
            if right != None:
                requirements[1] = copy.deepcopy(data[right.image].passConnects()[3])
                
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
                map[i][j].image = copy.deepcopy(possibleData[random.randint(0,possibleData.__len__()-1)])
                map[i][j].collapsed = True
            if j>0:
                tester(data[map[i][j].image].passConnects()[3],data[map[i][j-1].image].passConnects()[1],"Left")
    # return the index map
    for x in range(4):
        print (data[map[0][0].image].passConnects()[x])
    return map
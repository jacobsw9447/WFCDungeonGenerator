# Generator Code for the Wave Function Collapse Algorithm
# [ ] Proccessing Method to take in an array of data and set up the rotations and new array of tiled data
# [ ] Generation Method that takes the above array and a map array to fill and processes the tiles into the array for viewing
# [ ] ADD - Generation Method needs to handle backtracking


import pygame
from pygame.math import Vector2
from pygame.locals import *
import math
import SpriteHolder

importedInfo = []

def get_data(data):
    #data should come in as a dict list of strings
    importedInfo = data

    
#generate a new dictionary with the new rotated data
def Proccessing(images, dataTable):
    #new dictionary of data
    dictData = []
    #rotate current structs
    for i in range(images.__len__()):
        newImg = images[i]
        tempData=dataTable[i].copy()
        for j in range(0,360,90):
             tempImg = pygame.transform.rotate(newImg,-j)
             for k in range(int(j/89)):
                 #rotate the data for mapping connections
                 tempData.append(tempData.pop(0))
             dictData.append(SpriteHolder.ImageData(tempImg,tempData))
    return dictData


def Generation(data, map):
    pass
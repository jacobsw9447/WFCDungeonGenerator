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
        tempData=dataTable[i]
        for j in range(4):
            tempImg = pygame.transform.rotate(newImg,-j*90)
            tempD = tempData.copy()
            tempD.append(tempD.pop(0))
            dictData.append(SpriteHolder.ImageData(tempImg,tempData))
            tempData = tempD
    return dictData

#takes the array of ImageData and turns it into a 2-D array of sprite locations by use of integers
def Generation(data):
    map=[]


    return map
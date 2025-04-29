#Core Code for data viewing and tile setup/import.
# [ ] Code to handle importing of image tiles and display into pygame
# [ ] Code to handle displaying this data
# [ ] Code to handle moving around tilespace
# [ ] Draw method to draw on screen with the array return from Generator.py
# [ ] Update method to update screen with potential updates from the generator file or other code

# [ ] Code to make me a sandwich (OPTIONAL BUT HIGHLY RECOMMENDED)

import pygame
from pygame.math import Vector2
from pygame.locals import *
import math
import spritesheet
import Generator as gen
import SpriteHolder


# mapDraw - Draws the map.
# RETURNS
#               nothing
# PARAMETERS
#   window:     PyGame window object
#   imageArr:   Image dictionary recieved from Generator.Processing()
def tilesDraw(window, imageArr):
    x=0
    image = imageArr[x].passImage()

    # Iterate through each tile position and draw.
    for i in range(0,window.get_width(),image.get_width()):
        for j in range(0,window.get_height(), image.get_height()):
            # Grab image for this tile.
            image = imageArr[x].passImage()

            # Set x-position back to beginning if we reach the end of a line.
            if x>=imageArr.__len__()-1:
                x=0
            
            # Draw the tile and advance x-position.
            window.blit(image,Vector2(i,j))
            x+=1

# update    -   Updates the gamestate.
# RETURNS
#               nothing
# PARAMETERS
#   dt:         Delta time. (Time since last frame)
def update(dt):
    pass


# draw  -   Draws the map.
# RETURNS
#           nothing
# PARAMETERS
#   window:     PyGame window object
#   image:      Image dictionary recieved from Generator.Processing()
def mapDraw(window, mapArray, tileData, tileSize):
    height, width = 0,0
    for line in mapArray:
        for block in line:
            if block != -1:
                window.blit(tileData[block].passImage(), Vector2(width, height))
                width+=tileSize
        height+=tileSize
        width = 0



#-------------------------------START OF GAMELOOP CODE-----------------------------------------------------------
# Set basic parameters and initalize PyGame.
pygame.init()
width, height = 1000,800
window = pygame.display.set_mode([width, height])
font = pygame.font.SysFont('impact', 30, False, False)

#STARTING VARIABLES
state = "run"
data = [[],[],[],[]]
map = []
sprite = "BasicSpriteSheet01.png"
#image = pygame.image.load(sprite)

# Create spritesheet and get all tile images in an array ("images")
ss = spritesheet.spritesheet(sprite)
image = ss.images_at([(0, 0, 32, 32),(32, 0, 32, 32),(64, 0, 32, 32),(96, 0, 32, 32)])

# Tile connections matrix
imageVarData = [["aba","aba","aaa","aaa"],
                ["aba","aba","aaa","aba"],
                ["aaa","aaa","aaa","aaa"],
                ["aba","aba","aba","aba"]]

# Process the tiles extracted in the previous step in order to get rotated variants.
testDataStruct = gen.Processing(image,imageVarData)
# For testing: print the connections
for d in testDataStruct:
    print(d.passConnects())

# Generate the map.
map = gen.Generation(testDataStruct,(width,height),32)
# Timing parameters.
# Gamestate updates occur once per frame.
fps = 60
dt = 1/fps
clock = pygame.time.Clock()
t = 0
#RUN MAIN LOOP
while state != "quit":
    pygame.display.update()
    clock.tick(fps)
    if t < 5:
        t+=dt
    else:
        map = gen.Generation(testDataStruct,(width,height),32)
        t = 0
    #clears screen with a black background
    window.fill([0,0,0])

    # HANDLE EVENTS
    key = pygame.key.get_pressed()
    while event := pygame.event.poll():
        if event.type == pygame.QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
            state = "quit"

    # Update gamestate and draw the map.
    update(dt)
    mapDraw(window, map, testDataStruct, 32)
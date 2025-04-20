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


#MAP DRAW METHOD
def mapDraw(window, image):
    for i in range(0,window.get_width(),image.get_width()):
        for j in range(0,window.get_height(), image.get_height()):
            window.blit(image,Vector2(i,j))

#UPDATE METHOD
def update(dt):
    pass


#DRAW METHOD
def draw(window, image):
    mapDraw(window, image)




#-------------------------------START OF GAMELOOP CODE-----------------------------------------------------------
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
ss = spritesheet.spritesheet(sprite)
image = ss.images_at([(0, 0, 32, 32),(33, 0, 32, 32),(65, 0, 32, 32),(97, 0, 32, 32)])
imageVarData = [["aba","aba","aaa","aaa"],
                ["aba","aba","aba","aaa"],
                ["aaa","aaa","aaa","aaa"],
                ["aba","aba","aba","aba"]]

# timing
fps = 60
dt = 1/fps
clock = pygame.time.Clock()

#RUN LOOP
while state != "quit":
    pygame.display.update()
    clock.tick(fps)
    #clears screen with a black background
    window.fill([0,0,0])

    #EVENTS
    key = pygame.key.get_pressed()
    while event := pygame.event.poll():
        if event.type == pygame.QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
            state = "quit"

    update(dt)
    draw(window, image[1])


    


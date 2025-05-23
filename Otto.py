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


#MAP DRAW METHOD
def mapDraw(window, image):
    starter = image[0]
    iter=0
    for i in range(0,window.get_width(),32):
        for j in range(0,window.get_height(), 32):
            window.blit(image[iter%image.__len__()].passImage(),Vector2(i,j))
            iter+=1

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
spriteset1 = "BasicSpriteSheet01.png"
spriteset1Indexes = [(0, 0, 32, 32),(32, 0, 32, 32),
                     (64, 0, 32, 32),(96, 0, 32, 32)
                     ]
spriteset2 = "BasicSpriteSheet02.png"
spriteset2Indexes = [(0, 0, 32, 32), (32, 0, 32, 32),
                     (64, 0, 32, 32), (96, 0, 32, 32),
                     (128,0,32,32), (160,0,32,32),
                     (192,0,32,32),(224,0,32,32),
                     (256,0,32,32),(288,0,32,32)
                     ]
#image = pygame.image.load(sprite)

# Create spritesheet and get all tile images in an array ("images")
ss = spritesheet.spritesheet(spriteset2)
image = ss.images_at(spriteset2Indexes)

# Tile connections matrix
imageVarData1 = [["aba","aba","aaa","aaa"],
                ["aba","aba","aaa","aba"],
                ["aaa","aaa","aaa","aaa"],
                ["aba","aba","aba","aba"]]
imageVarData2 = [
	["aaa","aba","aaa","aaa"],
	["aaa","aaa","aba","aba"],
	["aaa","aba","aba","aba"],
	["aaa","ddd","aaa","aba"],
	["ddd","dfd","ddd","ddd"],
	["dfd","dfd","ddd","dfd"],
	["dfd","dfd","dfd","dfd"],
	["aaa","ddd","aaa","aaa"],
	["ddd","ddd","aaa","aaa"],
	["aaa","aaa","aaa","aaa"]
]
testDataStruct = gen.Processing(image,imageVarData2)
iter = 0
for t in testDataStruct:
    print(str(iter) + str(t.passConnects()))
    iter+=1

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
    draw(window, testDataStruct)


    

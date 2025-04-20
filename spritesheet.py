# This class handles sprite sheets
# This was taken from www.scriptefun.com/transcript-2-using
# sprite-sheets-and-drawing-the-background
# I've added some code to fail if the file wasn't found..
# Note: When calling images_at the rect is the format:
# (x, y, x + offset, y + offset)

import pygame

class spritesheet(object):
    def __init__(self, filename):
        message = "SpriteSheet shit the bed"
        try:
            self.sheet = pygame.image.load(filename).convert()
        except (pygame.error, message):
            print ('Unable to load spritesheet image:', filename)
            raise (SystemExit, message)
    # Load a specific image from a specific rectangle
    def image_at(self, rectangle, colorkey = None):
        "Loads image from x,y,x+offset,y+offset"
        rect = pygame.Rect(rectangle)
        image = pygame.Surface(rect.size).convert()
        image.blit(self.sheet, (0, 0), rect)
        if colorkey is not None:
            if colorkey is -1:
                colorkey = image.get_at((0,0))
            image.set_colorkey(colorkey, pygame.RLEACCEL)
        return image
    # Load a whole bunch of images and return them as a list
    def images_at(self, rects, colorkey = None):
        "Loads multiple images, supply a list of coordinates" 
        return [self.image_at(rect, colorkey) for rect in rects]
    # Load a whole strip of images
    def load_strip(self, rect, image_count, colorkey = None):
        "Loads a strip of images and returns them as a list"
        tups = [(rect[0]+rect[2]*x, rect[1], rect[2], rect[3])
                for x in range(image_count)]
        return self.images_at(tups, colorkey)

# #Here is a quick example on how you would use this


# import spritesheet
# #...
# ss = spritesheet.spriteshee('somespritesheet.png')
# # Sprite is 16x16 pixels at location 0,0 in the file...
# image = ss.image_at((0, 0, 16, 16))
# images = []
# # Load two images into an array, their transparent bit is (255, 255, 255)
# images = ss.images_at((0, 0, 16, 16),(17, 0, 16,16), colorkey=(255, 255, 255))
# #...

# #Here is a sprite strip animation iterator built on spritesheet.spritesheet


# import spritesheet

# class SpriteStripAnim(object):
#     """sprite strip animator
    
#     This class provides an iterator (iter() and next() methods), and a
#     __add__() method for joining strips which comes in handy when a
#     strip wraps to the next row.
#     """
#     def __init__(self, filename, rect, count, colorkey=None, loop=False, frames=1):
#         """construct a SpriteStripAnim
        
#         filename, rect, count, and colorkey are the same arguments used
#         by spritesheet.load_strip.
        
#         loop is a boolean that, when True, causes the next() method to
#         loop. If False, the terminal case raises StopIteration.
        
#         frames is the number of ticks to return the same image before
#         the iterator advances to the next image.
#         """
#         self.filename = filename
#         ss = spritesheet.spritesheet(filename)
#         self.images = ss.load_strip(rect, count, colorkey)
#         self.i = 0
#         self.loop = loop
#         self.frames = frames
#         self.f = frames
#     def iter(self):
#         self.i = 0
#         self.f = self.frames
#         return self
#     def next(self):
#         if self.i >= len(self.images):
#             if not self.loop:
#                 raise StopIteration
#             else:
#                 self.i = 0
#         image = self.images[self.i]
#         self.f -= 1
#         if self.f == 0:
#             self.i += 1
#             self.f = self.frames
#         return image
#     def __add__(self, ss):
#         self.images.extend(ss.images)
#         return self

# #And an example usage of sprite_strip_anim.SpriteStripAnim


# """
# Sprite strip animator demo

# Requires spritesheet.spritesheet and the Explode1.bmp through Explode5.bmp
# found in the sprite pack at
# http://lostgarden.com/2005/03/download-complete-set-of-sweet-8-bit.html

# I had to make the following addition to method spritesheet.image_at in
# order to provide the means to handle sprite strip cells with borders:

#             elif type(colorkey) not in (pygame.Color,tuple,list):
#                 colorkey = image.get_at((colorkey,colorkey))
# """
# import sys
# import pygame
# from pygame.locals import Color, KEYUP, K_ESCAPE, K_RETURN
# import spritesheet
# from sprite_strip_anim import SpriteStripAnim

# surface = pygame.display.set_mode((100,100))
# FPS = 120
# frames = FPS / 12
# strips = [
#     SpriteStripAnim('Explode1.bmp', (0,0,24,24), 8, 1, True, frames),
#     SpriteStripAnim('Explode2.bmp', (0,0,12,12), 7, 1, True, frames),
#     SpriteStripAnim('Explode3.bmp', (0,0,48,48), 4, 1, True, frames) +
#     SpriteStripAnim('Explode3.bmp', (0,48,48,48), 4, 1, True, frames),
#     SpriteStripAnim('Explode4.bmp', (0,0,24,24), 6, 1, True, frames),
#     SpriteStripAnim('Explode5.bmp', (0,0,48,48), 4, 1, True, frames) +
#     SpriteStripAnim('Explode5.bmp', (0,48,48,48), 4, 1, True, frames),
# ]
# black = Color('black')
# clock = pygame.time.Clock()
# n = 0
# strips[n].iter()
# image = strips[n].next()
# while True:
#     for e in pygame.event.get():
#         if e.type == KEYUP:
#             if e.key == K_ESCAPE:
#                 sys.exit()
#             elif e.key == K_RETURN:
#                 n += 1
#                 if n >= len(strips):
#                     n = 0
#                 strips[n].iter()
#     surface.fill(black)
#     surface.blit(image, (0,0))
#     pygame.display.flip()
#     image = strips[n].next()
#     clock.tick(FPS)
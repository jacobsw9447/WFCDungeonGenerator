import pygame


# ImageData - Stores PyGame Image as well as connection data for a tile.
class ImageData():
    def __init__(self, image, data):
        self.image = image
        self.data = data
        pass
    def passImage(self):
        return self.image
    def passConnects(self):
        return self.data
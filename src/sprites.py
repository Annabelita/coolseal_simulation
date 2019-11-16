"""
Contains all visible simulator objects
@author Andrej Savinov, Annabella Kadavanich, Isabel Schmuck
"""
import pygame as pg
from src.settings import *


"""
Constructor for Ants
"""


class Ant(pg.sprite.Sprite):
    def __init__(self, simulator, x, y, antID):
        self.groups = simulator.all_sprites, simulator.ants
        pg.sprite.Sprite.__init__(self, self.groups)
        self.simulator = simulator
        # How the ant looks like
        self.image = droneIMG
        #self.image = pg.Surface((TILESIZE,TILESIZE))
        #self.image.fill(GREEN_APPLE)
        # Rectangle that encloses the sprite (Position of the sprite on the screen).
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.position = (x,y)
        self.pixelPosition = (x * TILESIZE, y * TILESIZE)
        self.lastPos = None
        self.id = antID
        self.moved = False

    def getID(self):
        return self.id

    def setLastPos(self,pos):
        self.lastPos = pos

    def getLastPos(self):
        return self.lastPos

    # Can be used later to move ants
    def move(self, dx=0, dy=0):
        if not self.isColliding(dx, dy):
            self.x = dx
            self.y = dy

    def isColliding(self, dx=0, dy=0):
        for house in self.simulator.houses:
            if house.x == dx and house.y == dy:
                return True
        return False

    # Update rectangle for pixel coordinates (Position on screen)
    def update(self):
        self.pixelPosition = (self.rect.x, self.rect.y)
        self.position = (self.x, self.y)
        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y * TILESIZE

"""
Constructor for Houses
"""


class House(pg.sprite.Sprite):
    def __init__(self, simulator, x ,y, img):
        self.groups = simulator.all_sprites, simulator.houses
        pg.sprite.Sprite.__init__(self, self.groups)
        self.simulator = simulator
        self.image = img
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE
        self.position = (self.x, self.y)

    def getPosition(self):
        return self.position

"""
Constructor for Streets
"""

class Street(pg.sprite.Sprite):
    def __init__(self, simulator, x ,y):
        self.groups = simulator.all_sprites,simulator.streets
        pg.sprite.Sprite.__init__(self, self.groups)
        self.simulator = simulator
        self.image = street_0IMG
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE
        self.position = (self.x,self.y)
        self.stage = StreetStage_0
        self.id = None
        self.parentPos = None

    def getStage(self):
        return self.stage

    def setStage(self,stage,img):
        self.stage = stage
        self.image = img

    def setID(self,id):
        self.id = id

    def getID(self):
        return self.id

    def setParentPos(self,pos):
        self.parentPos = pos

    def getParentPos(self):
        return self.parentPos

class StartingPosition(pg.sprite.Sprite):
    def __init__(self, simulator, x ,y):
        self.groups = simulator.all_sprites,simulator.startingPos
        pg.sprite.Sprite.__init__(self, self.groups)
        self.simulator = simulator
        self.image = startingPosIMG
        #self.image = pg.Surface((TILESIZE,TILESIZE))
        #self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE
        self.position = (self.rect.x,self.rect.y)

"""
Settings for our simulator
@author Andrej Savinov, Annabella Kadavanich, Isabel Schmuck
"""
import pygame as pg
from os import path


'''
****
############### NO CHANGES HERE! #############################################################################
****
'''

BLACK = (0,0,0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
WATERMELON = (254, 127, 156)
GREEN_APPLE = (94, 119, 3)
TURQUOISE = (100, 212, 199)
ANT = (227, 217, 176)
BROWN = (210,105,30)
WHITE = (255,255,255)
BGCOLOR = (255,255,255)

StreetStage_0 = 0
StreetStage_1 = 1
StreetStage_2 = 2

TITLE = "CoolSeal_Simulator"

TILESIZE = 32
WIDTH = 1024
HEIGHT = 768
GRIDWIDTH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE

#Images for Sprites
imgFolder = path.join(path.dirname(path.dirname(path.abspath(__file__))),"images")

house_1IMG = pg.image.load(path.join(imgFolder,"house_1.png"))
house_2IMG = pg.image.load(path.join(imgFolder,"house_2.png"))

street_0IMG = pg.image.load(path.join(imgFolder,"street_0.png"))
street_1IMG = pg.image.load(path.join(imgFolder,"street_1.png"))
street_2IMG = pg.image.load(path.join(imgFolder,"street_2.png"))
streetIMGList = [street_0IMG,street_1IMG,street_2IMG]

droneIMG = pg.image.load(path.join(imgFolder,"Drone.png"))

startingPosIMG = pg.image.load(path.join(imgFolder,"startingPosition.png"))



'''
****
#####################################################################################################
****
'''

########################################################################
#                       Simulation Options                             #
########################################################################

# How many times per second the simulation is going to be updated (Default for testing = 0, Default for user = 5/10/20)
FPS = 0

# Agent amount (Default = 1)
ANT_AMOUNT = 1

# Which Walk to simulate (Default = 2)
# WALK = 0 : randomWalk() [Performs random walking for the agent] [Maximal ANT_AMOUNT = 3]
# WALK = 1 : simpleWalk() [Performs a random walk with the help of a evaluation function] [Maximal ANT_AMOUNT = 3]# WALK = 3 : simpleWalkStreetFirst() [Performs a street oriented walk with the help of a evaluation function] [Maximal ANT_AMOUNT = 3]
# WALK = 2 : multipleDFS() [Performs a multiple depth first search, as defined in the paper] [Maximal ANT_AMOUNT = 2 and 2 Starting positions]
WALK = 2

# How many times the simulation is going to repeat (Default = 1)
SIMULATIONROUNDS = 1
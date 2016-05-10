#!/usr/bin/env python3

import pygame
import sys

# for networked information, TODO later
import socket
import threading
from pygame.locals import *

from Fish import Fish
from World import World

RESOLUTION = (800, 600)
GAMENAME = 'Aquarium'
BGCOLOR = (0, 0, 0)

# The game is launched

pygame.init()

fpsClock = pygame.time.Clock()

window = pygame.display.set_mode(RESOLUTION)
pygame.display.set_caption(GAMENAME)


# the main loop
isPlaying = True


fishList = [];
algaeList = []
theWorld = World(fishList, algaeList)
fishList.append(Fish((400, 400), theWorld))


while isPlaying:
    window.fill(BGCOLOR)




# not much to do here, since it's mostly all automatic
    for event in pygame.event.get():
        if event.type == QUIT:
            isPlaying = False;
    
    pygame.display.update()
    fpsClock.tick(30)

# end of game loop

pygame.quit()

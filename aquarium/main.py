#!/usr/bin/env python3

import pygame
import sys
import random

# for networked information, TODO later
import socket
import threading
from pygame.locals import *

from fish import Fish
from world import World

RESOLUTION = (1024, 768)
GAMENAME = 'Aquarium'
BGCOLOR = (0, 0, 0)

# The game is launched

pygame.init()

fpsClock = pygame.time.Clock()

window = pygame.display.set_mode(RESOLUTION)
pygame.display.set_caption(GAMENAME)


# the main loop
isPlaying = True


fishList = []
algaeList = []
theWorld = World(RESOLUTION, fishList)
for i in range(20):
    theColor = tuple(random.randint(0, 255) for i in range(3))
    theSize = random.randint(0, 20) + 5 
    thePos = tuple(i*10 for k in range(2))
    fishList.append(Fish(thePos, theColor, theSize, theWorld, window))


while isPlaying:
    window.fill(BGCOLOR)

# not much to do here, since it's mostly all automatic
    for event in pygame.event.get():
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_q]:
            isPlaying = False
        if event.type == QUIT:
            isPlaying = False
    
    theWorld.update()
    theWorld.drawStuff()

    pygame.display.update()
    fpsClock.tick(30)

# end of game loop

pygame.quit()

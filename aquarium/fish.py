# This is the base fish class
import math
import pygame
import random
from itertools import accumulate
from enum import Enum

import numpy as np


class PossibleStates(Enum):
    nothing = 1
    moving = 2
    seeking_food = 3


class Fish():

    def __init__(self, startingPos, startingColor, startingSize, theWorld, theWindow):
        self.currentPos = startingPos
        self.currentPosNum = 0
        self.currentWiggle = 0
        self.angle = 0
        self.worldRef = theWorld
        self.windowRef = theWindow
        self.goalPos = self.currentPos
        self.posTup = tuple()  # a tuple containing the position values
        # the time to move in frames
        self.moveTime = round(random.random() * 120 + 50)
        self.state = PossibleStates.nothing  # defaults to nothing
        self.frameTimer = 0  # number of frame before decision
        self.color = startingColor  # the color in rgb
        self.size = startingSize  # the size in pixels
        self.wait_time = lambda: random.randint(0, 90)
        self.wiggle_amplitude = 0.1
        self.wiggle_speed = 1

    def chooseNextRandomPos(self):
        worldDimensions = self.worldRef.getScreenSize()
        self.goalPos = (random.randint(0, worldDimensions[0]),
                        random.randint(0, worldDimensions[1]))

    def setTrajectoryPosList(self):
        delta = (self.goalPos[0] - self.currentPos[0],
                 self.goalPos[1] - self.currentPos[1])
        poissonks = range(self.moveTime)
        lamb = self.moveTime / 4
        poissonXd = accumulate(
            delta[0] * math.e**(-lamb) * lamb**i / math.factorial(i) for i in range(self.moveTime))
        poissonX = (x + self.currentPos[0] for x in poissonXd)
        poissonYd = accumulate(
            delta[1] * math.e**(-lamb) * lamb**i / math.factorial(i) for i in range(self.moveTime))
        poissonY = (y + self.currentPos[1] for y in poissonYd)
        self.posTup = tuple(zip(poissonX, poissonY))

    def setMove(self):
        self.chooseNextRandomPos()
        self.setTrajectoryPosList()
        self.currentPosNum = 0
        deltaPos = (self.goalPos[0] - self.currentPos[0],
                    self.goalPos[1] - self.currentPos[1])
        self.angle = math.atan2(deltaPos[1], deltaPos[0])
        self.state = PossibleStates.moving

    def move(self):
        self.currentPos = (round(self.posTup[self.currentPosNum][0]),
                           round(self.posTup[self.currentPosNum][1]))
        self.currentPosNum += 1
        self.currentWiggle = math.sin(
            self.currentPosNum * self.wiggle_speed) * self.wiggle_amplitude

    def act(self):

        if self.state != PossibleStates.seeking_food and self.worldRef.isFoodAvailable():
            # food is available, move to it if too far
            pass
        elif self.state == PossibleStates.nothing and self.frameTimer > 0:
            # decrement the timer
            self.frameTimer -= 1
        elif self.state == PossibleStates.nothing:
            # timer is up, start moving
            self.setMove()
        elif self.state in (PossibleStates.moving, PossibleStates.seeking_food):
            # currently moving
            # first, checks if at goal Pos, stops moving
            if self.currentPosNum == self.moveTime:
                self.currentPos = self.goalPos
                if self.state != PossibleStates.seeking_food:
                    # if seeking food, no pause
                    self.frameTimer = self.wait_time()
                self.state = PossibleStates.nothing
            else:
                self.move()

    def draw(self):
        basePos1 = np.asarray([-self.size * 1.5, self.size])
        basePos2 = np.asarray([-self.size * 1.5, -self.size])
        rotMat = rotationMatrix(self.angle + self.currentWiggle)
        newPos1 = rotMat.dot(basePos1) + self.currentPos
        newPos2 = rotMat.dot(basePos2) + self.currentPos

        # the main body
        pygame.draw.circle(self.windowRef, self.color,
                           self.currentPos, self.size)
        # the tail
        pygame.draw.polygon(self.windowRef, self.color,
                            (newPos1, newPos2, self.currentPos))


def rotationMatrix(angle):
    return np.asarray([[np.cos(angle), -np.sin(angle)],
                       [np.sin(angle), np.cos(angle)]])

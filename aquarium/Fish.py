# This is the base fish class
import math
import pygame
import random
from itertools import accumulate

possibleStates = ('nothing', 'moving', 'seeking food')

class Fish():
    def __init__(self, startingPos, theWorld, theWindow):
        self.currentPos = startingPos
        self.currentPosNum = 0
        self.angle = 0
        self.worldRef = theWorld
        self.windowRef = theWindow
        self.goalPos = self.currentPos
        self.posTup = tuple() # a tuple containing the position values
        self.moveTime = 50 # the time to move in frames
        self.state = possibleStates[0] #defaults to nothing
        self.frameTimer = 0; # number of frame before decision
        self.color = (255, 255, 255) # the color in rgb
        self.size = 10 # the size in pixels

    def chooseNextRandomPos(self):
        worldDimensions = self.worldRef.getScreenSize()
        self.goalPos = (random.randint(0, worldDimensions[0]),
                        random.randint(0, worldDimensions[1]))

    def setTrajectoryPosList(self):
        delta = (self.goalPos[0]-self.currentPos[0],
                 self.goalPos[1]-self.currentPos[1])
        poissonks = range(self.moveTime)
        lamb = self.moveTime/4;
        poissonXd = accumulate(delta[0] * math.e**(-lamb) * lamb**i/math.factorial(i) for i in range(self.moveTime))
        poissonX = (x+self.currentPos[0] for x in poissonXd)
        poissonYd = accumulate(delta[1] * math.e**(-lamb) * lamb**i/math.factorial(i) for i in range(self.moveTime))
        poissonY = (y+self.currentPos[1] for y in poissonYd)
        self.posTup = tuple(zip(poissonX, poissonY))

    def setMove(self):
        self.chooseNextRandomPos()
        self.setTrajectoryPosList()
        self.currentPosNum = 0
        deltaPos = (self.goalPos[0] - self.currentPos[0],
                    self.goalPos[1] - self.currentPos[1])
        self.angle = math.atan2(deltaPos[1], deltaPos[0])
        self.state = possibleStates[1]

    def move(self):
        self.currentPos = (round(self.posTup[self.currentPosNum][0]),
                           round(self.posTup[self.currentPosNum][1]))
        self.currentPosNum += 1
        
    def act(self):

        if self.state != possibleStates[2] and self.worldRef.isFoodAvailable():
            # food is available, move to it if too far
            pass
        elif self.state == possibleStates[0] and self.frameTimer > 0:
            # decrement the timer
            self.frameTimer -= 1
        elif self.state == possibleStates[0]:
            # timer is up, start moving
            self.setMove()
        elif self.state in (possibleStates[1], possibleStates[2]):
            # currently moving
            # first, checks if at goal Pos, stops moving
            if self.currentPosNum == self.moveTime:
                self.currentPos = self.goalPos
                if self.state != possibleStates[2]:
                    # if seeking food, no pause
                    self.frameTimer = random.randint(0, 90)
                self.state = possibleStates[0]
            else:
                self.move()
    def draw(self):
        pygame.draw.circle(self.windowRef, self.color, self.currentPos, self.size)
       



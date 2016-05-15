# This is the base fish class
import math
import random
from itertools import accumulate

possibleStates = ('nothing', 'moving', 'seeking food')

class Fish():
    def __init__(self, startingPos, theWorld):
        self.currentPos = startingPos
        self.currentPosNum = 0
        self.angle = 0
        self.worldRef = theWorld
        self.goalPos = self.currentPos
        self.posTup = tuple() # a tuple containing the position values
        self.moveTime = 90 # the time to move in frames
        self.state = possibleStates[0] #defaults to nothing
        self.frameTimer = 0; # number of frame before decision

    def chooseNextRandomPos(self):
        worldDimensions = self.worldRef.getScreenSize()
        self.goalPos = (random.randint(0, self.worldDimensions[0]),
                        random.randint(0, self.worldDimensions[1]))

    def setTrajectoryPosList(self):
        delta = self.goalPos-self.currentPos
        poissonks = range(self.moveTime)
        lamb = moveTime/3;
        poissonXd = accumulate(delta[0] * math.e**(-lamb) * lamb^i/math.factorial(i) for i in range(self.moveTime))
        poissonX = x+self.currentPos[0] for x in poissonXd
        poissonYd = accumulate(delta[1] * math.e**(-lamb) * lamb^i/math.factorial(i) for i in range(self.moveTime))
        poissonY = y+self.currentPos[0] for y in poissonYd
        self.posTup = tuple(zip(poissonX, poissonY))

    def setMove(self):
        self.chooseNextRandomPos()
        self.setTrajectoryPosList()
        self.currentPosNum = 0
        deltaPos = self.goalPos - self.currentPos
        self.angle = math.atan2(deltaPos[1], deltaPos[0])
        self.state = possibleStates[1]

    def move(self):
        self.currentPos = self.posTup[currentPosNum]
        self.currentPosNum += 1
        
    def act(self):

        if self.state != possibleStates[2] && self.worldRef.isfoodAvailable():
            # food is available, move to it if too far
            pass
        elif self.state == possibleStates[0] && self.frameTimer > 0:
            # decrement the timer
            self.frameTimer -= 1
        elif self.state == possibleStates[0]:
            # timer is up, start moving
            self.setMove()
        elif self.state in (possibleStates[1], possibleStates[2]):
            # currently moving
            # first, checks if at goal Pos, stops moving
            if self.goalPosNum == self.moveTime:
                self.currentPos = self.goalPos
                if self.state != possibleStates[2]:
                    # if seeking food, no pause
                    self.frameTimer = random.randint(90)
                self.state = possibleStates[0]
            else
              self.move()
       



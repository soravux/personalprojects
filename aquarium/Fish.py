# This is the base fish class
import math

class Fish():
    def __init__(self, startingPosition, theWorld):
        self.health = 100 # in percentage
        self.speed = 1 # in pixels per second
        self.hunger = 0 # in percentage
        self.eggLayingPeriod = 10 # in minutes
        self.eggHatchPeriod = 10
        self.attackRadius = 10
        self.diet = 'vegetarian' #the other is 'piscivorous'
        self.name = 'fish'
        self.isAValidFish = True
        self.state = None
        self.position = startingPosition
        self.lastDecisionTime = 0
        self.lastLaidTime = 0
        self.theWorld = theWorld

    def isDead(self):
        if self.health <= 0:
            return True
        else:
            return False

    def isHungry(self):
        if self.hunger >= 80:
            return True
        else:
            return False

    def isSatiated(self):
        if self.hunger <= 20:
            return True
        else:
            return False

    def updateGoalPosition(self, newGoalPosition):
        self.goalPosition = newGoalPosition

    def eat(self, nutritionValue):
        self.hunger -= nutritionValue
        self.hunger = max(self.hunger, 0)

    def isWorth(self):
        return self.health-self.hunger

    def isAbleToLay(self):
        return self.hunger < 30

    def move(self):
        newPosition = self.position + (self.speed/30 * math.cos(self.angle), self.speed/30*math.sin(self.angle))

        if self.theWorld.collide(newPosition):
            self.state = 'none'
        else:
            self.position = newPosition

    def act(self):
        ''' This is where most of the work is done'''
        if self.state == 'laying':
            self.hasJustLaid = True
            self.hunger += 30
            self.lastLaidTime = pygame.time.get_ticks
            self.state = 'none'

        elif self.state == 'wandering':
            pass

        elif self.state == 'preying':
            pass

        elif self.state == 'none':
            pass



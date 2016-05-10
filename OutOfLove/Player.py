# This is the player game class

class Player:
    def __init__(self):
        self.health = 100
        self.experience = 0

        self.concealness = 0
        self.adaptability = 0
        self.frugal = 0
        self.fortitude = 0
        
        # the movement bools
        self.mvUp = False
        self.mvDown = False
        self.mvLeft = False
        self.mvRight = False
       
    def isDead(self):
        if self.health <= 0:
            return True
        else:
            return False

    def getHealth(self):
        return self.health

    def getExperience(self):
        return self.experience

    def dontMove(self, dir):
        if dir == "up":
          self.mvUp = False
        elif dir == "down":
          self.mvDown = False
        elif dir == "left":
          self.mvLeft = False
        elif dir == "right":
          self.mvRight = False
    
    def wantToMove(self, dir):
        if dir == "up":
          self.mvUp = True
        elif dir == "down":
          self.mvDown = True
        elif dir == "left":
          self.mvLeft = True
        elif dir == "right":
          self.mvRight = True

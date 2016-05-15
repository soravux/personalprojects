# This is the world class, it serves to model tons of stuff

class World():
    def __init__(self, screenSize, FishList):
        self.fishList = FishList
        self.screenSize = screenSize

    def update(self):
        for fish in self.fishList:
            fish.act()

    def isFoodAvailable(self):
        #TODO
        return False

    def drawStuff(self):
        for fish in self.fishList:
            fish.draw()

    def getScreenSize(self):
        return self.screenSize

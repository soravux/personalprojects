# This is the main game class
import pygame
from pygame.locals import *
from Player import Player

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
STREETCOLOR = (20, 20, 20)  # a dark gray
BUILDINGCOLOR = (120, 120, 120)  # a lighter gray
PARASITECOLOR = (0, 64, 0)  # darkish green
FONTSIZE = 24

UPKEY = ord('w')
LEFTKEY = ord('a')
DOWNKEY = ord('s')
RIGHTKEY = ord('d')

class Game:
    def __init__(self):
        pygame.init()
        self.initialize()

        self.gameLoop()

    def initialize(self):
        self.theWindow = pygame.display.set_mode((800, 600), 0, 32)
        self.theFont = pygame.font.SysFont(None, FONTSIZE)
        self.theWindow.fill(STREETCOLOR)
        pygame.display.set_caption('Out of Love')

        self.thePlayer = Player()
        self.entities = list()

    def updateGraphics(self):
        healthText = self.theFont.render('Health:' + str(self.thePlayer.getHealth()), True, WHITE)
        experienceText = self.theFont.render('Experience:' + str(self.thePlayer.getExperience()), True, WHITE)
        healthRect = healthText.get_rect()
        experienceRect = healthText.get_rect()
        healthRect.topleft = (5, 5)
        experienceRect.topleft = (5, 20)

        self.theWindow.blit(healthText, healthRect)
        self.theWindow.blit(experienceText, experienceRect)
        pygame.display.update();


    def quitGame(self):
        pygame.quit()

    def gameLoop(self):
        isPlaying = True;
        while isPlaying:
            # events
            for event in pygame.event.get():

                if event.type == QUIT:
                    print('Game has quit.')
                    isPlaying = False

                elif event.type == pygame.KEYUP:
                    if event.key == UPKEY:
                        self.thePlayer.dontMove("up")
                    elif event.key == LEFTKEY:
                        self.thePlayer.dontMove("left")
                    elif event.key == DOWNKEY:
                        self.thePlayer.dontMove("down")
                    elif event.key == RIGHTKEY:
                        self.thePlayer.dontMove("right")

                elif event.type == pygame.KEYDOWN:
                    if event.key == UPKEY:
                        self.thePlayer.wantToMove("up")
                    elif event.key == LEFTKEY:
                        self.thePlayer.wantToMove("left")
                    elif event.key == DOWNKEY:
                        self.thePlayer.wantToMove("down")
                    elif event.key == RIGHTKEY:
                        self.thePlayer.wantToMove("right")

            ## game logic
            


            # the graphics are updated
            self.updateGraphics()

        self.quitGame()

# Define some colors
import pygame
from math import pi as PI
BLACK = (   0,   0,   0)
WHITE = ( 255, 255, 255)
GREEN = (   0, 255,   0)
RED   = ( 255,   0,   0)
pygame.init()
size = (700, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Professor Craven's Cool Game")

done = False
frame = 0
clock = pygame.time.Clock()

while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            print('User asked to quit.')
        elif event.type == pygame.KEYDOWN:
            print('User pressed a key.')
        elif event.type == pygame.KEYUP:
            print('User let go of a key.')
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print('User pressed a mouse button')
    frame += 1
    screen.fill(WHITE)
    font = pygame.font.SysFont('monospace', 20)
    pygame.draw.line(screen, RED, [0,0], pygame.mouse.get_pos(), 5)
    pygame.draw.line(screen, RED, size, pygame.mouse.get_pos(), 5)
    pygame.draw.line(screen, RED, (size[0],0), pygame.mouse.get_pos(), 5)
    pygame.draw.line(screen, RED, (0, size[1]), pygame.mouse.get_pos(), 5)
    pygame.draw.line(screen, RED, (size[0]/2,0), pygame.mouse.get_pos(), 5)
    text = font.render("Frames: " + str(frame), True, BLACK)
    screen.blit(text, [250, 250])
    pygame.display.flip()

    clock.tick(60)
pygame.quit()

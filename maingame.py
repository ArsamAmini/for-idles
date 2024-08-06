import pygame

# init
pygame.init()
width = 500
hight = 500
win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Game")

# classes
class player(object):
    def __init__(self, maxl, maxc, width, hight, color):
        pass
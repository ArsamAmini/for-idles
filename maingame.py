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
        self.maxl = maxl
        self.maxc = maxc
        self.width = width
        self.hight = hight
        self.color = color
    
    def draw():
        pass

    def move():
        pass

# redraw
def redeawwindow():
    pass

# main loop
run = True
while run:
    pass
import pygame, sys
from pygame.locals import *
 
# Initialize program
pygame.init()
 
# Assign FPS a value
FPS = 1
w, h = 500, 500
FramePerSec = pygame.time.Clock()
 
# Setting up color objects
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
 
# Setup a 300x300 pixel display with caption
DISPLAYSURF = pygame.display.set_mode((w,h))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Snake")

class Square(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__() 
        w, h = 10, 10
        color = GREEN
        self.x, self.y = x, y
        self.image = pygame.Surface((w, h))
        self.image.fill(color)
        self.rect = self.image.get_rect(center = (self.x, self.y))
        self.dir_x = 0
        self.dir_y = 0

    def update(self):
        self.x += 10 * self.dir_x
        self.y += 10 * self.dir_y
        self.rect = self.image.get_rect(center = (self.x, self.y))
    
    def change_dir(self, dir_x, dir_y):
        self.dir_x = dir_x
        self.dir_y = dir_y

squares = pygame.sprite.Group(
    Square(10, 10)
)

while True:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                [square.change_dir(-1, 0) for square in squares]
            if event.key == pygame.K_RIGHT:
                [square.change_dir(1, 0) for square in squares]
            if event.key == pygame.K_UP:
                [square.change_dir(0, -1) for square in squares]
            if event.key == pygame.K_DOWN:
                [square.change_dir(0, 1) for square in squares]
        if event.type == pygame.K_RIGHT:
            [square.change_dir(1, 1) for square in squares]
            print('right')
        if event.type == pygame.MOUSEBUTTONUP:
            print('lalala')


    DISPLAYSURF.fill(WHITE)
    squares.draw(DISPLAYSURF)
    [square.update() for square in squares]
    pygame.display.flip()
    FramePerSec.tick(FPS)

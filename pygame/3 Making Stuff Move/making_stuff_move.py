import pygame
import sys
from pygame.locals import *

def main():
    pygame.init()
    FPS = 30
    fpsClock = pygame.time.Clock()

    window_size = (0, 0)
    screen = pygame.display.set_mode(window_size)

    pygame.display.set_caption("Making Stuff Move")

    WHITE = pygame.Color(255, 255, 255)
    GOLD = pygame.Color(255, 215, 0)
    RED = pygame.Color(255, 0, 0)

    screen.fill(WHITE)
    colors_for_house = {'house': GOLD, 'roof': RED}

    house = House(200, 200, 100, colors_for_house)
    house.draw(screen)

    move_up = False;
    move_down = False;
    move_left = False;
    move_right = False;

    while True:  # <--- main game loop
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == KEYDOWN:
                if event.key == K_UP:
                    move_up = True
                if event.key == K_DOWN:
                    move_down = True
                if event.key == K_LEFT:
                    move_left = True
                if event.key == K_RIGHT:
                    move_right = True

            if event.type == KEYUP:
                if event.key == K_UP:
                    move_up = False
                if event.key == K_DOWN:
                    move_down = False
                if event.key == K_LEFT:
                    move_left = False
                if event.key == K_RIGHT:
                    move_right = False

        if move_up:
            house.changeY(-10)
        if move_down:
            house.changeY(10)
        if move_left:
            house.changeX(-10)
        if move_right:
            house.changeX(10)

        # redraw the background and house each frame
        screen.fill(WHITE)
        house.draw(screen)
        pygame.display.update()
        fpsClock.tick(FPS)

class House:

    def __init__(self, x, y, size, colors):
        self.x = x
        self.y = y
        self.size = size
        self.colors = colors

    def draw(self, screen):
        pygame.draw.rect(screen, self.colors['house'], [self.x, self.y, self.size, self.size] )
        self.__draw_roof(screen)

    def __draw_roof(self, screen):
        pointlist = [ (self.x - 20, self.y), (self.x + self.size + 20, self.y), (self.x + 100, self.y - 100)]

        pygame.draw.polygon(screen, self.colors['roof'], pointlist)

    def changeX(self, inc):
        self.x += inc;

    def changeY(self, inc):
        self.y += inc;

if __name__ == "__main__":
    main()
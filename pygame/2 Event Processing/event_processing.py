import pygame
import sys
import random
import math
from pygame.locals import *


def main():

    # Always be sure to call the init() function before doing anything else
    pygame.init()

    # set the FPS for this game
    FPS = 30 # 30 frames per second
    fpsClock = pygame.time.Clock()

    # code to create the initial window
    windowSize = (0, 0)
    screen = pygame.display.set_mode(windowSize)

    # set the title of the window
    pygame.display.set_caption("Event Processing")

    # create some color objects
    FUCHSIA = pygame.Color(255, 0, 255)
    WHITE = pygame.Color(255, 255, 255)

    # change the initial background color to white
    screen.fill(WHITE)

    while True:  # <--- main game loop
        for event in pygame.event.get():

            if event.type == QUIT:  # QUIT event to exit the game
                pygame.quit()
                sys.exit()

            # puts some text on the screen
            font = pygame.font.SysFont("Arial", 20, True, True) # (name, size, bold, italic)
            text = font.render("Press t, l, c, e, and x (multiple times)", True, FUCHSIA) # (text to display, anti aliasing, color)
            # to put it on the screen
            screen.blit(text, [0, 0])

            #######Key Events#######
            if event.type == KEYDOWN:
                if event.key == K_t: # t key pressed
                    draw_triangles(100, 100, 100, screen)
                elif event.key == K_l: # l key pressed
                    draw_lines(45, 200, 50, screen)
                elif event.key == K_c: # c key pressed
                    draw_circles(60, 400, 50, screen)
                elif event.key == K_e: # e key pressed
                    draw_ellipses([60, 500, 100, 50], screen)
                elif event.key == K_x: # x key pressed
                    font = pygame.font.SysFont('Calibri', 25, True, False)
                    text = font.render("Pygame is fun!!",True ,random_color())
                    screen.blit(text, [260, 250])

        pygame.display.update() # update the display when all events have been processed
        fpsClock.tick(FPS)

def random_color():
    return pygame.Color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

def draw_triangles(x, y, length, screen):
    radius = (math.sqrt(3) / 3) * length

    for i in range(1, 6):
        width = 0 if i % 2 != 0 else 3
        points = [ (x, y - radius), (x + radius, y + radius), (x - radius, y + radius)]
        pygame.draw.polygon(screen, random_color(), points, width)
        x += 125

def draw_lines(x, y, length, screen):
    width = 2
    for i in range(1, 6):
        pygame.draw.line(screen, random_color(), (x, y), (x+100, y), width)
        y += 25
        width += 2

def draw_circles(x, y, length, screen):
    for i in range(1, 6):
        width = 0 if i % 2 == 0 else 5
        pygame.draw.circle(screen, random_color(), (x, y), length, width)
        x += 100

def draw_ellipses(bounding_rectangle, screen):
    for i in range(1, 6):
        width = 0 if i % 2 != 0 else 5
        pygame.draw.ellipse(screen, random_color(), bounding_rectangle, width)
        bounding_rectangle = [bounding_rectangle[0] + 100, bounding_rectangle[1], 100, 50]

if __name__ == "__main__":
    main()

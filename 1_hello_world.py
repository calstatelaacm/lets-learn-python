import pygame
import sys
from pygame.locals import *

def main():

    # always be sure to call the init() function before doing anything else
    pygame.init()

    # set the FPS for this game, in this case, 30 frames per second
    FPS = 30
    fpsClock = pygame.time.Clock()

    # create the initial window
    windowSize = (0, 0) # (0, 0) makes it full screen
    screen = pygame.display.set_mode(windowSize)

    # set the title of the window
    pygame.display.set_caption("My First Pygame Game!!!")

    # create some color objects
    BLACK = pygame.Color(0, 0 , 0)
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
            text = font.render("Hello World!", True, BLACK) # (text to display, anti aliasing, color)
            # to put it on the screen
            screen.blit(text, [100, 100])

        pygame.display.update() # update the display when all events have been processed
        fpsClock.tick(FPS) # limits the program to never run at more than `FPS` frames per second

if __name__ == "__main__":
    main()

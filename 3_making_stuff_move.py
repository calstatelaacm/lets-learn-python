import pygame
import sys
from pygame.locals import *

def main():

    pygame.init()
    FPS = 60
    fps_clock = pygame.time.Clock()

    window_size = (0, 0)
    screen = pygame.display.set_mode(window_size)

    pygame.display.set_caption("Make Stuff Move")

    WHITE = pygame.Color(255, 255, 255)
    screen.fill(WHITE)

    moveLeft = False;
    moveRight = False;
    moveDown = False;
    moveUp = False;

    dogX = 0
    dogY = 0

    # add dog.jpg image to screen
    dog = pygame.image.load("dog.png").convert_alpha() # don't forget .convert()
    screen.blit(dog, (dogX, dogY))

    while True:  # <--- main game loop
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == KEYDOWN:
                if event.key == K_UP:
                    moveUp = True
                if event.key == K_DOWN:
                    moveDown = True
                if event.key == K_LEFT:
                    moveLeft = True
                if event.key == K_RIGHT:
                    moveRight = True
            if event.type == KEYUP:
                if event.key == K_UP:
                    moveUp = False
                if event.key == K_DOWN:
                    moveDown = False
                if event.key == K_LEFT:
                    moveLeft = False
                if event.key == K_RIGHT:
                    moveRight = False

        if moveUp:
            dogY -= 10
        if moveDown:
            dogY += 10
        if moveLeft:
            dogX -= 10
        if moveRight:
            dogX += 10

        screen.fill(WHITE)
        screen.blit(dog, (dogX, dogY))
        pygame.display.update()  # needed to update the display when all events have been processed
        fps_clock.tick(FPS)

if __name__ == "__main__":
    main()

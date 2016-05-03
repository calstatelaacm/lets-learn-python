import pygame
import sys
from pygame.locals import *

def main():
    pygame.init()

    FPS = 30
    fpsClock = pygame.time.Clock()

    BLACK = pygame.Color(0, 0, 0)

    window_size = (812, 499)
    screen = pygame.display.set_mode(window_size)
    pygame.display.set_caption("Music & Sounds")

    # set the background image
    background = pygame.image.load("img/sky.jpg").convert()
    screen.blit(background, (0,0))

    # no transparency
    ship1 = pygame.image.load("img/blue_ship.png").convert()
    screen.blit(ship1, (40, 100))
    drawText(screen, 'No transparency', 1, 50)

    # transparent background with convert_alpha()
    ship2 = pygame.image.load("img/blue_ship.png").convert_alpha()
    screen.blit(ship2, (240, 100))
    drawText(screen, 'convert_alpha()', 200, 50)

    # transparent background with set_keycolor(BLACK)
    ship3 = pygame.image.load("img/blue_ship.png").convert()
    ship3.set_colorkey(BLACK)
    screen.blit(ship3, (440, 100))
    drawText(screen, 'set_colorkey()', 410, 50)

    # transparent image
    ship4 = pygame.image.load("img/blue_ship.png").convert()
    ship4.set_alpha(50)
    screen.blit(ship4, (640, 100))
    drawText(screen, 'set_alpha(50)', 630, 50)

    # load sound fx
    laser_sound = pygame.mixer.Sound('audio/laser.ogg')

    # load background music
    pygame.mixer.music.load('audio/Tetris.ogg')
    pygame.mixer.music.set_endevent(USEREVENT)
    pygame.mixer.music.play()

    while True:  # <--- main game loop
        for event in pygame.event.get():

            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == MOUSEBUTTONDOWN:
                buttons = pygame.mouse.get_pressed()

                if buttons[0]:
                    laser_sound.play()

            if event.type == USEREVENT:
                pygame.mixer.music.play()

        pygame.display.update()
        fpsClock.tick(FPS)

def drawText(screen, text, x, y):
    WHITE = pygame.Color(255, 255, 255)

    font = pygame.font.SysFont('Calibri', 25, True, False)
    rendered = font.render(text, True, WHITE)
    screen.blit(rendered, [x, y])

if __name__ == "__main__":
    main()
import pygame
import sys
import random
from pygame.locals import *

def main():
    pygame.init()

    NUM_SNOWFLAKES = 100

    FPS = 30
    FPS_CLOCK = pygame.time.Clock()

    BLACK = pygame.Color(0, 0, 0)

    window_size = (0, 0)
    screen = pygame.display.set_mode(window_size)

    pygame.display.set_caption("Falling Snow")

    snow_list = gen_snow_list(NUM_SNOWFLAKES)

    while True:  # <--- main game loop
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(BLACK)

        # process each snowflake in the list
        for snowflake in snow_list:
            snowflake.draw(screen)

            # move the snowflake
            snowflake.fall()

            # if the snowflake moved off the bottom of the screen
            if snowflake.y > pygame.display.Info().current_h:
                snowflake.reset()

        pygame.display.update()  # update the display when all events have been processed
        FPS_CLOCK.tick(FPS)

def gen_snow_list(num):
    """Returns a list of snow objects"""

    snow_list = []

    screen_width = pygame.display.Info().current_w
    screen_height = pygame.display.Info().current_h

    for x in range(num):
        rand_x = random.randint(0, screen_width)
        rand_y = random.randint(0, screen_height)
        rand_size = random.randint(2, 10)
        rand_speed = random.randint(1, 5)

        snow_list.append(Snow(rand_x, rand_y, rand_size, rand_speed))

    return snow_list

class Snow:
    def __init__(self, x, y, size, speed):
        self.x = x
        self.y = y
        self.size = size
        self.speed = speed

    def fall(self):
        self.y += self.speed

    def draw(self, screen):
        pygame.draw.circle(screen, pygame.Color(255, 255, 255), [self.x, self.y], self.size)

    # used when the snowflake reaches the end of the screen
    def reset(self):
        self.x = random.randint(0, pygame.display.Info().current_w)
        self.y = -10

if __name__ == "__main__":
    main()

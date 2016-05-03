import pygame
import sys
from pygame.locals import *

def main():

    pygame.init()

    FPS = 30
    fpsClock = pygame.time.Clock()

    WHITE = pygame.Color(255, 255, 255)

    # Code to create the initial window
    window_size = (500, 500)
    SCREEN = pygame.display.set_mode(window_size)

    # set the title of the window
    pygame.display.set_caption("Bouncing Ball Animation")

    # change the initial background color to white
    SCREEN.fill(WHITE)

    b1 = Ball(0, 0, 3, 5)

    b1.draw(SCREEN)

    while True:  # <--- main game loop
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        SCREEN.fill(WHITE)
        b1.move(SCREEN)
        b1.draw(SCREEN)

        pygame.display.update()
        fpsClock.tick(FPS)

# derive your class from the Sprite super class
class Ball(pygame.sprite.Sprite):
    def __init__(self, x, y, vx, vy):
        # Don't forget to call the super constructor
        super().__init__();
        self.image = pygame.image.load("pokeball.png").convert_alpha()

        # Set the color that should be transparent
        # self.image.set_colorkey(pygame.Color(0, 0, 0))

        # Required for collision detection
        # HINT: You will need this for the lab
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y
        self.vx = vx
        self.vy = vy

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.rect.x, self.rect.y))

    def move(self, SCREEN):
        r_collide = self.rect.x + self.image.get_width() + self.vx > SCREEN.get_width()
        l_collide = self.rect.x + self.vx < 0
        t_collide = self.rect.y + self.vy < 0
        b_collide = self.rect.y + self.image.get_height() + self.vy > SCREEN.get_height()

        # Check collision on right and left sides of screen
        if l_collide or r_collide:
            self.vx *= -1

        # Check collision on top and bottom sides of screen
        if t_collide or b_collide:
            self.vy *= -1

        self.rect.x += self.vx
        self.rect.y += self.vy

if __name__ == "__main__":
    main()
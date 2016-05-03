import pygame
import sys
from pygame.locals import *

def main():

    pygame.init()

    FPS = 30
    fpsClock = pygame.time.Clock()

    WHITE = pygame.Color(255, 255, 255)

    windowSize = (500, 500)
    screen = pygame.display.set_mode(windowSize)

    pygame.display.set_caption("Simple Collision Detection")

    screen.fill(WHITE)

    pokeball = Ball(0, 0, 3, 5)
    pokeball.draw(screen)

    while True:  # <--- main game loop
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(WHITE)
        pokeball.move(screen)
        pokeball.draw(screen)

        pygame.display.update()
        fpsClock.tick(FPS)

# derive your class from the Sprite super class
class Ball(pygame.sprite.Sprite):

    def __init__(self, x, y, vx, vy):

        # don't forget to call the super constructor
        super().__init__();

        self.image = pygame.image.load("pokeball.png").convert_alpha()

        # required for collision detection
        self.rect = self.image.get_rect() # gets the bounding rectangle

        self.rect.x = x
        self.rect.y = y
        self.vx = vx
        self.vy = vy

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def move(self, screen):
        tCollide = self.rect.y + self.vy < 0
        bCollide = self.rect.y + self.image.get_height() + self.vy > screen.get_height()
        rCollide = self.rect.x + self.image.get_width() + self.vx > screen.get_width()
        lCollide = self.rect.x + self.vx < 0

        # check collision on top and bottom sides of screen
        if tCollide or bCollide:
            self.vy *= -1

        # check collision on right and left sides of screen
        if lCollide or rCollide:
            self.vx *= -1

        self.rect.x += self.vx
        self.rect.y += self.vy

if __name__ == "__main__":
    main()
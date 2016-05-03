import pygame
from pygame.locals import *
import random
import sys

def main():
    pygame.init()

    RED = pygame.Color(255, 0, 0)

    screen_size = (0, 0)
    screen = pygame.display.set_mode(screen_size)

    clock = pygame.time.Clock()
    FPS = 60

    # create the sprite lists
    block_list = pygame.sprite.Group()
    all_sprites_list = pygame.sprite.Group()

    generate_sprites(block_list, all_sprites_list, pygame.display.Info().current_w, pygame.display.Info().current_h, 50)

    # create the player
    player = Player()
    all_sprites_list.add(player)

    score = 0

    pygame.mouse.set_visible(False)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(RED)

        # get the current mouse position
        pos = pygame.mouse.get_pos()

        # set the player object to the mouse location
        player.rect.x = pos[0]
        player.rect.y = pos[1]

        # see if the player block has collided with anything
        blocks_hit_list = pygame.sprite.spritecollide(player, block_list, True)

        # check the list of collisions
        for block in blocks_hit_list:
            score += 1
            print(score)

        # call the update() method for all blocks in the block_list
        block_list.update()

        # draw all the spites
        all_sprites_list.draw(screen)

        # update the screen with what we've drawn
        pygame.display.flip()

        clock.tick(60)

def generate_sprites(block_list, all_sprites_list, screen_w, screen_h, num):

    for i in range(num):
        if i % 2 == 0:
            block = Block(Color(0,0,0), 20, 15)
            block.rect.x = random.randrange(screen_w)
            block.rect.y = random.randrange(screen_h)
            block_list.add(block)
            all_sprites_list.add(block)
        else:
            circle = MyCircle(Color(0,0,255), 20)
            circle.rect.x = random.randrange(screen_w)
            circle.rect.y = random.randrange(screen_h)
            block_list.add(circle)
            all_sprites_list.add(circle)

class Player(pygame.sprite.Sprite):

    def __init__(self):
        # call the parent class (Sprite) constructor
        super().__init__()

        # create the image
        self.image = pygame.image.load('creeper.png').convert()

        # set the bounding box
        self.rect = self.image.get_rect()

class MyCircle(pygame.sprite.Sprite):

    def __init__(self, color, radius):
        # call the parent class (Sprite) constructor
        super().__init__()

        # create the image
        self.image = pygame.Surface([radius * 2, radius * 2])
        self.image.fill(pygame.Color(255, 255, 255))
        self.image.set_colorkey(pygame.Color(255,255,255))

        # draw the circle in the image (which is also a Surface)
        pygame.draw.circle(self.image, color, [radius, radius], radius)

        # set the bounding box
        self.rect = self.image.get_rect()

    def update(self):
        """ Called each frame. """

        # move block down one pixel
        self.rect.y += 1

class Block(pygame.sprite.Sprite):

    def __init__(self, color, width, height):
        # call the parent class (Sprite) constructor
        super().__init__()

        # create an image of the block, and fill it with a color
        # this could also be an image loaded from the disk
        self.image = pygame.Surface([width, height])
        self.image.fill(color)

        # fetch the rectangle object that has the dimensions of the image
        # update the position of this object by setting the values of rect.x and rect.y
        self.rect = self.image.get_rect()

    def update(self):
        """ Called each frame. """

        # move block down one pixel
        self.rect.y += 1

if __name__ == '__main__':
    main()
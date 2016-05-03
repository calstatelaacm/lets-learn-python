import pygame
import sys
from pygame.locals import *

def main():
    pygame.init()

    FPS = 30
    FPS_CLOCK = pygame.time.Clock()

    WHITE = pygame.Color(255, 255, 255)

    window_size = (700, 600)
    screen = pygame.display.set_mode(window_size)
    pygame.display.set_caption("Mouse Tracker")
    screen.fill(WHITE)

    movement = (0, 0)
    button_clicked = "no"

    while True:  # <--- main game loop
        screen.fill(WHITE)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == MOUSEBUTTONDOWN:
                # get the state(s) of the mouse buttons
                button_pressed = pygame.mouse.get_pressed()
                # `buttons` contains (1, 0, 0) for left click, (0, 1, 0) for middle click, and (0, 0, 1) for right click

                movement = pygame.mouse.get_rel() # get x & y coordinate since the previous call to this function

                if button_pressed[0]: # left click
                    button_clicked = "left"
                if button_pressed[1]: # middle click
                    button_clicked = "middle"
                if button_pressed[2]: # right click
                    # if the mouse is visible, make it invisible & vice versa
                    pygame.mouse.set_visible(not pygame.mouse.set_visible(0))
                    button_clicked = "right"

            if event.type == MOUSEMOTION:
                mouse_coords = pygame.mouse.get_pos()
                print(mouse_coords)

        update_mouse_coords(screen, mouse_coords)
        update_click_data(screen, movement, button_clicked)
        pygame.display.update()
        FPS_CLOCK.tick(FPS)

def update_mouse_coords(screen, coords):
    x_text = "x = " + str(coords[0])
    y_text = "y = " + str(coords[1])

    font = pygame.font.SysFont("Consolas", 20, False, False)
    text_to_draw1 = font.render(x_text, True, Color(0,0,0))
    text_to_draw2 = font.render(y_text, True, Color(0,0,0))
    screen.blit(text_to_draw1, (50, 50))
    screen.blit(text_to_draw2, (50, 75))

def update_click_data(screen, movement, mouse_button):
    text = "Distance moved since last button click:"
    x_text = "x click = " + str(movement[0])
    y_text = "y click = " + str(movement[1])
    button_text = mouse_button + " button clicked"

    font = pygame.font.SysFont("Consolas", 20, False, False)
    text_to_draw = font.render(text, True, Color(0, 0, 0))
    text_to_draw1 = font.render(x_text, True, Color(0,0,0))
    text_to_draw2 = font.render(y_text, True, Color(0,0,0))
    text_to_draw3 = font.render(button_text, True, Color(0, 0, 0))
    screen.blit(text_to_draw, (50, 125))
    screen.blit(text_to_draw1, (50, 150))
    screen.blit(text_to_draw2, (50, 175))
    screen.blit(text_to_draw3, (50, 200))

if __name__ == "__main__":
    main()
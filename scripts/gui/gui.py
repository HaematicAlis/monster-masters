import pygame
import sys
window_open = True
height = 144
width = 256


def display_init(height, width):
    display_dim = (height, width)
    display = pygame.display.set_mode(display_dim)
    return display

display = display_init(height, width)
while window_open == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            window_open = False
    pygame.display.flip()





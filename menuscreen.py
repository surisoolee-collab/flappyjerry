import pygame, sys  #GF: imports pygame and sys (pygame is used for creating games and multimedia applications, sys provides access to system-specific parameters and functions, such as exiting the program)
import font #GF: imports font module for text rendering

pygame.init() #GF: Initializes all imported pygame modules

screen = pygame.display.set_mode((420, 420)) #GF: Sets the display mode to a window of size 420x420 pixels
pygame.display.set_caption("Flappy Jerry") #GF: Sets the title of the window to "Flappy Jerry"
import pygame # imports the pygame module for game development
pygame.init() # initializes all imported pygame modules
from sys import exit # imports the exit function from the sys module
from random import * # Imports all functions, classes, or variables from the random module

screen = pygame.display.set_mode((800, 600)) # set up display window of size 420x420 pixels
pygame.display.set_caption("Flappy Jerry") # sets the window title to "Flappy Jerry"


jerry_alive = pygame.image.load("jerry.png").convert_alpha
jerry_x = 400
jerry_y = 300
jerry_position = jerry_alive.get_rect(center = (jerry_x, jerry_y)) # sets the initial position of Jerry

def spacebar():
    jerry_y -= 30 # moves Jerry up by 30 pixels
    """Move bird up in response to clicking spacebar."""

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            spacebar() # calls the spacebar function to move Jerry up
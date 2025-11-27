# SYL: Soo Young Lee
# GF: Gabriella Ferry
# GU: Gulyar Udun
"""Flappy Jerry, game inspired by Flappy Bird.
"""
 
import pygame # imports the pygame module for game development
from sys import exit # imports the exit function from the sys module
from random import * # Imports all functions, classes, or variables from the random module

pygame.init() # initializes all imported pygame modules

#Sceen setup
screen = pygame.display.set_mode((900, 700))
pygame.display.set_caption("Flappy Jerry") # sets the window title to "Flappy Jerry"
clock = pygame.time.Clock()

#Import images
jerry_alive = pygame.image.load("images/jerry.png").convert_alpha()
jerry_alive = pygame.transform.scale(jerry_alive, (45, 45))

jerry_dead = pygame.image.load("images/deadjerry.png").convert_alpha()
jerry_dead = pygame.transform.scale(jerry_dead, (45, 45))

mousetrap = pygame.image.load("images/mousetrap.png").convert_alpha()
mousetrap = pygame.transform.scale(mousetrap, (50, 50))

cat = pygame.image.load("images/cat.png").convert_alpha()
cat = pygame.transform.scale(cat, (55, 55))

cheese = pygame.image.load("images/cheese.png").convert_alpha()
cheese = pygame.transform.scale(cheese, (45, 45))

background = pygame.image.load("images/background.png").convert_alpha()
background = pygame.transform.scale(background, (900, 700))

# Jerry setup
jerry = jerry_alive.get_rect(center=(450, 350))

# Obstacle setup
mousetrap_obstacle = [] #empty list that will later store the obstacles
trap_speed = 5 # speed of the mousetrap obstacles
gravity = 3 # gravity that pulls Jerry down

def spacebar(): 
    """
    Move jerry up in response to clicking spacebar.
    """
    jerry.y -= 30 

def spawn_mousetrap():
    """
    Spawn a new mousetrap obstacle at a random y-coordinate.
    """
    y = randrange(10, 550) # random y-coordinate for the new mousetrap (between 10 and 550)
    trap = mousetrap.get_rect(midleft = (900, y)) # creates a new mousetrap at the far right (x=799) with the random y-coordinate
    mousetrap_obstacle.append(trap) # adds the new mousetrap to the list mousetrap_obstacle
    

def check_dead(point): 
    """
    Return True if dead.
    """
    #Hit top or bottom of screen
    if point.top <= 0 or point.bottom >= 700:
        return True
    
    #Hit mousetrap
    for mousetrap in mousetrap_obstacle:
        if jerry.colliderect(mousetrap): # checks for collision between Jerry and the mousetrap
            return True
    else:
        return False

running = True
while running:
    screen.blit(background, (0, 0)) # fills the screen with a sky blue color

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            spacebar() # calls the spacebar function to move Jerry up

    jerry.y += gravity # makes Jerry move down by 5 units (gravity)

    if randrange(23) == 0: #randrange method will rturn a number between 0 and 21 if it is 0 spawn a mousetrap
        spawn_mousetrap() 

    #Move mousetraps
    for trap in mousetrap_obstacle:
        trap.x -= trap_speed # moves every mousetrap by mousetrap_speed units left each time the loop runs
        screen.blit(mousetrap, trap) # draws the mousetrap on the screen at its current position
        
        if trap.right < 0: # if the mousetrap has moved off the left side of the screen
            mousetrap_obstacle.remove(trap) # remove and return the first mousetrap from the list
        
    #Draw Jerry
    screen.blit(jerry_alive, jerry)

    #Check if jerry is dead
    if check_dead(jerry):
        screen.blit(jerry_dead, jerry)
        pygame.display.update()
        pygame.time.delay(4000)
        pygame.quit()
        exit()
        
    pygame.display.update()  # updates the contents of the entire display
    clock.tick(30)  # limits the frame rate to 30 frames per second

# SYL: Soo Young Lee
# GF: Gabriella Ferry
# GU: Gulyar Udun
"""Flappy, game inspired by Flappy Bird.
"""

import pygame # imports the pygame module for game development
pygame.init() # initializes all imported pygame modules
from sys import exit # imports the exit function from the sys module
from random import * # Imports all functions, classes, or variables from the random module

screen = pygame.display.set_mode((420, 420)) # set up display window of size 420x420 pixels
pygame.display.set_caption("Flappy Jerry") # sets the window title to "Flappy Jerry"

clock = pygame.time.Clock() # creates a Clock object to help track time

#Import images
jerry = pygame.image.load("jerry.png").convert_alpha
deadjerry = pygame.image.load("deadjerry.png").convert_alpha
cat = pygame.image.load("cat.png").convert_alpha
mousetrap = pygame.image.load("mousetrap.png").convert_alpha
cheese = pygame.image.load("cheese.png").convert_alpha
background = pygame.image.load("background.png").convert_alpha

#Initialize jerry position
jerry_x = 210
jerry_y = 210
jerry_position = jerry_alive.get_rect(center = (jerry_x, jerry_y)) # sets the initial position of Jerry

mousetrap_obstacle = [] #empty list that will later store the obstacles


def spacebar():
    jerry_y -= 30 # moves Jerry up by 30 pixels
    """Move bird up in response to clicking spacebar."""

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
    key = pygame.key.get_pressed() # checks if the spacebar key is pressed
        if key[pygame.K_SPACE]:
            spacebar() # calls the spacebar function to move Jerry up
        else:
            


def inside(point): #GF: Defines the function "inside" that checks if a point is within the screen boundaries.
    """Return True if point on screen."""
    return -200 < point.x < 200 and -200 < point.y < 200 #GF: If True, the point's x and y coordinates are within the screen boundaries (between -200 and 200).


def draw(alive): #GF: This function is responsible for rendering the game objects on the screen.
    """Draw screen objects."""
    clear() #GF: This function clears the screen to prepare for new drawings.

    goto(bird.x, bird.y) #GF: Moves the turtle to the bird's current position.

    if alive: #GF: If the bird is alive, it draws a green dot. Otherwise, it draws a red dot. The dot is 10 pixels wide.
        dot(10, 'green')
    else:
        dot(10, 'red')

    for ball in balls: #GF: Draws each ball (obstacle) on the screen at the given x,y coordinates as a black dot that is 20 pixels wide.
        goto(ball.x, ball.y)
        dot(20, 'black')

    update() #GF: This function updates the screen to show the newly drawn objects.


def move(): #SYL: defines main game loop. Updates positions of bird and balls, checks for losing conditions, and redraws the screen.
    """Update object positions."""
    bird.y -= 5 #SYL: makes the bird move down by 5 units in the y-coordinate 

    for ball in balls: #SYL: moves every ball by 3 units left each time the function is called
        ball.x -= 3

    if randrange(10) == 0: #SYL: randrange method will return number between 0 to 9 and if it returns 0 (10% channce), a new ball will be created
        y = randrange(-199, 199) #SYL: a random y-coordinate for the new ball (between -199 and 199)
        ball = vector(199, y) #SYL: creates a new ball at the far right (x=199) with the random y-coordinate
        balls.append(ball) #SYL: adds the new ball to the list balls

    while len(balls) > 0 and not inside(balls[0]): #SYl: while there are balls in the list and the first ball is not inside the screen
        balls.pop(0) #SYL: remove and return the first ball from the list
    if not inside(bird): #GU: Checks whether the bird is still on the game screen
        draw(False) #GU: If bird is outside of the game screen then function will return False and the game will end.
        return

    for ball in balls: #GU: Checks every ball in this list of random balls(obstacles)
        if abs(ball - bird) < 15: #GU: Calculates the absolute value of the distance betweent the bird and a ball, and checks if the distance is less than 15 units
            draw(False) #GU: If distance is less than 15 units then function will return False and game will end.
            return

    draw(True) #GU: If distance is more than 15 units then it tells the game that the bird has not collided into anything
    ontimer(move, 50) #GU: When the bird is safe the game will continue by updating the game screen every 50 milliseconds(creates the illusion that the bird is moving horizontally.)



onscreenclick(spacebar) #SYL: calls the spacebar function whenever the screen is clicked
move() #SYL: starts the game by calling the move function
done() #SYL: when the program is finished waits for the user to close the window

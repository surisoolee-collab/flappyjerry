# SYL: Soo Young Lee
# GF: Gabriella Ferry
# GU: Gulyar Udun
"""Flappy, game inspired by Flappy Bird.
"""

import pygame # imports the pygame module for game development
from sys import exit # imports th exit function from the sys module
from random import * # Imports all functions, classes, or variables from the random module

pygame.display.set_caption("Flappy Jerry") # sets the window title to "Flappy Jerry"
jerry_alive = pygame.image.load("jerry_alive.png").convert_alpha # loads the image of Jerry when he is alive
jerry_dead = pygame.image.load("jerry_dead.png").convert_alpha # loads the image of Jerry when he is dead

jerry_alive = vector(0, 0) #SYL: Initializes bird position at the center of the screen at position (0,0)
balls = [] #GU: creates an empty list that will later store the obstacles (balls) 


def tap(x, y):
    """Move bird up in response to screen tap.""" #GU: 
    up = vector(0, 30)
    bird.move(up)


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
    if not inside(bird): #GU:
        draw(False)
        return

    for ball in balls:
        if abs(ball - bird) < 15:
            draw(False)
            return

    draw(True)
    ontimer(move, 50)


setup(420, 420, 370, 0) #SYL: creates a 420 by 420 pixel window, at 370 pixels left and 0 pixels from the top of the screen
hideturtle() #SYL: hides the default turtle cursor
up() #SYL: lifts the turtle pen up so the turtle moves without drawing lines
tracer(False)
onscreenclick(tap) #SYL: calls the tap function whenever the screen is clicked
move() #SYL: starts the game by calling the move function
done() #SYL: when the program is finished waits for the user to close the window

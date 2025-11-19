# SYL: Soo Young Lee
# GF: Gabriella Ferry
# GU: Gulyar Udun
"""Flappy, game inspired by Flappy Bird.
"""

from random import * #GF: Imports all functions, classes, or variables from the random module
from turtle import * #GF: Imports all turtle functions used to draw graphics on the screen. Such as movement/positioning and shapes

from freegames import vector #SYL: Imports vector from the module freegames, to run the game freegames must be installed

bird = vector(0, 0) #SYL: Initializes bird position at the center of the screen at position (0,0)
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

    goto(bird.x, bird.y)

    if alive:
        dot(10, 'green')
    else:
        dot(10, 'red')

    for ball in balls:
        goto(ball.x, ball.y)
        dot(20, 'black')

    update()


def move(): #SYL:
    """Update object positions."""
    bird.y -= 5

    for ball in balls:
        ball.x -= 3

    if randrange(10) == 0:
        y = randrange(-199, 199)
        ball = vector(199, y)
        balls.append(ball)

    while len(balls) > 0 and not inside(balls[0]):
        balls.pop(0)

    if not inside(bird): #GU:
        draw(False)
        return

    for ball in balls:
        if abs(ball - bird) < 15:
            draw(False)
            return

    draw(True)
    ontimer(move, 50)


setup(420, 420, 370, 0) #SYL:
hideturtle()
up()
tracer(False)
onscreenclick(tap)
move()
done()

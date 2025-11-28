# SYL: Soo Young Lee
# GF: Gabriella Ferry
# GU: Gulyar Udun
"""Flappy Jerry, game inspired by Flappy Bird.
"""
 
import pygame # imports the pygame module for game development
from sys import exit # imports the exit function from the sys module
from random import * # Imports all functions, classes, or variables from the random module
import menuscreen # imports the menuscreen module

pygame.init() # initializes all imported pygame modules

def play_game(highscore):
    """
    Main game function to run Flappy Jerry.
    """
    #Sceen setup
    screen = pygame.display.set_mode((900, 700))
    pygame.display.set_caption("Flappy Jerry") # sets the window title to "Flappy Jerry"
    clock = pygame.time.Clock()

    menuscreen.run_menu(screen, 0) # runs the menu screen function from the menuscreen module

    #Import images
    jerry_alive = pygame.image.load("images/jerry.png").convert_alpha()
    jerry_alive = pygame.transform.scale(jerry_alive, (45, 45))

    jerry_dead = pygame.image.load("images/deadjerry.png").convert_alpha()
    jerry_dead = pygame.transform.scale(jerry_dead, (45, 45))

    mousetrap = pygame.image.load("images/mousetrap.png").convert_alpha()
    mousetrap = pygame.transform.scale(mousetrap, (50, 50))

    tom = pygame.image.load("images/cat.png").convert_alpha()
    tom = pygame.transform.scale(tom, (60, 60))

    cheese_image = pygame.image.load("images/cheese.png").convert_alpha()
    cheese_image = pygame.transform.scale(cheese_image, (45, 45))

    background = pygame.image.load("images/background.png").convert_alpha()
    background = pygame.transform.scale(background, (900, 700))

    # Jerry setup
    jerry = jerry_alive.get_rect(center=(450, 350))
    gravity = 5 # gravity that pulls Jerry down

    # Obstacle setup
    mousetrap_obstacle = [] #empty list that will later store the obstacles
    trap_speed = 5 # speed of the mousetrap obstacles

    # Cheese setup
    cheese_points = []  # empty list that will later store the cheeses
    cheese_speed = 5 # speed of the cheese points (same as mousetrap speed)

    # Cat setup
    tom_obstacle = [] # empty list that will later store the cat obstacles
    tom_speed = 8 # speed of the cat obstacles

    def spacebar(): 
        """
        Move jerry up in response to clicking spacebar.
        """
        jerry.y -= 50 

    def spawn_mousetrap():
        """
        Spawn a new mousetrap obstacle at a random y-coordinate.
        """
        y = randrange(10, 650) # random y-coordinate for the new mousetrap (between 10 and 550)
        trap = mousetrap.get_rect(midleft = (900, y)) # creates a new mousetrap at the far right (x=799) with the random y-coordinate
        mousetrap_obstacle.append(trap) # adds the new mousetrap to the list mousetrap_obstacle
    
    def spawn_cheeses():
        """
        Spawn a cheese at a random y-coordinate.
        """
        y = randrange(10, 650) # random y-coordinate for the new cheese (between 10 and 550)
        cheese = cheese_image.get_rect(midleft = (900, y)) # creates a new cheese at the far right (x=799) with the random y-coordinate
        cheese_points.append(cheese) # adds the new cheese to the list cheese_points

    def spawn_tom():
        """
        Spawn a cat obstacle at a random y-coordinate.
        """
        y = randrange(30, 630) # random y-coordinate for the new cat (between 10 and 550)
        cat = tom.get_rect(midleft = (900, y)) # creates a new cat at the far right (x=799) with the random y-coordinate
        tom_obstacle.append(cat) # adds the new cat to the list cat_obstacle

    def check_dead(point): 
        """
        Return True if dead.
        """
        #Hit top or bottom of screen
        if point.top <= 0 or point.bottom >= 700:
            return True
    
        #Hit mousetrap
        for mousetrap in mousetrap_obstacle:
            if point.colliderect(mousetrap): # checks for collision between Jerry and the mousetrap
                return True

        for tom in tom_obstacle:
            if point.colliderect(tom):
                return True
    
        return False
    
    def get_points(jerry, cheese_points, score):
        """
        Return True if jerry gets cheese.
        """
        for cheese in cheese_points[:]: 
            if jerry.colliderect(cheese): # checks for collision between Jerry and the cheese
                score += 1 # increase score by 1
                cheese_points.remove(cheese) # remove the cheese that was collected from the list
                return True, score
        return False, score

    font = pygame.font.SysFont("Cooper Black", 50) 
    score = 0

    running = True
    while running:
    
        screen.blit(background, (0, 0)) # draws the background image

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                spacebar() # calls the spacebar function to move Jerry up

        jerry.y += gravity # makes Jerry move down by 5 units (gravity)

        if randrange(25) == 0: #randrange method will return a number between 0 and 21 if it is 0 spawn a mousetrap
            spawn_mousetrap() 

        if randrange(45) == 0:
            spawn_cheeses()

        if randrange(80) == 0:
            spawn_tom()

        #Move mousetraps
        for trap in mousetrap_obstacle:
            trap.x -= trap_speed # moves every mousetrap by mousetrap_speed units left each time the loop runs
            screen.blit(mousetrap, trap) # draws the mousetrap on the screen at its current position
        
            if trap.right < 0: # if the mousetrap has moved off the left side of the screen
                mousetrap_obstacle.remove(trap) # remove and return the first mousetrap from the list

        for cat in tom_obstacle:
            cat.x -= tom_speed
            screen.blit(tom, cat)

            if cat.right < 0:
                tom_obstacle.remove(cat)

        for cheese in cheese_points:
            cheese.x -= cheese_speed
            screen.blit(cheese_image, cheese)
    
            if cheese.right < 0:
                cheese_points.remove(cheese)
    
        got_cheese, score = get_points(jerry, cheese_points, score)

        #updates the highscore depending on what the highest score achieved is
        if score > highscore:
            highscore = score

        score_text = font.render(f"Score: {score}", True, (255, 255, 255))

        screen.blit(score_text, (10,10))

        highscore_text = font.render(f"Highscore: {highscore}", True, (255, 255, 0))

        screen.blit(highscore_text, (480, 10))
        
        #Draw Jerry
        dead = check_dead(jerry) # dead = True if Jerry is dead, False otherwise
        if dead:
            screen.blit(jerry_dead, jerry)
            pygame.display.update()
            pygame.time.delay(1000)
            
            return highscore  # exit the game loop and return the highscore to main.py
        else:
            screen.blit(jerry_alive, jerry)

        pygame.display.update()  # updates the contents of the entire display
        clock.tick(30)  # limits the frame rate to 30 frames per second
    
    return highscore

def main():
    """
    Main function to start and restart the game.
    """
    highscore = 0

    while True:
        menuscreen.run_menu(pygame.display.set_mode((900, 700)), highscore)  # shows the menu screen with the updated highscore
        highscore = play_game(highscore)  # starts the game and updates the highscore after each game over

if __name__ == "__main__":
    main()
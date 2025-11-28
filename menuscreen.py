import pygame 
import sys
import buttons
#import buttons later

pygame.init()  # initializes all imported pygame modules

#SCREEN = pygame.display.set_mode((800, 600))  # sets the display window size to 400 pixels wide and 600 pixels high
#pygame.display.set_caption("Flappy Jerry Menu")  # sets the window title to "Flappy Jerry Menu"

#define variables
game_paused = True

font = pygame.font.SysFont("04b 30", 70)
text_color = (255, 255, 255)

#load button images
start_button_image = pygame.image.load('start button.png').convert_alpha()
quit_button_image = pygame.image.load('images/quit button.png').convert_alpha()
#button instances
start_button = buttons.Button(400, 275, start_button_image, 0.3)
quit_button = buttons.Button(400, 425, quit_button_image, 0.3)

def draw_text(text, font, color, surface, x, y):
    img = font.render(text, True, color) # renders the text into an image
    SCREEN.blit(img, (x, y)) # draws the text image onto the screen at position (x, y)

#game loop starts here
run = True  # boolean variable to control the main loop
while run:
    SCREEN.fill((222,184,135))  # fills the screen with a sky blue color (RGB: 135, 206, 235)

    #check if the game is paused
    if game_paused == True:
        draw_text('Flappy Jerry', font, text_color, SCREEN, 60, 100)  # draws the title text on the screen
        if start_button.draw(SCREEN):  # draws the start button on the screen
            game_paused = False  # exits the paused state when the start button is clicked
        if quit_button.draw(SCREEN):  # draws the quit button on the screen
            event.type = pygame.QUIT  # sets the event type to QUIT to exit the game
    for event in pygame.event.get():  # iterates through the list of events that have occurred
        if event.type == pygame.KEYDOWN:  # checks if a key has been pressed down
            if event.key == pygame.K_ESCAPE:  # checks if the pressed key is the spacebar
                game_paused = True  # sets run to False to exit the main loop
        if event.type == pygame.QUIT:
            run = False  # checks if the event type is QUIT (e.g., closing the window)
            pygame.quit()  # uninitializes all pygame modules
            sys.exit()  # exits the program 

    pygame.display.update()  # updates the contents of the entire display

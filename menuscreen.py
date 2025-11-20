import pygame 

pygame.init()  # initializes all imported pygame modules

SCREEN = pygame.display.set_mode((200, 200))  # sets the display window size to 400 pixels wide and 600 pixels high
pygame.display.set_caption("Flappy Jerry")  # sets the window title to "Flappy Jerry"

'''
def draw_text(text, font, color, surface, x, y):
    img = font.render(text, True, color)
    screen.blit(img, (x, y))
'''
#game loop starts here
run = True  # boolean variable to control the main loop
while run:
    SCREEN.fill((135, 206, 235))  # fills the screen with a sky blue color (RGB: 135, 206, 235)

    for event in pygame.event.get():  # iterates through the list of events that have occurred
        if event.type == pygame.QUIT:  # checks if the event type is QUIT (e.g., closing the window)
            pygame.quit()  # uninitializes all pygame modules
            sys.exit()  # exits the program

    pygame.display.update()  # updates the contents of the entire display

import pygame 
import sys
import buttons

pygame.init()  # initializes all imported pygame modules

def run_menu():
    SCREEN = pygame.display.set_mode((900, 700))
    pygame.display.set_caption("Flappy Jerry Menu")

    font = pygame.font.SysFont("04b 30", 70)
    text_color = (255, 255, 255)
    game_paused = True

    # load button images
    start_button_image = pygame.image.load('images/start button.png').convert_alpha()
    quit_button_image  = pygame.image.load('images/quit button.png').convert_alpha()

    # button instances
    start_button = buttons.Button(450, 275, start_button_image, 0.3)
    quit_button  = buttons.Button(450, 425, quit_button_image, 0.3)

    def draw_text(text, font, color, surface, x, y):
        img = font.render(text, True, color)
        SCREEN.blit(img, (x, y))

    # Menu loop
    run = True
    while run:
        SCREEN.fill((222, 184, 135))

        if game_paused:

            # Title text
            draw_text('Flappy Jerry', font, text_color, SCREEN, 100, 100)

            # START button clicked → return to main game
            if start_button.draw(SCREEN):
                return # return to main.py to start the game

            # QUIT button clicked → exit whole program
            if quit_button.draw(SCREEN):
                pygame.quit()
                sys.exit()

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()

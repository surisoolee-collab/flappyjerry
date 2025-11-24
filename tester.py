import pygame
from sys import exit
from random import randrange

pygame.init()

# Screen setup
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Flappy Jerry")
clock = pygame.time.Clock()

# Load images
jerry_alive = pygame.image.load("jerry.png").convert_alpha()
jerry_alive = pygame.transform.scale(jerry_alive, (50, 50))

jerry_dead = pygame.image.load("deadjerry.png").convert_alpha()
jerry_dead = pygame.transform.scale(jerry_dead, (50, 50))

mousetrap_img = pygame.image.load("mousetrap.png").convert_alpha()
mousetrap_img = pygame.transform.scale(mousetrap_img, (50, 50))

# Jerry setup
jerry = jerry_alive.get_rect(center=(400, 300))
gravity = 5

# Obstacle setup
mousetraps = []
mousetrap_speed = 4

def jump():
    """Make Jerry move up."""
    jerry.y -= 35

def spawn_mousetrap():
    y = randrange(10, SCREEN_HEIGHT - 10)
    trap = mousetrap_img.get_rect(midleft=(SCREEN_WIDTH, y))
    mousetraps.append(trap)

def check_dead():
    """Check if Jerry is dead (hits screen or mousetrap)."""
    if jerry.top < 0 or jerry.bottom > SCREEN_HEIGHT:
        return True

    for trap in mousetraps:
        if jerry.colliderect(trap):
            return True

    return False

running = True
while running:
    screen.fill((135, 206, 235))  # Sky color

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            jump()

    # Gravity
    jerry.y += gravity

    # Randomly spawn mousetraps
    if randrange(20) == 0:
        spawn_mousetrap()

    # Move and draw mousetraps
    for trap in list(mousetraps):
        trap.x -= mousetrap_speed
        screen.blit(mousetrap_img, trap)
        if trap.right < 0:
            mousetraps.remove(trap)

    # Draw Jerry
    screen.blit(jerry_alive, jerry)

    # Check collision
    if check_dead():
        screen.blit(jerry_dead, jerry)
        pygame.display.update()
        pygame.time.wait(1500)
        pygame.quit()
        exit()

    pygame.display.update()
    clock.tick(30)
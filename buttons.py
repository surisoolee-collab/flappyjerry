import pygame

#button images
start_button_image = pygame.image.load('start button.png').convert_alpha()
quit_button_image = pygame.image.load('quit button.png').convert_alpha()

#button class
class Button():
    def __init__(self, x, y, image): # x and y are the top-left coordinates where the button will be placed
        width = image.get_width()
        height = image.get_height()
        self.image = image # store the button image
        self.rect = self.image.get_rect() # get the rectangle object for positioning
        self.rect.topleft = (x, y) # set the top-left position of the button
        self.clicked = False
    
    def draw(self, surface): # draws the button on the given surface
         surface.blit(self.image, (self.rect.x, self.rect.y))
         return self.is_clicked(pygame.mouse.get_pos())

    def draw(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)
import pygame

#button class
class Button():
    def __init__(self, x, y, image, scale): # x and y are the top-left coordinates where the button will be placed
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width*scale), int(height*scale))) # store the button image
        self.rect = self.image.get_rect() # get the rectangle object for positioning
        self.rect.center = (x, y) # set the top-left position of the button
        self.clicked = False
    
    def draw(self, surface): # draws the button on the given surface
        surface.blit(self.image, self.rect)
        action = False
        mouse_position = pygame.mouse.get_pos() # get the current mouse position
        if self.rect.collidepoint(mouse_position): # check if the mouse is over the button
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False: # check if the left mouse button is pressed
                self.clicked = True
                action = True
        if pygame.mouse.get_pressed()[0] == 0: # reset clicked state when mouse button is released
            self.clicked = False

        surface.blit(self.image, (self.rect.x, self.rect.y))

        return action
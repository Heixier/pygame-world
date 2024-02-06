import pygame, sys
import screens.screen as screen

pygame.init()

main_font = pygame.font.SysFont("arial", 50)

class Button():
    def __init__(self, screen_obj, x_pos, y_pos, text_input, image = False):
        self.image = image
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.text_input = text_input
        self.screen = screen_obj
        
        if self.image:
            self.rect = self.image.get_rect(center = (self.x_pos, self.y_pos))
            self.image = pygame.transform.scale(self.image, (400, 150))
        else:
            self.image = pygame.Surface((400, 150))

            self.rect = self.image.get_rect(center = (self.x_pos, self.y_pos))

            self.image.fill("blue")

            
        self.text = main_font.render(self.text_input, True, "white")
        self.text_rect = self.text.get_rect(center = (self.x_pos, self.y_pos))
        print(self.image)
        print(type(self.image))
        
    def update(self):
        self.screen.blit(self.image, self.rect)
        self.screen.blit(self.text, self.text_rect)
    
    def inputcheck(self, position):
        '''Checks if mouse position is within the button's area'''
        if position[0] in range(self.rect.left, self.rect.right) and position [1] in range(self.rect.top, self.rect.bottom):
            print("Success")
        
    def hover(self, position):
        '''Checks if mouse position is within the button's area'''
        if position[0] in range(self.rect.left, self.rect.right) and position [1] in range(self.rect.top, self.rect.bottom):
            self.text = main_font.render(self.text_input, True, "green")
        else:
            self.text = main_font.render(self.text_input, True, "white")
            

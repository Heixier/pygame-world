import pygame, sys

from screens import screen
from elements.buttons import Button

pygame.init()
FONT = pygame.font.SysFont(None, 80)


def view(sc):
    '''Main menu screen'''
    
    pygame.display.set_caption("Main Menu")
    button = Button(sc, screen.MAX_WIDTH / 2, screen.MAX_HEIGHT / 2, "click me")
    
    while True:
        
        # Blit background at coordinates 0, 0
        screen.reset(sc)
        
        TEXT = FONT.render("MAIN MENU", True, "#FFFFFF")
        RECT = TEXT.get_rect(center = (640, 100))
        
        sc.blit(TEXT, RECT)
        
        MENU_MOUSE_POS = pygame.mouse.get_pos()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                button.inputcheck(pygame.mouse.get_pos())
        
        button.update()
        button.hover(pygame.mouse.get_pos())
                
        pygame.display.update()
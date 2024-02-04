import pygame, sys

from screens import screen

pygame.init()
FONT = pygame.font.SysFont(None, 80)

def view(sc):
    '''Main menu screen'''
    pygame.display.set_caption("Main Menu")
    
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
                
        pygame.display.update()
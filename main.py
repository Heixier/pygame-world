import pygame, sys

from screens import screen, options, main_menu, game

pygame.init()

SCREEN = pygame.display.set_mode((screen.MAX_WIDTH, screen.MAX_HEIGHT))



if __name__ == "__main__":
    main_menu.view(SCREEN)
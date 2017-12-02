import pygame


class Menu_screen:
    def __init__(self, width, height, bg_color=(0, 0, 0)):
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.background = pygame.Surface(self.screen.get_size())

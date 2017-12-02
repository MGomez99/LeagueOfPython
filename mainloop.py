import pygame
import player1
import player2
import sys


class Controller:
    def __init__(self,player1_spec, player2_spec,  width=800, height=600):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.background = pygame.Surface(self.screen.get_size())
        self.player1 = player1_spec
        self.player2 = player2_spec

        self.sprites = pygame.sprite.Group((self.player1,) + (self.player2,))

        def mainLoop(self):
            pygame.key.set_repeat(1, 60)
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.Quit:
                        sys.exit()
                self.screen.blit(self.background, (0, 0))
                self.sprites.draw(self.screen)
                pygame.display.flip()


def main():
    gameon = Controller(player1_spec, player2_spec)
    gameon.mainLoop()

main()

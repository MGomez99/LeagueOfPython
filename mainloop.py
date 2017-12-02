import pygame
import player
import projectile
import spec1
import spec2
import spec3
import sys
import menu_screen


class Controller:
    def __init__(self):
        pygame.init()
        self.width = 800
        self.height = 600
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.background = pygame.Surface(self.screen.get_size())
        self.sprites = pygame.sprite.Group((self.player1,) + (self.player2,))
        def menu_screen(self):
            self.background.blit("startmenu.png", (0,0))
            for event in pygame.event.get():
                if event.type==pygame.KEYDOWN:
                    if event.key==K_RETURN:
                        Controller.player1select()
                        break
        def player1select(self):
            self.background.blit("player1menu.png", (0, 0))
            for event in pygame.event.get():
                if event.type==pygame.KEYDOWN:
                    if event.key==K_q:
                        player1=player.player(50,self.height/2,"BLUE",spec1)
                        break
                    elif event.key==K_q:
                        player1=player.player(50,self.height/2,"BLUE",spec2)
                    elif event.key==K_q:
                        player1=player.player(50,self.height/2,"BLUE",spec3)
        def player2select(self):
            self.background.blit("player2menu.png", (0, 0))
        def mainLoop(self):
            #start screen here, press button to go to next
            #player 1 spec select
            #player 2 spec select
            #game
            pygame.key.set_repeat(1, 60)
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.Quit:
                        sys.exit()
                self.screen.blit(self.background, (0, 0))
                self.sprites.draw(self.screen)
                pygame.display.flip()


def main():
    gameon = Controller()
    gameon.menu_screen()

main()

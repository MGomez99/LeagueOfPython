import pygame
import player
import projectile
import spec1
import spec2
import spec3
import sys
import pause_menu


class Controller:
    def __init__(self):
        pygame.init()
        self.width = 800
        self.height = 600
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.background = pygame.Surface(self.screen.get_size())
        self.sprites = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        self.lsbullets = pygame.sprite.Group()
        self.bigassbullets = pygame.sprite.Group()
        self.punyassbullets = pygame.sprite.Group()
        clock = pygame.time.Clock()

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
                    Controller.player2select()
                    break
                elif event.key==K_w:
                    player1=player.player(50,self.height/2,"BLUE",spec2)
                    Controller.player2select()
                    break
                elif event.key==K_e:
                    player1=player.player(50,self.height/2,"BLUE",spec3)
                    Controller.player2select()
                    break

    def player2select(self):
        self.background.blit("player2menu.png", (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == K_u:
                    player2 = player.player(self.width-50, self.height / 2, "RED", spec1)
                    Controller.mainLoop()
                    break
                elif event.key == K_i:
                    player2 = player.player(self.width-50, self.height / 2, "RED", spec2)
                    Controller.mainLoop()
                    break
                elif event.key == K_o:
                    player2 = player.player(self.width-50, self.height / 2, "RED", spec3)
                    Controller.mainLoop()
                    break

    def mainLoop(self):
        pygame.key.set_repeat(1, 60)
        sprites.add(player1)
        sprites.add(player2)
        while True:
            player1.update()
            player2.update()
            if len(bullets.sprites()>0):
                bullet.update() # will need to update for uniques as well
            for event in pygame.event.get():
                if event.type == pygame.Quit:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == K_ESCAPE:
                        pause = True
                        pause_menu.paused()

            self.screen.blit(self.background, (0, 0))
            self.sprites.draw(self.screen)
            pygame.display.flip()


def main():
    gameon = Controller()
    gameon.menu_screen()

main()

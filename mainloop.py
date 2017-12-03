import pygame
import player
import projectile
import spec1
import spec2
import spec3
import sys
import pause_menu
import text_to_screen


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

    def start_menu(self):
        self.background.blit("startmenu.png", (0,0))
        # prompt "press enter to enter select" or something
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == K_RETURN:
                    Controller.player1select()
                    Controller.player2select()
                    break


    def player1select(self):
        self.background.blit("player1menu.png", (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == K_q:
                    player1 = player.player(50,self.height/2,"BLUE",spec1)
                    break
                elif event.key == K_w:
                    player1 = player.player(50,self.height/2,"BLUE",spec2)
                    break
                elif event.key == K_e:
                    player1 = player.player(50,self.height/2,"BLUE",spec3)
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

    def map_select(self):
        self.background.blit("mapselect.png")
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key() == K_q:
                    self.background.blit("mars.png", (0, 0))
                    break
                if event.key() == K_w:
                    self.background.blit("moon.png", (0, 0))
                    break
                if event.key() == K_e:
                    self.background.blit("venus.png", (0, 0))
                    break
        for time in range(-5, 0):
            text = str("Game starting in ", abs(time), ". Get ready!")
            text_to_screen.tts(self.screen, text, (400, 200))
            pygame.time.wait(1000)  # countdown timer pre-game

    def mainLoop(self):
        pygame.key.set_repeat(1, 60)
        self.sprites.add(self.player1)
        self.sprites.add(self.player2)

        while True:
            self.player1.update()
            self.player2.update()
            if len(self.bullets.sprites()>0):
                player.bullet.update()
            if len(self.lsbullets.sprites()>0):
                player.lsbullet.update()
            if len(self.bigassbullets.sprites()>0):
                player.bigassbullet.update()
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
    gameon.start_menu()
    gameon.mainLoop()


main()

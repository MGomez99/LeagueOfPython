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
        self.clock = pygame.time.Clock()

    def start_menu(self):
        self.background.blit("startmenu.png", (0, 0))
        # prompt "press enter to enter select" or something
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == K_RETURN:
                    player1 = Controller.player1select()
                    player2 = Controller.player2select()
                    return player1, player2
                if event.key == K_ESCAPE:
                    sys.exit()

    def player1select(self):
        self.background.blit("player1menu.png", (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == K_q:
                    player1 = player.player(50,self.height/2,"BLUE",spec1)
                    return player1
                elif event.key == K_w:
                    player1 = player.player(50,self.height/2,"BLUE",spec2)
                    return player1
                elif event.key == K_e:
                    player1 = player.player(50,self.height/2,"BLUE",spec3)
                    return player1

    def player2select(self):
        self.background.blit("player2menu.png", (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == K_u:
                    player2 = player.player(self.width-50, self.height / 2, "RED", spec1)
                    return player2
                elif event.key == K_i:
                    player2 = player.player(self.width-50, self.height / 2, "RED", spec2)
                    return player2
                elif event.key == K_o:
                    player2 = player.player(self.width-50, self.height / 2, "RED", spec3)
                    return player2

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

    def mainLoop(self, player1, player2):
        pygame.key.set_repeat(1, 60)
        self.sprites.add(player1)
        self.sprites.add(player2)
        go_to_menu = False
        while True:
            player1.update()
            player2.update()
            if len(self.bullets.sprites() > 0):
                self.bullet.update() # will need to update for uniques as well
            for event in pygame.event.get():
                if event.type == pygame.Quit:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == K_ESCAPE:
                        isPaused = True
                        go_to_menu = pause_menu.paused(self.display, self.clock)

            self.screen.blit(self.background, (0, 0))
            self.sprites.draw(self.screen)
            pygame.display.flip()
            if go_to_menu:
                break


def main():
    game_on = Controller()
    player1, player2 = game_on.start_menu()
    game_on.mainLoop(player1, player2)
    game_on.start_menu()


main()

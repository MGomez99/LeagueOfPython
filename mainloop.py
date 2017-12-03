import pygame
import player
import projectile
import sys
import pause_menu
import text_to_screen
import stats


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
        self.rockets = pygame.sprite.Group()
        self.rapidfirebullets = pygame.sprite.Group()
        self.punyassbullets = pygame.sprite.Group()
        self.allprojectiles = pygame.sprite.Group()

    def start_menu(self):
        self.background.blit("assets\startmenu.png", (0, 0))
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
        self.background.blit("assets\player1menu.png", (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == K_q:
                    player1 = player.Player(50, self.height / 2, "BLUE", "spec1", self.allprojectiles, self.lsbullets, self.bullets, self.rockets, self.rapidfirebullets)
                    return player1
                elif event.key == K_w:
                    player1 = player.Player(50, self.height / 2, "BLUE", "spec2", self.allprojectiles, self.lsbullets, self.bullets, self.rockets, self.rapidfirebullets)
                    return player1
                elif event.key == K_e:
                    player1 = player.Player(50, self.height / 2, "BLUE", "spec3", self.allprojectiles, self.lsbullets, self.bullets, self.rockets, self.rapidfirebullets)
                    return player1

    def player2select(self):
        self.background.blit("assets\player2menu.png", (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == K_u:
                    player2 = player.Player(self.width - 50, self.height / 2, "RED", "spec1", self.allprojectiles, self.lsbullets, self.bullets, self.rockets, self.rapidfirebullets)
                    return player2
                elif event.key == K_i:
                    player2 = player.Player(self.width - 50, self.height / 2, "RED", "spec2", self.allprojectiles, self.lsbullets, self.bullets, self.rockets, self.rapidfirebullets)
                    return player2
                elif event.key == K_o:
                    player2 = player.Player(self.width - 50, self.height / 2, "RED", "spec3", self.allprojectiles, self.lsbullets, self.bullets, self.rockets, self.rapidfirebullets)
                    return player2

    def map_select(self):
        self.background.blit("assets/mapselect.png")
        selecting_map = True
        while selecting_map:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key() == K_q:
                        self.background.blit("assets/mars.png", (0, 0))
                        break
                    if event.key() == K_w:
                        self.background.blit("assets/moon.png", (0, 0))
                        break
                    if event.key() == K_e:
                        self.background.blit("assets/venus.png", (0, 0))
                        break
        for time in range(-5, 0):
            text = "Game starting in "+str(abs(time), ". Get ready!")
            text_to_screen.tts(self.screen, text, (400, 200))
            pygame.time.wait(1000)  # countdown timer pre-game

    def mainLoop(self, player1, player2):
        pygame.key.set_repeat(1, 60)
        self.sprites.add(player1)
        self.sprites.add(player2)
        go_to_menu = False
        while True:
            player1.updoot()
            player2.updoot()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == K_ESCAPE:
                        isPaused = True
                        go_to_menu, isPaused = pause_menu.paused(self.screen, isPaused)
            self.screen.blit(self.background, (0, 0))
            self.sprites.draw(self.screen)
            pygame.display.flip()
            if go_to_menu:
                break


def main():
    game_on = Controller()
    player1, player2 = game_on.start_menu()
    game_on.map_select()
    game_on.mainLoop(player1, player2,)
    game_on.start_menu()


main()

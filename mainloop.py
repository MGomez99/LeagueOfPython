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
        self.background_rect = self.background.get_rect
        self.sprites = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        self.lsbullets = pygame.sprite.Group()
        self.rockets = pygame.sprite.Group()
        self.rapidfirebullets = pygame.sprite.Group()
        self.punyassbullets = pygame.sprite.Group()
        self.allprojectiles = pygame.sprite.Group()
        self.map = ""

    def start_menu(self):
        background_file = pygame.image.load("assets/start.png")
        self.screen.blit(background_file, background_file.get_rect())
        pygame.display.flip()
        # prompt "press enter to enter select" or something
        time_to_start = True
        while time_to_start:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        player1 = self.player1select()

                        player2 = self.player2select()
                        return player1, player2
                    if event.key == pygame.K_ESCAPE:
                        sys.exit()

    def player1select(self):
        background_file = pygame.image.load("assets/player1.png")
        self.screen.blit(background_file, background_file.get_rect())
        pygame.display.flip()
        select_player = True
        while select_player:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        player1 = player.Player(50, self.height / 2, "BLUE", "spec1", self.sprites, self.allprojectiles, self.lsbullets, self.bullets, self.rockets, self.rapidfirebullets)
                        return player1
                    elif event.key == pygame.K_w:
                        player1 = player.Player(50, self.height / 2, "BLUE", "spec2", self.sprites, self.allprojectiles, self.lsbullets, self.bullets, self.rockets, self.rapidfirebullets)
                        return player1
                    elif event.key == pygame.K_e:
                        player1 = player.Player(50, self.height / 2, "BLUE", "spec3", self.sprites, self.allprojectiles, self.lsbullets, self.bullets, self.rockets, self.rapidfirebullets)
                        return player1

    def player2select(self):
        background_file = pygame.image.load("assets/player2.png")
        self.screen.blit(background_file, background_file.get_rect())
        pygame.display.flip()
        player_select = True
        while player_select:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        player2 = player.Player(self.width - 50, self.height / 2, "RED", "spec1", self.sprites, self.allprojectiles, self.lsbullets, self.bullets, self.rockets, self.rapidfirebullets)
                        return player2
                    elif event.key == pygame.K_w:
                        player2 = player.Player(self.width - 50, self.height / 2, "RED", "spec2", self.sprites, self.allprojectiles, self.lsbullets, self.bullets, self.rockets, self.rapidfirebullets)
                        return player2
                    elif event.key == pygame.K_e:
                        player2 = player.Player(self.width - 50, self.height / 2, "RED", "spec3", self.sprites, self.allprojectiles, self.lsbullets, self.bullets, self.rockets, self.rapidfirebullets)
                        return player2

    def map_select(self):
        background_file = pygame.image.load("assets/mapselection.png")
        self.screen.blit(background_file, background_file.get_rect())
        pygame.display.flip()
        selecting_map = True
        while selecting_map:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        self.background = pygame.image.load("assets/mars.png")
                        self.screen.blit(self.background, self.background.get_rect())
                        selecting_map = False
                    if event.key == pygame.K_w:
                        self.background = pygame.image.load("assets/moon.png")
                        self.screen.blit(self.background, self.background.get_rect())
                        selecting_map = False
                    if event.key == pygame.K_e:
                        self.background = pygame.image.load("assets/venus.png")
                        self.screen.blit(self.background, self.background.get_rect())
                        selecting_map = False
        self.background_rect = self.background.get_rect
        pygame.display.flip()
        # for time in range(-5, 0):
        #     text = "Game starting in ", str(abs(time)), ". Get ready!"
        #     text = text_to_screen.tts(self.screen, text, 200, 0, 20, (0, 255, 0))
        #     pygame.display.flip()
        #     pygame.time.wait(1000)  # countdown timer pre-game
        #     pygame.display.flip()
        #     self.screen.blit(bg, bg.get_rect())
        #     pygame.display.flip()

    def mainLoop(self, player1, player2):
        pygame.init()
        pygame.key.set_repeat(1, 60)
        # self.sprites.add(player1)
        # self.sprites.add(player2)
        go_to_menu = False
        player1
        while True:
            player1.updoot(player2)
            player2.updoot(player1)
            if player1.hp==0:
                
            if player2.hp==0:

            for event in pygame.event.get():
                player1.updoot(player2, event)
                player2.updoot(player1, event)
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        isPaused = True
                        go_to_menu, isPaused = pause_menu.paused(self.screen, isPaused)
            self.screen.blit(self.background, self.background_rect())
            self.sprites.draw(self.background)

            pygame.display.flip()
            if go_to_menu:
                break


def main():
    game_on = Controller()
    player1, player2 = game_on.start_menu()
    game_on.map_select()
    game_on.mainLoop(player1, player2)
    game_on.start_menu()


main()

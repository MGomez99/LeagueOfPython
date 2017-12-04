import pygame
import player
import projectile
import sys
import pause_menu
import text_to_screen
import stats
import threading
from threading import Thread



class Controller:
    def __init__(self):
        pygame.init()
        self.width = 800
        self.height = 600
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.background = pygame.Surface(self.screen.get_size())  # will become map SURFACE
        self.background_rect = self.background.get_rect
        self.sprites = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        self.lsbullets = pygame.sprite.Group()
        self.rockets = pygame.sprite.Group()
        self.rapidfirebullets = pygame.sprite.Group()
        self.punyassbullets = pygame.sprite.Group()
        self.allprojectiles = pygame.sprite.Group()
        self.bgfile = ''

    def start_menu(self):
        background_file = pygame.image.load("assets/start.png")
        self.screen.blit(background_file, background_file.get_rect())
        pygame.display.flip()
        pygame.key.set_repeat(1, 300)
        # prompt "press enter to enter select" or something
        time_to_start = True
        while time_to_start:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
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
                if event.type == pygame.QUIT:
                    sys.exit()
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
                    if event.key == pygame.K_BACKSPACE:
                        main()  # go back

    def player2select(self):
        background_file = pygame.image.load("assets/player2.png")
        self.screen.blit(background_file, background_file.get_rect())
        pygame.display.flip()
        player_select = True
        while player_select:
            for event in pygame.event.get():
                if event.type == pygame.exit():
                    sys.exit()
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
                    if event.key == pygame.K_BACKSPACE:
                        main() # go back

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
                    if event.key == pygame.K_BACKSPACE:
                        self.start_menu()  # go back
        self.background_rect = self.background.get_rect
        self.bgfile = self.background
        pygame.display.flip()
        # for time in range(-5, 0):
        #     x_pos_list = [i for i in range(101, 96)]
        #     print (x_pos_list)
        #     start = 0
        #     for fontsize in range(30, 35):
        #         if start >= 4:
        #             start = 0
        #         text = "Game starting in " + str(abs(time)) + ". Get ready!"
        #         text_to_screen.tts(self.screen, text, x_pos_list[start], 300, 'assets/spaceage.ttf', fontsize, (0, 255, 0))
        #         start += 1
        #         pygame.display.flip()
        #         pygame.time.wait(100)
        #         self.screen.blit(self.bgfile, self.bgfile.get_rect())
        #         pygame.display.flip()
        #
        #
        #     pygame.time.wait(1000)
        #     self.screen.blit(self.bgfile, self.bgfile.get_rect())
        #     pygame.display.flip()

    def gameOver(self, player1, player2):
        isRunning = True
        while isRunning:
            keys = pygame.key.get_pressed()
            if player1.hp <= 0:
                game_over_bg = pygame.image.load("assets/player2win.png")

            elif player2.hp <= 0:
                game_over_bg = pygame.image.load("assets/player1win.png")
            self.screen.blit(game_over_bg, game_over_bg.get_rect())
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if keys[pygame.K_RETURN]:
                    main()

    def mainLoop(self, player1, player2):
        pygame.init()
        pygame.key.set_repeat(1, 60)
        self.sprites.add(player1)
        self.sprites.add(player2)
        go_to_menu = False
        isRunning = True
        while isRunning:
            if len(player1.allprojectiles.sprites()) > 0:
                self.allprojectiles.add(player1.allprojectiles)
            if len(player2.allprojectiles.sprites()) > 0:
                self.allprojectiles.add(player2.allprojectiles)
            if len(self.allprojectiles.sprites()) > 0:
                for shot in self.allprojectiles.sprites():
                    if shot.team == 'BLUE':
                        player1.number_of_hits = shot.bullet_travelling(player2, player1.number_of_hits)
                    if shot.team == 'RED':
                        player2.number_of_hits = shot.bullet_travelling(player1, player2.number_of_hits)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                keys = pygame.key.get_pressed()
                Thread(target=(player1.updoot(player1.number_of_hits, event, keys))).start()  # update p1
                Thread(target=player2.updoot(player2.number_of_hits, event, keys)).start()  # update p2
                if event.type == pygame.KEYDOWN:  # pause
                    if event.key == pygame.K_ESCAPE:
                        isPaused = True
                        go_to_menu, isPaused = pause_menu.paused(self.screen, isPaused)
            self.sprites.add(player1.sprites)
            self.sprites.add(player2.sprites)
            self.screen.blit(self.bgfile, self.bgfile.get_rect())
            self.sprites.draw(self.screen)
            pygame.display.flip()
            if player1.hp <= 0 or player2.hp <= 0:
                isRunning = False
                self.gameOver(player1, player2)  # game over screen, blit stuff and ask for replay
            if go_to_menu:
                main()


def main():
    game_on = Controller()
    player1, player2 = game_on.start_menu()
    game_on.map_select()
    game_on.mainLoop(player1, player2)
    game_on.start_menu()


main()

import sys
import time
import pygame
import pause_menu
import player


class Controller:
    def __init__(self):
        pygame.init()
        self.width = 800
        self.height = 600
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.background = pygame.Surface(self.screen.get_size())  # will become map SURFACE
        self.background_rect = self.background.get_rect
        self.sprites = pygame.sprite.Group()  # Self explanatory, see description in player.py
        self.bullets = pygame.sprite.Group()
        self.lsbullets = pygame.sprite.Group()
        self.rockets = pygame.sprite.Group()
        self.rapidfirebullets = pygame.sprite.Group()
        self.punyassbullets = pygame.sprite.Group()
        self.allprojectiles = pygame.sprite.Group()  # ALL Projectiles, Doesn't conflict w/ anything so it's ok
        self.bgfile = ''  # For changing background, ignore
        self.clock = pygame.time.Clock()  # Used for countdown timer, ignore
        self.Players = []

    def start_menu(self):
        """
        Start menu for game, calls character selection to get player objects
        :return: player1 and player 2 objects
        """
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
        """
        Called by Start Menu, customize player 1
        :return:
        """
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
                        player1 = player.Player(50, self.height / 2, "BLUE", "spec1", self.sprites,
                                                self.lsbullets, self.bullets, self.rockets, self.rapidfirebullets)
                        return player1
                    elif event.key == pygame.K_w:
                        player1 = player.Player(50, self.height / 2, "BLUE", "spec2", self.sprites,
                                                self.lsbullets, self.bullets, self.rockets, self.rapidfirebullets)
                        return player1
                    elif event.key == pygame.K_e:
                        player1 = player.Player(50, self.height / 2, "BLUE", "spec3", self.sprites,
                                                self.lsbullets, self.bullets, self.rockets, self.rapidfirebullets)
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
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        player2 = player.Player(self.width - 50, self.height / 2, "RED", "spec1", self.sprites,
                                                self.lsbullets, self.bullets, self.rockets,
                                                self.rapidfirebullets)
                        return player2
                    elif event.key == pygame.K_w:
                        player2 = player.Player(self.width - 50, self.height / 2, "RED", "spec2", self.sprites,
                                                self.lsbullets, self.bullets, self.rockets,
                                                self.rapidfirebullets)
                        return player2
                    elif event.key == pygame.K_e:
                        player2 = player.Player(self.width - 50, self.height / 2, "RED", "spec3", self.sprites,
                                                self.lsbullets, self.bullets, self.rockets,
                                                self.rapidfirebullets)
                        return player2
                    if event.key == pygame.K_BACKSPACE:
                        main()  # go back

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
                        self.background = pygame.image.load("assets/venus.png")
                        self.screen.blit(self.background, self.background.get_rect())
                        selecting_map = False
                    if event.key == pygame.K_w:
                        self.background = pygame.image.load("assets/moon.png")
                        self.screen.blit(self.background, self.background.get_rect())
                        selecting_map = False
                    if event.key == pygame.K_e:
                        self.background = pygame.image.load("assets/mars.png")
                        self.screen.blit(self.background, self.background.get_rect())
                        selecting_map = False
                    if event.key == pygame.K_BACKSPACE:
                        self.start_menu()  # go back
        self.background_rect = self.background.get_rect
        self.bgfile = self.background
        pygame.display.flip()
        # some countdown timer shit that pretty much works, don't judge

        for timer in range(-5, 0):
            start_time = time.time()
            self.screen.blit(self.bgfile, self.bgfile.get_rect())
            pygame.display.flip()
            for font_size in range(30, 100, 1):
                current_time = time.time()
                total_time = current_time - start_time
                self.screen.blit(self.bgfile, self.bgfile.get_rect())
                pygame.display.flip()
                text = str(abs(timer))
                rendered_text = pygame.font.Font('assets/spaceage.ttf', font_size).render(text, True, (255, 0, 0))
                text_rect = rendered_text.get_rect(center=(400, 300))

                self.screen.blit(rendered_text, text_rect)
                pygame.display.flip()
                if total_time >= 1:
                    break
            self.screen.blit(self.bgfile, self.bgfile.get_rect())
            pygame.display.flip()

    def gameOver(self, player1, player2):
        """
        Game over Screen
        :param player1: player 1
        :param player2: player 1
        :return: none
        """
        isRunning = True
        while isRunning:
            keys = pygame.key.get_pressed()
            if player1.hp <= 0:
                game_over_bg = pygame.image.load("assets/player2win.png")

            elif player2.hp <= 0:
                game_over_bg = pygame.image.load("assets/player1win.png")
            self.screen.blit(game_over_bg, game_over_bg.get_rect())
            # statistics
            title1_text = pygame.font.Font('assets/spaceage.ttf', 30).render("PLAYER 1", True, (0, 0, 0))
            title1_rect = title1_text.get_rect(left=100, top=350)
            self.screen.blit(title1_text, title1_rect)
            title2_text = pygame.font.Font('assets/spaceage.ttf', 30).render("PLAYER 2", True, (0, 0, 0))
            title2_rect = title2_text.get_rect(left=400, top=350)
            self.screen.blit(title2_text, title2_rect)
            # number of shots
            numofshots1_text = pygame.font.Font('assets/spaceage.ttf', 10).render(
                "Number of shots: " + str(player1.number_of_shots), True, (0, 0, 0))
            numofshots1_rect = numofshots1_text.get_rect(left=100, top=400)
            self.screen.blit(numofshots1_text, numofshots1_rect)
            numofshots2_text = pygame.font.Font('assets/spaceage.ttf', 10).render(
                "Number of shots: " + str(player2.number_of_shots), True, (0, 0, 0))
            numofshots2_rect = numofshots2_text.get_rect(left=400, top=400)
            self.screen.blit(numofshots2_text, numofshots2_rect)
            # number of hits
            numofhits1_text = pygame.font.Font('assets/spaceage.ttf', 10).render(
                "Number of hits: " + str(player1.number_of_hits), True, (0, 0, 0))
            numofhits1_rect = numofhits1_text.get_rect(left=100, top=410)
            self.screen.blit(numofhits1_text, numofhits1_rect)
            numofhits2_text = pygame.font.Font('assets/spaceage.ttf', 10).render(
                "Number of hits: " + str(player2.number_of_hits), True, (0, 0, 0))
            numofhits2_rect = numofhits2_text.get_rect(left=400, top=410)
            self.screen.blit(numofhits2_text, numofhits2_rect)
            # accuracy
            if player1.number_of_shots > 0:
                acc1 = str(round(player1.number_of_hits / player1.number_of_shots, 2) * 100) + "%"
            else:
                acc1 = "N/A"
            if player2.number_of_shots > 0:
                acc2 = str(round(player2.number_of_hits / player2.number_of_shots, 2) * 100) + "%"
            else:
                acc2 = "N/A"
            acc1_text = pygame.font.Font('assets/spaceage.ttf', 10).render("Accuracy: " + acc1, True, (0, 0, 0))
            acc1_rect = acc1_text.get_rect(left=100, top=420)
            self.screen.blit(acc1_text, acc1_rect)
            acc2_text = pygame.font.Font('assets/spaceage.ttf', 10).render("Accuracy: " + acc2, True, (0, 0, 0))
            acc2_rect = acc2_text.get_rect(left=400, top=420)
            self.screen.blit(acc2_text, acc2_rect)
            # damage taken
            dmg1_text = pygame.font.Font('assets/spaceage.ttf', 10).render("Damage taken: " + str(player1.damagetaken),
                                                                           True, (0, 0, 0))
            dmg1_rect = acc1_text.get_rect(left=100, top=430)
            self.screen.blit(dmg1_text, dmg1_rect)
            dmg2_text = pygame.font.Font('assets/spaceage.ttf', 10).render("Damage taken: " + str(player2.damagetaken),
                                                                           True, (0, 0, 0))
            dmg2_rect = acc1_text.get_rect(left=400, top=430)
            self.screen.blit(dmg2_text, dmg2_rect)
            # mana spent
            mana1_text = pygame.font.Font('assets/spaceage.ttf', 10).render("Mana spent: " + str(player1.manaspent),
                                                                            True, (0, 0, 0))
            mana1_rect = mana1_text.get_rect(left=100, top=440)
            self.screen.blit(mana1_text, mana1_rect)
            mana2_text = pygame.font.Font('assets/spaceage.ttf', 10).render("Mana spent: " + str(player2.manaspent),
                                                                            True, (0, 0, 0))
            mana2_rect = mana1_text.get_rect(left=400, top=440)
            self.screen.blit(mana2_text, mana2_rect)
            # final health
            hp1_text = pygame.font.Font('assets/spaceage.ttf', 10).render("Final health: " + str(player1.hp), True,
                                                                          (0, 0, 0))
            hp1_rect = hp1_text.get_rect(left=100, top=450)
            self.screen.blit(hp1_text, hp1_rect)
            hp2_text = pygame.font.Font('assets/spaceage.ttf', 10).render("Final health: " + str(player2.hp), True,
                                                                          (0, 0, 0))
            hp2_rect = hp2_text.get_rect(left=400, top=450)
            self.screen.blit(hp2_text, hp2_rect)
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if keys[pygame.K_RETURN]:
                    main()

    def mainLoop(self, player1, player2):
        """
        The "main" infinite loop that calls the update function from player, it works, don't touch it
        :param player1: player1 obj
        :param player2: player2 obj
        :return: None
        """
        pygame.init()
        self.sprites.add(player1)
        self.sprites.add(player2)
        self.Players = [player1, player2]
        print(self.Players)
        go_to_menu = False
        isRunning = True  # Is the game running?
        pygame.key.set_repeat(10, 10)

        while isRunning:
            # If there's projectiles on the screen
            if len(player1.allprojectiles.sprites()) > 0:
                self.allprojectiles.add(player1.allprojectiles)
            if len(player2.allprojectiles.sprites()) > 0:
                self.allprojectiles.add(player2.allprojectiles)
            if len(self.allprojectiles.sprites()) > 0:
                for shot in self.allprojectiles.sprites():
                    if shot.team == 'BLUE':
                        player1.number_of_hits = shot.bullet_travelling(player1, player2, player1.number_of_hits)
                    if shot.team == 'RED':
                        player2.number_of_hits = shot.bullet_travelling(player2, player1, player2.number_of_hits)
            keys = pygame.key.get_pressed()
            for player in self.Players:
                player.update_pos(keys)
                if player.moving_up:  # ACTUAL MOVEMENT
                    player.y -= player.vel
                elif player.moving_down:
                    player.y += player.vel
                if player.moving_left:
                    player.x -= player.vel
                elif player.moving_right:
                    player.x += player.vel
                player.updoot(player.number_of_hits, keys)

            self.sprites.add(player1.sprites)  # refreshing sprite groups and stuff
            self.sprites.add(player2.sprites)
            self.screen.blit(self.bgfile, self.bgfile.get_rect())  # drawing sprites
            self.sprites.draw(self.screen)

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    sys.exit()

                # player1.updoot(player1.number_of_hits, keys)  # update p1
                # player2.updoot(player2.number_of_hits, keys)  # update p2
                if event.type == pygame.KEYDOWN:  # pause
                    if event.key == pygame.K_ESCAPE:
                        isPaused = True
                        go_to_menu, isPaused = pause_menu.paused(self.screen, isPaused)

            if player1.mana < 100:  # need to regen mana regardless of event in pygame
                player1.mana += .05
            elif player1.mana > 100:  # bugfix
                player1.mana = 100
            if player2.mana < 100:
                player2.mana += .05
            elif player2.mana > 100:  # bugfix
                player2.mana = 100

            self.sprites.add(player1.sprites)  # refreshing sprite groups and stuff
            self.sprites.add(player2.sprites)
            self.screen.blit(self.bgfile, self.bgfile.get_rect())  # drawing sprites
            self.sprites.draw(self.screen)

            # players health and mana text
            # player1 health
            health1_text = pygame.font.Font('assets/spaceage.ttf', 30).render(str(round(player1.hp)), True, (255, 0, 0))
            health1_rect = health1_text.get_rect(left=0, top=0)
            self.screen.blit(health1_text, health1_rect)
            # player2 health
            health2_text = pygame.font.Font('assets/spaceage.ttf', 30).render(str(round(player2.hp, 2)), True,
                                                                              (255, 0, 0))
            health2_rect = health2_text.get_rect(left=740, top=0)
            self.screen.blit(health2_text, health2_rect)
            # player1 mana
            mana1_text = pygame.font.Font('assets/spaceage.ttf', 30).render(str(round(player1.mana, 2)), True,
                                                                            (0, 0, 255))
            mana1_rect = mana1_text.get_rect(left=0, top=35)
            self.screen.blit(mana1_text, mana1_rect)
            # player2 mana
            mana2_text = pygame.font.Font('assets/spaceage.ttf', 30).render(str(round(player2.mana, 2)), True,
                                                                            (0, 0, 255))
            mana2_rect = mana2_text.get_rect(left=740, top=35)
            self.screen.blit(mana2_text, mana2_rect)
            pygame.display.flip()

            if player1.hp <= 0 or player2.hp <= 0:
                player1.number_of_shots = player1.number_of_shots - len(player1.allprojectiles.sprites())
                player2.number_of_shots = player2.number_of_shots - len(player2.allprojectiles.sprites())
                isRunning = False
                self.gameOver(player1, player2)  # game over screen, blit stuff and ask for replay
            if go_to_menu:
                main()  # RESTART TO MENU [ Restart Game ]


def main():
    game_on = Controller()
    player1, player2 = game_on.start_menu()
    game_on.map_select()
    game_on.mainLoop(player1, player2)
    game_on.start_menu()


main()

import sys
import time
import pygame
import pause_menu
import player
import Stats
import health_and_mana

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
        self.bgfile = ''  # For changing and resetting background, different use later on than self.background
        self.clock = pygame.time.Clock()  # Used for countdown timer, ignore
        self.Players = []  # List of players

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
                        main()  # Reset Game [MUCH better than trying to go back to prev screen, trust us]


    def map_select(self):
        background_file = pygame.image.load("assets/mapselection.png")
        self.screen.blit(background_file, background_file.get_rect())
        pygame.display.flip()
        selecting_map = True
        maps = {pygame.K_q: 'assets/venus.png', pygame.K_w: 'assets/moon.png', pygame.K_e: 'assets/mars.png'}
        while selecting_map:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:  # Go back to menu
                            main()  # Nuclear option, easier and works

                    if event.key in maps:
                        self.background = pygame.image.load(maps[event.key])
                        self.screen.blit(self.background, self.background.get_rect())
                        selecting_map = False

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
            Stats.show_stats(player1, player2, self.screen)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if keys[pygame.K_RETURN]:
                    main()

    def refresh_player_sprites(self, players):
            self.sprites.add(players[0].sprites, players[1].sprites)  # refreshing sprite groups and stuff
            self.screen.blit(self.bgfile, self.bgfile.get_rect())  # drawing sprites
            self.sprites.draw(self.screen)

    def mainLoop(self, player1, player2):
        """
        The "main" infinite loop that calls the update function from player, it works, don't touch it
        :param player1: player1 obj
        :param player2: player2 obj
        :return: None
        """
        pygame.init()
        self.sprites.add(player1, player2)  # adds both players to group
        self.Players = [player1, player2]
        go_to_menu = False
        isRunning = True  # Is the game running?
        pygame.key.set_repeat(10, 10)

        while isRunning:
            # If there's projectiles on the screen, update them FIRST
            # Each players projectiles update independently. So, we add any that aren't accounted for into the big group
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

            keys = pygame.key.get_pressed()  # Get a boolean dictionary of all pressed keys

            for player in self.Players:  # Updates players movement, position, state, projectiles based on keys pressed
                player.update_pos(keys)
                if player.moving_up:  # ACTUAL MOVEMENT portion, changing state each frame happens in player.updoot
                    player.y -= player.vel
                elif player.moving_down:
                    player.y += player.vel
                if player.moving_left:
                    player.x -= player.vel
                elif player.moving_right:
                    player.x += player.vel
                player.updoot(player.number_of_hits, keys)
            self.refresh_player_sprites(self.Players)  # refresh player sprites

            for event in pygame.event.get():

                if event.type == pygame.QUIT:  # Don't blame ya
                    sys.exit()

                if event.type == pygame.KEYDOWN:  # pause
                    if event.key == pygame.K_ESCAPE:
                        isPaused = True
                        go_to_menu, isPaused = pause_menu.paused(self.screen, isPaused)
            for player in self.Players:  # Reminder, self.players is a list of both player objects
                if player.mana < 100:  # need to regen mana regardless of event in pygame
                    player.mana += .05
                elif player.mana > 100:  # bugfix
                    player.mana = 100

            self.refresh_player_sprites(self.Players)
            health_and_mana.show_resources(self.Players, self.screen)

            if player1.hp <= 0 or player2.hp <= 0:
                # Final count of shots
                player1.number_of_shots = player1.number_of_shots - len(player1.allprojectiles.sprites())
                player2.number_of_shots = player2.number_of_shots - len(player2.allprojectiles.sprites())
                isRunning = False
                self.gameOver(player1, player2)  # game over screen, blit stuff and ask for replay

            if go_to_menu:
                main()  # RESTART TO 'MENU' [ Restart Game ]


def main():
    game_on = Controller()
    player1, player2 = game_on.start_menu()
    game_on.map_select()
    game_on.mainLoop(player1, player2)
    game_on.start_menu()


main()

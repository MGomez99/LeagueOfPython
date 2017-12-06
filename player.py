import pygame

from projectile import Projectile


class Player(pygame.sprite.Sprite):
    def __init__(self, xcoor, ycoor, team, spec, sprites, lsbullets, bullets, bigassbullets,
                 punyassbullets):
        """
        Oh boy lots of stuff. Everything the player class needs for function calling
        :param xcoor: x pos
        :param ycoor: y pos
        :param team: BLUE/RED
        :param spec: specialization(or RPG "Class")1,2,3
        :param sprites: group of all sprites
        :param lsbullets: lifesteal bullets
        :param bullets: normal bullets from default attack
        :param bigassbullets: rockets
        :param punyassbullets: machine gun bullets
        """
        pygame.sprite.Sprite.__init__(self)
        self.res = pygame.display.get_surface().get_size()
        self.x = xcoor
        self.y = ycoor
        self.moving_left = False
        self.moving_right = False
        self.moving_up = False
        self.moving_down = False
        self.team = team
        # projectiles

        self.allprojectiles = pygame.sprite.Group()  # All PLAYER projectiles
        self.bullets = bullets  # "Default Bullets"
        self.lsbullets = lsbullets  # "LifeSteal Bullets"
        self.bigassbullets = bigassbullets  # "Rockets"
        self.punyassbullets = punyassbullets  # "Rapid Fire Bullets"

        # statistics
        self.number_of_shots = 0  # number of bullets shot by player
        self.number_of_hits = 0  # bullets hit
        self.manaspent = 0
        self.damagetaken = 0
        self.accuracy = 0
        self.hp = 0  # spec dependent, initialize to 0
        self.image = pygame.image.load("assets/" + spec + team.lower() + ".png")
        self.rect = self.image.get_rect()
        self.rect.center = self.x, self.y
        self.sprites = sprites
        self.res = 800, 600  # resolution

        # spec stuff
        self.spec = spec
        if self.spec == "spec1":  # lifesteal
            self.maxhp = 250
            self.hp = self.maxhp
            self.mana = 100
            self.vel = 3
            if self.team == "BLUE":
                self.imagefile = "assets/spec1blue.png"
            elif self.team == "RED":
                self.imagefile = "assets/spec1red.png"
        elif self.spec == "spec2":  # rocket launcher
            self.maxhp = 375
            self.hp = self.maxhp
            self.mana = 100
            self.vel = 1
            if self.team == "BLUE":
                self.imagefile = "assets/spec2blue.png"
            elif self.team == "RED":
                self.imagefile = "assets/spec2red.png"
        elif self.spec == "spec3":  # machine gun
            self.maxhp = 250
            self.hp = self.maxhp
            self.mana = 100
            self.vel = 5
            if self.team == "BLUE":
                self.imagefile = "assets/spec3blue.png"
            elif self.team == "RED":
                self.imagefile = "assets/spec3red.png"

        if self.team == "BLUE":
            self.health_location = (0, 0)
            self.mana_location = (0, 35)
            self.move_left = pygame.K_a
            self.move_right = pygame.K_d
            self.move_up = pygame.K_w
            self.move_down = pygame.K_s

        if self.team == "RED":
            self.health_location = (740, 0)
            self.mana_location = (740, 35)
            self.move_left = pygame.K_j
            self.move_right = pygame.K_l
            self.move_up = pygame.K_i
            self.move_down = pygame.K_k

    def specialAbility1(self):
        """
        Lifesteal Bullets
        :return: True if player has mana
        """
        if self.mana >= 5:
            lsbullet = Projectile(self.x, self.y, 5, 10, self.team, "assets/spec1special.png")
            self.allprojectiles.add(lsbullet)
            self.lsbullets.add(lsbullet)
            self.sprites.add(lsbullet)
            self.mana -= 5
            self.manaspent += 5
            return True

    def specialAbility2(self):
        """
        Rockets
        :return: True if player has mana
        """
        if self.mana >= 5:
            if self.team == 'BLUE':
                bigassbullet = Projectile(self.x, self.y, 4, 40, self.team, "assets/Rocket(blue).png")
            if self.team == 'RED':
                bigassbullet = Projectile(self.x, self.y, 4, 40, self.team, "assets/Rocket(red).png")
            self.allprojectiles.add(bigassbullet)
            self.bigassbullets.add(bigassbullet)
            self.sprites.add(bigassbullet)
            self.mana -= 5
            self.manaspent += 5
            return True

    def specialAbility3(self):
        """
        Machine gun
        :return: True if player has mana
        """
        if self.mana >= 5:
            punyassbullet = Projectile(self.x, self.y, 10, 5, self.team, "assets/spec3special.png")
            self.allprojectiles.add(punyassbullet)
            self.punyassbullets.add(punyassbullet)
            self.sprites.add(punyassbullet)
            self.mana -= 3
            self.manaspent += 3
            return True

    def not_moving(self):
        """
        Resets moving state to not moving
        :return: None
        """
        self.moving_left = False
        self.moving_right = False
        self.moving_up = False
        self.moving_down = False

    def update_pos(self, keys):
        """
        Updates movement state
        :param keys: Keys that are currently pressed
        :return: none
        """
        self.not_moving()  # lets assume none are pressed, function checks if they are pressed below
        if keys[self.move_left]:
            self.moving_left = True
        if keys[self.move_up]:
            self.moving_up = True
        if keys[self.move_down]:
            self.moving_down = True
        if keys[self.move_right]:
            self.moving_right = True

    def update_accuracy(self):
        """
        Updates accuracy, saves to player
        :return: None
        """
        if self.number_of_shots > 0:
            self.accuracy = int(self.number_of_hits) / int(self.number_of_shots)

    def updoot(self, number_of_hits, keys):
        """
        Updates everything but movement (pretty much)
        :param number_of_hits:
        :param keys:
        :return: None
        """
        self.number_of_hits = number_of_hits  # new hits will add to number of hits before this frame

        if self.team == "BLUE":
            if self.x < 0:  # BLUE stay inbounds x
                self.x = 0
            if self.x > self.res[0] / 2:
                self.x = self.res[0] / 2
        elif self.team == "RED":
            if self.x < self.res[0] / 2:  # RED stay inbounds x
                self.x = self.res[0] / 2
            if self.x > self.res[0]:
                self.x = self.res[0]
        if self.y < 0:  # BOTH stay inbounds y
            self.y = 0
        elif self.y > self.res[1]:
            self.y = self.res[1]

        # ABILITIES and SHOOTING
        if self.team == "BLUE":
            if keys[pygame.K_q]:
                if self.mana >= 1:
                    bullet = Projectile(self.x, self.y, 5, 10, self.team, "assets/bullet.png")
                    self.allprojectiles.add(bullet)
                    self.bullets.add(bullet)
                    self.sprites.add(bullet)
                    self.mana -= 1
                    self.manaspent += 1
                    self.number_of_shots += 1
            if keys[pygame.K_e]:
                if self.spec == "spec1":
                    didShoot = self.specialAbility1()  # returns true or false cause checking for mana
                    if didShoot:
                        self.number_of_shots += 1  # shoots if true, same for all
                elif self.spec == "spec2":
                    didShoot = self.specialAbility2()
                    if didShoot:
                        self.number_of_shots += 1
                elif self.spec == "spec3":
                    didShoot = self.specialAbility3()
                    if didShoot:
                        self.number_of_shots += 1
        elif self.team == "RED":
            if keys[pygame.K_u]:  # Pressing U
                if self.mana >= 1:
                    bullet = Projectile(self.x, self.y, 5, 10, self.team, "assets/bullet.png")
                    self.allprojectiles.add(bullet)
                    self.bullets.add(bullet)
                    self.sprites.add(bullet)
                    self.mana -= 1
                    self.number_of_shots += 1
            if keys[pygame.K_o]:  # Pressing O
                if self.spec == "spec1":
                    didShoot = self.specialAbility1()
                    if didShoot:
                        self.number_of_shots += 1
                elif self.spec == "spec2":
                    didShoot = self.specialAbility2()
                    if didShoot:
                        self.number_of_shots += 1
                elif self.spec == "spec3":
                    didShoot = self.specialAbility3()
                    if didShoot:
                        self.number_of_shots += 1

        self.update_accuracy()  # Not much to say
        self.rect.center = self.x, self.y  # move rect to x,y location stored


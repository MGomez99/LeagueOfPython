import pygame
from projectile import Projectile
import stats


class Player(pygame.sprite.Sprite):
    def __init__(self, xcoor, ycoor, team, spec, sprites, all_projectiles, lsbullets, bullets, bigassbullets,
                 punyassbullets):
        pygame.sprite.Sprite.__init__(self)
        self.res = pygame.display.get_surface().get_size()
        self.x = xcoor
        self.y = ycoor
        self.team = team
        #projectiles
        self.allprojectiles = all_projectiles
        self.bullets = bullets
        self.lsbullets = lsbullets
        self.bigassbullets = bigassbullets
        self.punyassbullets = punyassbullets
        self.number_of_shots = 0  # number of bullets shot by player
        self.number_of_hits = 0  # bullets hit
        self.accuracy = 0
        self.image = pygame.image.load("assets/" + spec + team.lower() + ".png")
        self.rect = self.image.get_rect()
        self.rect.center = self.x, self.y
        self.sprites = sprites
        self.res = 800, 600
        # spec stuff
        self.spec = spec
        if self.spec == "spec1":  # lifesteal
            self.hp = 100
            self.mana = 100
            self.vel = 5
            if self.team == "BLUE":
                self.image = "assets/spec1blue.png"
            elif self.team == "RED":
                self.image = "assets/spec1red.png"
        elif self.spec == "spec2":  # rocket launcher
            self.hp = 150
            self.mana = 100
            self.vel = 3
            if self.team == "BLUE":
                self.image = "assets/spec2blue.png"
            elif self.team == "RED":
                self.image = "assets/spec2red.png"
        elif self.spec == "spec3":  # machine gun
            self.hp = 100
            self.mana = 100
            self.vel = 7
            if self.team == "BLUE":
                self.image = "assets/spec3blue.png"
            elif self.team == "RED":
                self.image = "assets/spec3red.png"
        #statistics (also end health, spec)
        self.number_of_shots = 0  # number of bullets shot by player
        self.number_of_hits = 0  # bullets hit
        self.accuracy = 0
        self.manaspent=0
        self.damagetaken=0


    def specialAbility1(self):  # lifesteal
        if self.mana >= 10:
            lsbullet = Projectile(self.x, self.y, 10, 10, self.team, "assets/spec1special.png")
            self.allprojectiles.add(lsbullet)
            self.lsbullets.add(lsbullet)
            self.sprites.add(lsbullet)
            self.mana -= 10
            self.manaspent+10
            return True

    def specialAbility2(self):  # rocket launcher
        if self.mana >= 20:
            bigassbullet = Projectile(self.x, self.y, 5, 25, self.team, "assets/spec2special.png")
            self.allprojectiles.add(bigassbullet)
            self.bigassbullets.add(bigassbullet)
            self.sprites.add(bigassbullet)
            self.mana -= 20
            self.manaspent+20
            return True

    def specialAbility3(self):  # machine gun
        if self.mana >= 5:
            punyassbullet = Projectile(self.x, self.y, 20, 5, self.team, "assets/spec3special.png")
            self.allprojectiles.add(punyassbullet)
            self.punyassbullets.add(punyassbullet)
            self.sprites.add(punyassbullet)
            self.mana -= 5
            self.manaspent+5
            return True

    def updoot(self, enemy_player):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if self.team == "BLUE":
                    if event.key == pygame.K_w:
                        self.y += self.vel
                    if event.key == pygame.K_a:
                        self.x -= self.vel
                    if event.key == pygame.K_s:
                        self.y -= self.vel
                    if event.key == pygame.K_d:
                        self.x += self.vel
                    if event.key == pygame.K_q:
                        if self.mana >= 1:
                            bullet = Projectile(self.x, self.y, 10, 10, self.team, "assets/bullet.png")
                            self.allprojectiles.add(bullet)
                            self.bullets.add(bullet)
                            self.sprites.add(bullet)
                            self.mana -= 1
                            self.manaspent+1
                            self.number_of_shots += 1
                    if action.key == pygame.K_e:
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
                    if self.x < 0:
                        self.x = 0
                    if self.x > self.res[0] / 2:
                        self.x = self.res[0] / 2

            if self.team == "RED":
                if action.key == pygame.K_i:
                    self.y += self.vel
                    print("i")
                if action.key == pygame.K_j:
                    self.x -= self.vel
                if action.key == pygame.K_k:
                    self.y -= self.vel
                if action.key == pygame.K_l:
                    self.x += self.vel
                if action.key == pygame.K_u:
                    if self.mana >= 1:
                        bullet = Projectile(self.x, self.y, 10, 10, self.team, "assets/bullet.png")
                        self.allprojectiles.add(bullet)
                        self.bullets.add(bullet)
                        self.sprites.add(bullet)
                        self.mana -= 1
                        self.number_of_shots += 1
                if action.key == pygame.K_o:
                    if self.spec == "spec1":
                        didShoot = self.specialAbility1()
                        if didShoot:
                            self.number_of_shots += 1
                    if action.key == pygame.K_o:
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
                    if self.x < self.res[0] / 2:
                        self.x = self.res[0] / 2
                    if self.x > self.res[0]:
                        self.x = self.res[0]
                if self.y < 0:
                    self.y = 0
                if self.y > self.res[1]:
                    self.y = self.res[1]
            if self.mana < 100:
                self.mana += .1
            if len(self.bullets.sprites()) > 0:
                self.bullets.bullet_travlling()  # will need to update for uniques as well
                self.mana += .1
            if len(self.allprojectiles) > 0:
                for projectile in self.allprojectiles:
                    for bullet in range(len(projectile)):
                        self.number_of_hits = projectile[bullet].bullet_travelling(enemy_player, self.number_of_hits)
                        if projectile[bullet].hitstat:
                            damagetaken+=projectile[bullet].dmg
            if self.number_of_shots>0:
                self.accuracy = self.number_of_hits/self.number_of_shots

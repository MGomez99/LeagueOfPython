import pygame
from projectile import Projectile


class Player(pygame.sprite.Sprite):

    def __init__(self, display, xcoor, ycoor, team, spec, sprites, lsbullets, bullets, bigassbullets, punyassbullets):
        pygame.init()
        self.x = xcoor
        self.y = ycoor
        self.team = team
        self.sprites = sprites
        self.bullets = bullets
        self.lsbullets = lsbullets
        self.bigassbullets = bigassbullets
        self.punyassbullets = punyassbullets
        # spec stuff
        self.spec = spec
        if self.spec == "spec1":  # lifesteal
            self.hp = 100
            self.mana = 100
            self.vel = 5
            if self.team == "BLUE":
                self.image = "spec1blue.png"
            elif self.team == "RED":
                self.image = "spec1red.png"
        elif self.spec == "spec2":  # rocket launcher
            self.hp = 150
            self.mana = 100
            self.vel = 3
            if self.team == "BLUE":
                self.image = "spec2blue.png"
            elif self.team == "RED":
                self.image = "spec2red.png"
        elif self.spec == "spec3":  # machine gun
            self.hp = 100
            self.mana = 100
            self.vel = 7
            if self.team == "BLUE":
                self.image = "spec3blue.png"
            elif self.team == "RED":
                self.image = "spec3red.png"

    def specialAbility1(self):  # lifesteal
        if self.mana >= 10:
            lsbullet = Projectile(self.x, self.y, 10, 10, self.team, spec1special.png)
            self.sprites.add(lsbullet)
            self.lsbullets.add(lsbullet)
            self.mana -= 10

    def specialAbility2(self):  # rocket launcher
        if self.mana >= 20:
            bigassbullet = Projectile(self.x, self.y, 5, 25, self.team, spec2special.png)
            self.sprites.add(bigassbullet)
            self.bigassbullets.add(bigassbullet)
            self.mana -= 20

    def specialAbility3(self):  # machine gun
        if self.mana >= 5:
            punyassbullet = Projectile(self.x, self.y, 20, 5, self.team, spec3special.png)
            self.sprites.add(punyassbullet)
            self.punyassbullets.add(punyassbullet)
            self.mana -= 5

    def updoot(self):
        for event in pygame.event.get():

            if event.type == pygame.KEYDOWN:
                if self.team == "BLUE":
                    if event.key == K_w:
                        self.y += self.vel
                    if event.key == K_a:
                        self.x -= self.vel
                    if event.key == K_s:
                        self.y -= self.vel
                    if event.key == K_d:
                        self.x += self.vel
                    if event.key == K_q:
                        if self.mana >= 1:
                            bullet = Projectile(self.x, self.y, 10, 10, self.team, "bullet.png")
                            self.sprites.add(bullet)
                            self.bullets.add(bullet)
                            self.mana -= 1
                    if event.key == K_e:
                        if self.spec == "spec1":
                            self.specialAbility1()
                        elif self.spec == "spec2":
                            self.specialAbility2()
                        elif self.spec == "spec3":
                            self.specialAbility3()

                if self.team == "RED":
                    if event.key == K_i:
                        self.y += self.vel
                    if event.key == K_j:
                        self.x -= self.vel
                    if event.key == K_k:
                        self.y -= self.vel
                    if event.key == K_l:
                        self.x += self.vel
                    if event.key == K_u:
                        if self.mana >= 1:
                            bullet = Projectile(self.x, self.y, 10, 10, self.team, "bullet.png")
                            self.sprites.add(bullet)
                            self.bullets.add(bullet)
                            self.mana -= 1
                    if event.key == K_o:
                        if self.spec == "spec1":
                            self.specialAbility1()
                        elif self.spec == "spec2":
                            self.specialAbility2()
                        elif self.spec == "spec3":
                            self.specialAbility3()
            if self.mana < 100:
                self.mana += (.1)
            if len(self.bullets.sprites() > 0):
                self.bullets.update()  # will need to update for uniques as well

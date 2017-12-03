import pygame
import projectile

class spec1: #lifesteal
    def __init__(self):
        self.hp = 100 #tbd
        self.mana = 100 #tbd
        self.image = spec1.png
    def specialAbility(self):
        if self.mana >=20:
            lsbullet = projectile(self.x, self.y, VELOCITYPLACEHOLDER, DAMAGEPLACEHOLDER, self.team, IMAGEPLACEHOLDER)
            self.mana-=20


import pygame
import projectile

class spec2: #rocket
    def __init__(self):
        self.hp = 100 #tbd
        self.mana = 100 #tbd
        self.image = spec2
    def specialAbility(self):
        if self.mana >=MANACOSTPLACEHOLDER:
            #shit here
            self.mana-=MANACOSTPLACEHOLDER


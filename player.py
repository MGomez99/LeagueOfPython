import pygame
import spec1
import spec2
import spec3
import projectile


class Player:
    def __init__(self, xcoor, ycoor, velocity, team, spec):
        self.x = xcoor
        self.y = ycoor
        self.vel = velocity
        self.team = team
        self.spec = spec
        Player.health = self.spec.hp
        Player.mana = self.spec.mana

    def update(self):
        if event.type==pygame.KEYDOWN:
            if self.team=="BLUE":
                if event.key==K_w:
                    self.y+=self.vel
                if event.key==K_a:
                    self.x-=self.vel
                if event.key==K_s:
                    self.y-=self.vel
                if event.key==K_d:
                    self.x+=self.vel
                if event.key==K_q:
                    if player.mana>=MANACOSTPLACEHOLDER:
                        bullet=projectile(self.x,self.y,VELOCITYPLACEHOLDER,DAMAGEPLACEHOLDER,self.team,IMAGEPLACEHOLDER)
                        sprites.add(bullet)
                        projectiles.add(bullet)
                        player.mana-=MANACOSTPLACEHOLDER
                if event.key==K_e:
                    self.spec.specialAbility()
            if self.team=="RED":
                if event.key==K_i:
                    self.y+=self.vel
                if event.key==K_j:
                    self.x-=self.vel
                if event.key==K_k:
                    self.y-=self.vel
                if event.key==K_l:
                    self.x+=self.vel
                if event.key==K_u:
                    if player.mana>=MANACOSTPLACEHOLDER:
                        bullet=projectile(self.x,self.y,VELOCITYPLACEHOLDER,DAMAGEPLACEHOLDER,self.team,IMAGEPLACEHOLDER)
                        sprites.add(bullet)
                        projectiles.add(bullet)
                        player.mana-=MANACOSTPLACEHOLDER
                if event.key==K_o:
                    self.spec.specialAbility()
        if player.mana<100:
            player.mana+=1

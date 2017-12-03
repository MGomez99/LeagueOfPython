import pygame
import projectile


class Player:
    def __init__(self, xcoor, ycoor, team, spec):
        self.x = xcoor
        self.y = ycoor
        self.team = team
        #spec stuff
        self.spec = spec
        if self.spec==spec1: #lifesteal
            self.hp=100
            self.mana=100
            self.vel=5
            self.image="spec1.png"
        elif self.spec==spec2: #rocket launcher
            self.hp=150
            self.mana=100
            self.vel=3
            self.image="spec2.png"
        elif self.spec==spec3: #machine gun
            self.hp=100
            self.mana=100
            self.vel=7
            self.image="spec3.png"
    def specialAbility1(self): #lifesteal
        if self.mana>=10:
            lsbullet=projectile(self.x,self.y,10,10,self.team,spec1special.png)
            sprites.add(lsbullet)
            lsbullets.add(lsbullet)
            self.mana-=10
    def specialAbility2(self): #rocket launcher
        if self.mana>=20:
            bigassbullet=projectile(self.x,self.y,5,25,self.team,spec2special.png)
            sprites.add(bigassbullet)
            bigassbullets.add(bigassbullet)
            self.mana-=20
    def specialAbility3(self): #machine gun
        if self.mana>=5:
            punyassbullet=projectile(self.x,self.y,20,5,self.team,spec3special.png)
            sprites.add(punyassbullet)
            punyassbullets.add(punyassbullet)
            self.mana-=5
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
                    if player.mana>=1:
                        bullet=projectile(self.x,self.y,10,10,self.team,bullet.png)
                        sprites.add(bullet)
                        bullets.add(bullet)
                        player.mana-=1
                if event.key==K_e:
                    if self.spec==spec1:
                        self.specialAbility1()
                    elif self.spec==spec2:
                        self.specialAbility2()
                    elif self.spec==spec3:
                        self.specialAbility3()
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
                        bullets.add(bullet)
                        player.mana-=MANACOSTPLACEHOLDER
                if event.key==K_o:
                    if self.spec==spec1:
                        self.specialAbility1()
                    elif self.spec==spec2:
                        self.specialAbility2()
                    elif self.spec==spec3:
                        self.specialAbility3()
        if player.mana<100:
            player.mana+=(.1)

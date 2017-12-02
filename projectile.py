import pygame


class Projectile(pygame.sprite.Sprite):
    res=pygame.display.get_surface().get_size()
    def __init__(self, xcoor, ycoor, velocity, damage, team, image):
        pygame.sprite.Sprite.__init__(self)
        self.x=xcoor
        self.y=ycoor
        self.vel=velocity
        self.dmg=damage
        self.team=team #BLUE (left side) RED (right side)
        self.projectile=pygame.image.load(image)
        self.rect=self.projectile.get_rect()
    def update(self, player): 
        if self.team=="BLUE" and self.x<res[0]:
            self.x+=self.vel
        elif self.team == "RED" and self.x<0:
            self.x-=self.vel
        elif self.team=="BLUE" and self.x>=res[0]:
            self.kill()
        elif self.team=="RED" and self.x<=0:
            self.kill()
        if self.team != player.team:
            if(self.rect.colliderect(player.rect))==True:
                player.health=player.health-self.damage
                self.kill()

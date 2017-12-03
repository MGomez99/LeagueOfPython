import pygame


class Projectile(pygame.sprite.Sprite):
    def __init__(self, xcoor, ycoor, velocity, damage, team, image):
        self.res = pygame.display.get_surface().get_size()
        pygame.sprite.Sprite.__init__(self)
        self.x = xcoor
        self.y = ycoor
        self.vel = velocity
        self.dmg = damage
        self.team = team
        self.projectile = pygame.image.load(image)
        self.rect = self.projectile.get_rect()

    def bullet_travelling(self, player):
        if self.team == "BLUE" and self.x < self.res[0]:
            self.x += self.vel
        elif self.team == "RED" and self.x < 0:
            self.x -= self.vel
        elif self.team == "BLUE" and self.x >= self.res[0]:
            self.kill()
        elif self.team == "RED" and self.x <= 0:
            self.kill()
        if self.team != player.team:
            if self.rect.colliderect(player.rect):
                player.health = player.health - self.dmg
                self.kill()

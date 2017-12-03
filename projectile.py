import pygame
import player


class Projectile(pygame.sprite.Sprite):
    def __init__(self, xcoor, ycoor, velocity, damage, team, image):
        self.res = pygame.display.get_surface().get_size()
        pygame.sprite.Sprite.__init__(self)
        self.x = xcoor
        self.y = ycoor
        self.vel = velocity
        self.dmg = damage
        self.team = team
        self.image = pygame.image.load(image)
        self.rect.center = self.x, self.y
        self.rect = self.image.get_rect()
        self.projectile = pygame.image.load(image)
        self.rect = self.projectile.get_rect()
        self.hitstat=False

    def bullet_travelling(self, enemy_player, bullets_hit):
        if self.team == "BLUE" and self.x < self.res[0]:
            self.x += self.vel
        elif self.team == "RED" and self.x < 0:
            self.x -= self.vel
        elif self.team == "BLUE" and self.x >= self.res[0]:
            self.kill()
        elif self.team == "RED" and self.x <= 0:
            self.kill()
        if self.team != enemy_player.team:
            if self.rect.colliderect(enemy_player.rect):
                enemy_player.health = enemy_player.health - self.dmg
                self.kill()
                self.hitstat=True
                bullets_hit += 1
            else:
                hitstat=False
        self.rect.center = self.x, self.y
        self.rect = self.image.get_rect()
        return bullets_hit

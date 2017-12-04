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
        self.rect = self.image.get_rect()
        self.projectile = self.image
        self.rect = self.projectile.get_rect()
        self.rect.center = self.x, self.y
        self.hitstat=False

    def bullet_travelling(self, enemy_player, bullets_hit):
        '''
        Updates bullets
        :param enemy_player: not friendly player
        :param bullets_hit: num of bullets hit
        :return: bullets hit
        '''
        if self.team == "BLUE" and self.x < self.res[0]:
            self.x += self.vel
        if self.team == "RED" and self.x > 0:
            self.x -= self.vel
        if self.team == "BLUE" and self.x >= self.res[0]:
            self.kill()
        if self.team == "RED" and self.x <= 0:
            self.kill()
        if self.rect.colliderect(enemy_player.rect):
            print("work")
            enemy_player.hp = enemy_player.hp - self.dmg
            print(enemy_player.hp)
            self.kill()
            self.hitstat=True
            bullets_hit += 1
        else:
            hitstat=False
        self.rect = self.image.get_rect()
        self.rect.center = self.x, self.y
        return bullets_hit

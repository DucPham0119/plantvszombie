import pygame

import constant
from config import car_map


class Car(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        self.image = pygame.image.load('assets/Car/car.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.line = y
        self.rect.bottom = car_map[y]
        self.walk = False
        self.dead = False

    def update(self, zombie_group):
        if not self.walk:
            pass
        elif self.walk:
            self.rect.x += 4
        if self.rect.x > constant.WINDOW_WIDTH:
            self.dead = True

        self.checkCarCollisions(zombie_group)

    def setWalk(self):
        if not self.walk:
            self.walk = True

    def draw(self, surface):
        if not self.dead:
            surface.blit(self.image, self.rect)

    # def attack(self, zombie):
    #     for item in zombie:
    #         if pygame.sprite.collide_mask(self, item):
    #             self.walk = True

    def checkCarCollisions(self, zombie_group):
        for zombie in zombie_group:
            if pygame.sprite.collide_mask(self, zombie) and zombie.can_zombie_move and self.line == zombie.line:
                self.setWalk()
                zombie.collisionCar()
                zombie.die_zombie()
            if self.dead:
                self.kill()

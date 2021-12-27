import pygame

import constant
from config import car_map


class Car(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        self.image = pygame.image.load('assets/Car/car.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.bottom = car_map[y]
        self.walk = False
        self.dead = False

    def update(self, zombie_group):
        # self.current_time = game_info[c.CURRENT_TIME]
        # self.attack(zombie_group)
        if not self.walk:
            pass
        elif self.walk:
            self.rect.x += 4
        if self.rect.x > constant.WINDOW_WIDTH:
            self.dead = True

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

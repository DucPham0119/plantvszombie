import time

import pygame


class Pea(pygame.sprite.Sprite):
    def __init__(self, x, y, name):
        super().__init__()

        self.name = name
        self.start_x = x
        self.start_y = y
        self.path = "assets/Pea/"
        self.x_vel = 4
        self.fly_state = True
        self.exist = True
        self.damage_focus = 5
        self.current_time = 0

    def update(self, display_surface, zombie_group):
        self.animation(display_surface)
        self.collisionZombie(zombie_group)
        if self.rect.x >= 950:
            self.kill()
        if not self.fly_state:
            if (self.current_time - self.explode_timer) > 100:
                self.kill()

    def animation(self, display_surface):
        self.rect.x += self.x_vel
        self.draw(display_surface)

    def draw(self, surface):
        if self.exist:
            surface.blit(self.image, self.rect)

    def collisionZombie(self, zombie):
        pass

    def loadImage(self, name):
        return pygame.image.load(self.path + str(self.name) + "/" + name)


class PeaNormal(Pea):
    def __init__(self, x, y, name):
        super().__init__(x, y, name)
        type_name = self.name + "_0.png"
        self.image = self.loadImage(type_name)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.bottom = y

    def collisionZombie(self, zombie):
        self.current_time = time.time_ns()
        for item in zombie:
            if pygame.sprite.collide_mask(self, item):
                if item.health > 0:
                    item.health -= self.damage_focus
                    self.setExplode()
                    self.fly_state = False
                self.exist = False
                break

    def setExplode(self):
        self.explode_timer = time.time_ns()
        name = "PeaNormalExplode_0.png"
        self.image = self.loadImage(name)


class PeaIce(Pea):
    def __init__(self, x, y, name):
        super().__init__(x, y, name)
        type_name = self.name + "_0.png"
        self.image = self.loadImage(type_name)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.bottom = y

    def collisionZombie(self, zombie):
        self.current_time = time.time_ns()
        for item in zombie:
            if pygame.sprite.collide_mask(self, item):
                if item.health > 0:
                    item.health -= self.damage_focus
                    self.setExplode()
                    self.fly_state = False
                else:
                    item.remove(zombie)
                self.exist = False
                break

    def setExplode(self):
        self.explode_timer = time.time_ns()
        name = "PeaIceExplode_0.gif"
        self.image = self.loadImage(name)

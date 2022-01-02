import time

import pygame

import constant


class Sun(pygame.sprite.Sprite):
    def __init__(self, x, y, dest_y):

        super().__init__()

        self.sun_list = []
        self.loadImage()
        self.current_sprite = 0
        self.image = self.sun_list[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.dest_y = dest_y
        self.time = 0
        self.state = constant.WALK
        self.sun_value = constant.SUN_VALUE
        # self.zombie_group = zombie_group

    def update(self):
        self.time = time.time_ns()
        self.move()
        self.animation()
        self.handleState()

        # self.checkCollision()

    def handleState(self):
        if self.rect.y == self.dest_y:
            self.time = time.time_ns()
            self.state = constant.FREEZE
            if (time.time_ns() - self.time) > constant.SUN_LIVE_TIME:
                self.state = constant.DIE
                self.kill()


    def move(self):
        if self.state == constant.WALK:
            self.rect.y += constant.SUN_CHANGE
            # print(self.rect)

    def animation(self):
        self.current_sprite += 0.4

        if self.current_sprite >= len(self.sun_list):
            self.current_sprite = 0

        self.image = self.sun_list[int(self.current_sprite)]

    def checkCollision(self, x, y):
        if self.state == constant.DIE:
            return False
        if (self.rect.x <= x <= self.rect.right and
                self.rect.y <= y <= self.rect.bottom):
            self.state = constant.DIE
            self.kill()
            return True
        return False

    def loadImage(self):
        for i in range(0, 22):
            self.sun_list.append(
                pygame.transform.scale(pygame.image.load('assets/Sun/Sun' + '_' + str(i) + '.png'), (78, 78)))

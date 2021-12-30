import time

import pygame

import constant
from ZombieHead import ZombieHead


class Zombie(pygame.sprite.Sprite):
    def __init__(self, x, line, name):
        super().__init__()
        self.image = pygame.image.load("assets/Zombies/NormalZombie/Zombie/Zombie_0.png")
        self.rect = self.image.get_rect()
        self.line = line
        y = constant.START_Y + (self.line - 1) * constant.LINE_Y + constant.LINE_Y // 2
        self.rect.topright = (x, y)
        self.name = name
        self.current_sprite = 0
        self.die = False
        self.damage_focus = 30
        self.zombie_list = []
        # self.zombie_head_list = []
        self.zombie_lost_head_list = []
        self.zombie_die_list = []
        self.healthy = 400
        self.can_zombie_move = True

        # value check zombie head and zombie lost head
        self.animate_zombie = True
        self.animate_zombie_head = 0
        self.animate_zombie_lost_head = False
        self.animate_zombie_dead = 0

        self.current_zombie_lost_head = 0
        self.current_zombie_dead = 0

        self.init_zombie_list()
        # self.init_zombie_head()
        self.init_zombie_lost_head()
        self.init_zombie_die()

    def init_zombie_list(self):
        for i in range(1, 22):
            self.zombie_list.append(pygame.transform.scale(
                pygame.image.load("assets/Zombies/NormalZombie/Zombie/Zombie_" + str(i) + ".png"), (166, 144)))

    def init_zombie_lost_head(self):
        for i in range(0, 18):
            self.zombie_lost_head_list.append(
                pygame.image.load("assets/Zombies/NormalZombie/ZombieLostHead/ZombieLostHead_" + str(i) + ".png")
            )

    def init_zombie_die(self):
        for i in range(0, 10):
            self.zombie_die_list.append(
                pygame.image.load("assets/Zombies/NormalZombie/ZombieDie/ZombieDie_" + str(i) + ".png")
            )

    def update(self, plant):
        self.move()
        self.check_animation_zombie()
        self.collisionPlant(plant)

    def move(self):
        if self.can_zombie_move:
            self.rect.x -= constant.NUMBER_CHANGE_MOVE_ZOMBIE

    def check_can_remove(self):
        return self.rect.x < constant.NUMBER_POSITION_CAN_REMOVE_ZOMBIE

    # Animation cho zombie di
    def animation(self, zombie_list):

        if self.current_sprite < len(zombie_list) - 1:
            self.current_sprite += constant.NUMBER_CHANGE_IMAGE_ZOMBIE
        else:
            self.current_sprite = 0

        self.image = zombie_list[int(self.current_sprite)]

    # Animation cho zombie bi mat dau
    def animation_lost_head(self, zombie_list):

        if self.current_zombie_lost_head < len(zombie_list) - 1:
            self.current_zombie_lost_head += constant.NUMBER_CHANGE_IMAGE_ZOMBIE
        else:
            self.current_zombie_lost_head = 0

        self.image = zombie_list[int(self.current_zombie_lost_head)]

    # Animation cho zombie khi chet
    def animation_zombie_dead(self, zombie_list):

        if self.current_zombie_dead < len(zombie_list) - 1:
            self.current_zombie_dead += constant.NUMBER_CHANGE_IMAGE_ZOMBIE
        else:
            self.kill()
            return
        self.image = zombie_list[int(self.current_zombie_dead)]

    # Check cac trang thai animate cua zombie
    def check_animation_zombie(self):
        if self.healthy > 100:
            self.animation(self.zombie_list)
            self.can_zombie_move = True
        elif 100 >= self.healthy > 1:
            self.animation_lost_head(self.zombie_lost_head_list)
        else:
            self.can_zombie_move = False

            self.animation_zombie_dead(self.zombie_die_list)

    # collision voi plant
    def collisionPlant(self, plant):
        for item in plant:
            if pygame.sprite.collide_mask(self, item):
                self.can_zombie_move = False
                item.health -= self.damage_focus
                if item.health == 0:
                    item.remove(plant)
                    self.can_zombie_move = True
                break

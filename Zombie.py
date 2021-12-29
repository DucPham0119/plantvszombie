import time

import pygame

import constant
from ZombieHead import ZombieHead


class Zombie(pygame.sprite.Sprite):
    def __init__(self, x, line, name, head_group=None):
        super().__init__()
        self.image = pygame.image.load("assets/Zombies/NormalZombie/Zombie/Zombie_0.png")
        self.rect = self.image.get_rect()
        self.head_zombie_group = head_group
        self.x = x
        self.line = line
        self.y = constant.START_Y + (self.line - 1) * constant.LINE_Y + constant.LINE_Y // 2
        self.rect.topright = (x, self.y)
        self.name = name
        self.current_sprite = 0
        self.die = False
        self.damage_focus = 30
        self.zombie_list = []
        # self.zombie_head_list = []
        self.zombie_lost_head_list = []
        self.zombie_die_list = []
        self.healthy = 400
        self.can_move = True

        # value check zombie head and zombie lost head
        self.animate_zombie = True
        self.animate_zombie_head = True
        self.animate_zombie_lost_head = False
        self.animate_zombie_dead = False
        self.is_check = 0

        self.init_zombie_list()
        # self.init_zombie_head()
        self.init_zombie_lost_head()
        self.init_zombie_die()

    def init_zombie_list(self):
        for i in range(1, 22):
            self.zombie_list.append(pygame.transform.scale(
                pygame.image.load("assets/Zombies/NormalZombie/Zombie/Zombie_" + str(i) + ".png"), (166, 144)))

    # def init_zombie_head(self):
    #     for i in range(0,12):
    #         self.zombie_head_list.append(
    #             pygame.image.load("assets/Zombies/NormalZombie/ZombieHead/ZombieHead_"+str(i)+".png"))

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
        if self.can_move:
            self.rect.x -= constant.NUMBER_CHANGE_MOVE_ZOMBIE

    def check_can_remove(self):
        return self.rect.x < constant.NUMBER_POSITION_CAN_REMOVE_ZOMBIE

    def animation(self, zombie_list):

        if self.current_sprite < len(zombie_list) - 1:
            self.current_sprite += constant.NUMBER_CHANGE_IMAGE_ZOMBIE
        else:
            self.current_sprite = 0

        self.image = zombie_list[int(self.current_sprite)]

    # def animation_zombie_head(self):
    #     if self.head_current < len(self.zombie_head_list) - 1:
    #         self.head_current += constant.NUMBER_CHANGE_IMAGE_ZOMBIE
    #     else:
    #         self.head_current = 0
    #
    #     self.image = self.zombie_head_list[int(self.head_current)]

    def check_animation_zombie(self):
        if self.healthy > 100:
            self.animation(self.zombie_list)
        elif 100 >= self.healthy:
            self.animation(self.zombie_lost_head_list)
        else:
            self.animation(self.zombie_die_list)



    def collisionPlant(self, plant):
        for item in plant:
            if pygame.sprite.collide_mask(self, item):
                self.can_move = False
                item.health -= self.damage_focus
                if item.health == 0:
                    item.remove(plant)
                    self.can_move = True
                break

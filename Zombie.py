import pygame

import constant


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
        self.healthy = 200
        self.can_move = True

        self.init_zombie_list()

    def init_zombie_list(self):
        for i in range(1, 22):
            self.zombie_list.append(pygame.transform.scale(
                pygame.image.load("assets/Zombies/NormalZombie/Zombie/Zombie_" + str(i) + ".png"), (166, 144)))

    def update(self, plant):
        self.move()
        self.animation()
        self.collisionPlant(plant)

    def move(self):
        if self.can_move:
            self.rect.x -= constant.NUMBER_CHANGE_MOVE_ZOMBIE

    def check_can_remove(self):
        return self.rect.x < constant.NUMBER_POSITION_CAN_REMOVE_ZOMBIE

    def animation(self):

        if self.current_sprite < len(self.zombie_list) - 1:
            self.current_sprite += constant.NUMBER_CHANGE_IMAGE_ZOMBIE
        else:
            self.current_sprite = 0

        self.image = self.zombie_list[int(self.current_sprite)]

    def collisionPlant(self, plant):
        for item in plant:
            if pygame.sprite.collide_mask(self, item):
                self.can_move = False
                item.health -= self.damage_focus
                if item.health == 0:
                    item.remove(plant)
                    self.can_move = True
                break

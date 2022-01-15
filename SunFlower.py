import pygame

import constant
from Sun import Sun
from config import check_map, map_plant


class SunFlower(pygame.sprite.Sprite):
    def __init__(self, x, y, name, sun_group):
        super().__init__()
        self.flower_list = []
        self.init_flower_list()

        # Load imgae and get_rect
        self.name = name
        self.current_sprite = 0
        self.image = self.flower_list[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

        self.suns = sun_group
        self.location_x = 0
        self.location_y = 0

        self.is_animate = False
        self.can_move = True
        self.current_time = pygame.time.get_ticks()

        self.VELOCITY = 10
        self.STARTING_HEALTH = 300
        self.velocity = self.VELOCITY
        self.health = self.STARTING_HEALTH

    def init_flower_list(self):
        for i in range(0, 18):
            image = pygame.image.load('assets/Plant/SunFlower/' + 'SunFlower_' + str(i) + '.png').convert_alpha()
            self.flower_list.append(image)

    def addSun(self):
        sun = Sun(self.rect.x, self.rect.y, self.rect.y + 20)
        self.suns.add(sun)
        pass

    def mouse_pos_plant(self, x, y):
        self.is_animate = True
        self.can_move = False
        self.location_x = x
        self.location_y = y
        self.update_position()
        check_map[self.location_x][self.location_y] = 1

    def update_position(self):
        current_location = map_plant[self.location_x][self.location_y]
        self.rect.center = current_location[0], current_location[1]

    def update(self, time):
        self.creatSun(time)
        if self.is_animate:
            self.animate()

    def animate(self):
        self.current_sprite += 0.4

        if self.current_sprite >= len(self.flower_list):
            self.current_sprite = 0

        self.image = self.flower_list[int(self.current_sprite)]

    def move_plant(self, x, y):
        self.rect.center = (x, y)

    def creatSun(self, time):
        if time <= constant.LEVEL_1_TIME:
            add_sun_flower_time = constant.LEVEL_1_SUN_FLOWER_TIME
        elif time <= constant.LEVEL_2_TIME:
            add_sun_flower_time = constant.LEVEL_2_SUN_FLOWER_TIME
        else:
            add_sun_flower_time = constant.LEVEL_3_SUN_FLOWER_TIME

        if pygame.time.get_ticks() - self.current_time >= add_sun_flower_time:
            self.addSun()
            self.current_time = pygame.time.get_ticks()

import pygame

import constant
from Pea import PeaNormal, PeaIce
from config import map, check_map


class Plant(pygame.sprite.Sprite):
    def __init__(self, x, y, name, zombie_group):
        super().__init__()
        self.name = name
        self.path = "assets/Plant/"
        # Set constant variables
        self.VELOCITY = 10
        self.STARTING_HEALTH = 300

        # Set velocity for Plant
        self.velocity = self.VELOCITY

        # Set value for Plant
        self.health = self.STARTING_HEALTH

        # Animation frames
        self.plant_list = []
        self.init_plant_list()

        # Load imgae and get_rect
        self.current_sprite = 0
        self.image = self.plant_list[self.current_sprite]
        self.rect = self.image.get_rect()

        # Animation boolean
        self.animation_fire = False
        self.is_animate = False
        self.can_move = True
        self.fly = False
        # self.dark_img()

        self.peas = pygame.sprite.GroupSingle()
        self.zombie_group = zombie_group

        self.location_x = x
        self.location_y = y

        self.update_position()

    # def dark_img(self):
    #     if not self.is_animate:
    #         dark = pygame.Surface((self.image.get_width(), self.image.get_height()), flags=pygame.SRCALPHA)
    #         dark.fill((50, 50, 50, 0))
    #         self.image.blit(dark, (0, 0), special_flags=pygame.BLEND_RGBA_SUB)

    def init_plant_list(self):
        pass

    def update_position(self):
        current_location = map[self.location_x][self.location_y]
        self.rect.center = current_location[0], current_location[1]

    def update(self, display_surface):
        # self.map()
        self.peas.update(display_surface, self.zombie_group)
        self.checkPea(display_surface, self.zombie_group)
        # self.check_fire(display_surface)
        if self.is_animate:
            self.animate()
        # else:
        #     self.move(display_surface)

    def animate(self):
        self.current_sprite += 0.4

        if self.current_sprite >= len(self.plant_list):
            self.current_sprite = 0

        self.image = self.plant_list[int(self.current_sprite)]

    # def move(self, display_surface):
    #     return False
    #     keys = pygame.key.get_pressed()
    #
    #     if keys[pygame.K_LEFT] and self.rect.left > 228:
    #         # self.rect.x -= self.velocity
    #         self.location_y = self.location_y - 1
    #         self.update_position()
    #     if keys[pygame.K_RIGHT] and self.rect.right < 980:
    #         # self.rect.x += self.velocity
    #         print("right")
    #         self.location_y = self.location_y + 1
    #         self.update_position()
    #     if keys[pygame.K_UP] and self.rect.top > 100:
    #         # self.rect.y -= self.velocity
    #         self.location_x = self.location_x - 1
    #         self.update_position()
    #     if keys[pygame.K_DOWN] and self.rect.bottom < constant.WINDOW_HEIGHT - 50:
    #         # self.rect.y += self.velocity
    #         self.location_x = self.location_x + 1
    #         self.update_position()
    #     if keys[pygame.K_SPACE]:
    #         self.is_animate = True
    #         self.can_move = False
    #         self.map()
    #         # print(self.rect.x)
    #         # print(self.col)
    #         self.fire(display_surface)
    #         # self.check_fly(display_surface, self.zombie_group)

    def checkPea(self, display_surface, zombie):
        self.line = (self.rect.y - constant.START_Y - constant.LINE_Y // 2) // constant.LINE_Y + 1
        for item in zombie:
            if self.line == item.line and self.is_animate:
                if len(self.peas) == 0:
                    self.fire()
                if len(self.peas) != 0:
                    self.peas.draw(display_surface)

    def update_move(self, type):
        if type == 'right' and self.location_y < 8:
            self.location_y += 1
        if type == 'left' and self.location_y > 0:
            self.location_y -= 1
        if type == 'up' and self.location_x > 0:
            self.location_x -= 1
        if type == 'down' and self.location_x < 4:
            self.location_x += 1

        self.update_position()

        if type == "space" and check_map[self.location_x][self.location_y] == 0:
            self.is_animate = True
            self.can_move = False
            check_map[self.location_x][self.location_y] = 1

    # def map(self):
    #     self.line = (self.rect.y - constant.START_Y - constant.LINE_Y // 2) // constant.LINE_Y + 1
    #     self.col = round((self.rect.midbottom[0] - constant.START_X - 5 * constant.COL_X // 6) // constant.COL_X)
    #     print(self.line, self.col)
    #     if self.col == -1:
    #         self.col = 0
    #     if self.col <= 8:
    #         self.col += 1
    #     print("line, col: ", self.line, self.col)
    #     x = (self.col - 1) * constant.COL_X + constant.COL_X + constant.START_X
    #     y = (self.line - 1) * constant.LINE_Y + constant.LINE_Y + constant.START_Y
    #     # print("x,y: ", x, y)
    #     if self.col >= 7:
    #         self.rect.midbottom = (x + 65, y)
    #     elif self.col >= 4:
    #         self.rect.midbottom = (x + 36, y)
    #     else:
    #         self.rect.midbottom = (x + 5, y)

    def fire(self):
        pass

    def loadImage(self, name):
        return pygame.image.load(self.path + str(self.name) + "/" + name)


class RepeaterPea(Plant):
    def __init__(self, x, y, name, zombie_group):
        super().__init__(x, y, name, zombie_group)

    def init_plant_list(self):
        for i in range(0, 15):
            typeName = self.name + "_" + str(i) + ".png"
            image = self.loadImage(typeName)
            self.plant_list.append(image)

    def fire(self):
        pea_normal = PeaNormal(self.rect.centerx, self.rect.centery, 'PeaNormal')
        self.peas.add(pea_normal)
        pass


class SnowPea(Plant):
    def __init__(self, x, y, name, zombie_group):
        super().__init__(x, y, name, zombie_group)

    def init_plant_list(self):
        for i in range(0, 15):
            typeName = self.name + "_" + str(i) + ".png"
            image = self.loadImage(typeName)
            self.plant_list.append(image)

    def fire(self):
        pea_normal = PeaIce(self.rect.centerx, self.rect.centery, 'PeaIce')
        self.peas.add(pea_normal)
        pass


class Threepeater(Plant):
    def __init__(self, x, y, name, zombie_group):
        super().__init__(x, y, name, zombie_group)

    def init_plant_list(self):
        for i in range(0, 14):
            typeName = self.name + "_" + str(i) + ".png"
            image = self.loadImage(typeName)
            self.plant_list.append(image)

    def fire(self):
        pea_normal = PeaNormal(self.rect.centerx, self.rect.centery, 'PeaNormal')
        self.peas.add(pea_normal)
        pass

# array: 5x9, array[0][0] = x, array[0][1]=y
# current location: x=0,y=0 -> x = 0, y= 1
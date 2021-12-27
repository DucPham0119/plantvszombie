import pygame

import constant
from Pea import PeaNormal, PeaIce
from config import map


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
        # self.rect.center = (x, y)
        # self.line = (self.rect.y - constant.START_Y - constant.LINE_Y // 2) // constant.LINE_Y + 1
        # Animation boolean
        self.animation_fire = False
        self.is_animate = False
        self.can_move = True
        self.fly = False

        self.peas = pygame.sprite.GroupSingle()
        self.zombie_group = zombie_group

        self.location_x = x
        self.location_y = y

        self.update_position()

    def init_plant_list(self):
        pass

    def update_position(self):
        current_location = map[self.location_x][self.location_y]
        self.rect.center = current_location[0], current_location[1]

    def check_fire(self, display_surface):
        # print('len',len(self.peas))
        if self.can_move:
            return
        # self.check_fly(display_surface, zombie)
        if not self.peas.sprite.exist:
            self.fire(display_surface)
            # self.check_fly(display_surface, zombie)
        pass

    def check_fly(self, display_surface, zombie):
        for item in zombie:
            if item.rect.x <= 200:
                self.fly = True
                # print(item.rect.x)
            if self.fly:
                self.fire(display_surface)

    def update(self, display_surface):
        # self.map()
        self.peas.update(display_surface, self.zombie_group)
        self.check_fire(display_surface)
        if self.is_animate:
            self.animate()
        else:
            self.move(display_surface)

    def animate(self):
        self.current_sprite += 0.4

        if self.current_sprite >= len(self.plant_list):
            self.current_sprite = 0

        self.image = self.plant_list[int(self.current_sprite)]

    def move(self, display_surface):
        return False
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and self.rect.left > 228:
            # self.rect.x -= self.velocity
            self.location_y = self.location_y - 1
            self.update_position()
        if keys[pygame.K_RIGHT] and self.rect.right < 980:
            # self.rect.x += self.velocity
            print("right")
            self.location_y = self.location_y + 1
            self.update_position()
        if keys[pygame.K_UP] and self.rect.top > 100:
            # self.rect.y -= self.velocity
            self.location_x = self.location_x - 1
            self.update_position()
        if keys[pygame.K_DOWN] and self.rect.bottom < constant.WINDOW_HEIGHT - 50:
            # self.rect.y += self.velocity
            self.location_x = self.location_x + 1
            self.update_position()
        if keys[pygame.K_SPACE]:
            self.is_animate = True
            self.can_move = False
            self.map()
            # print(self.rect.x)
            # print(self.col)
            self.fire(display_surface)
            # self.check_fly(display_surface, self.zombie_group)

    def update_move(self, type):
        if type == 'right':
            self.location_y = self.location_y + 1
        if type == 'left':
            self.location_y = self.location_y - 1
        if type == 'up':
            self.location_x = self.location_x - 1
        if type == 'down':
            self.location_x = self.location_x + 1

        self.update_position()

    def map(self):
        self.line = (self.rect.midbottom[1] - constant.START_Y - constant.LINE_Y // 2) // constant.LINE_Y + 1
        self.col = round((self.rect.midbottom[0] - constant.START_X - 5 * constant.COL_X // 6) // constant.COL_X)
        print(self.line, self.col)
        if self.col == -1:
            self.col = 0
        if self.col <= 8:
            self.col += 1
        print("line, col: ", self.line, self.col)
        x = (self.col - 1) * constant.COL_X + constant.COL_X + constant.START_X
        y = (self.line - 1) * constant.LINE_Y + constant.LINE_Y + constant.START_Y
        # print("x,y: ", x, y)
        if self.col >= 7:
            self.rect.midbottom = (x + 65, y)
        elif self.col >= 4:
            self.rect.midbottom = (x + 36, y)
        else:
            self.rect.midbottom = (x + 5, y)

    def fire(self, display_surface):
        pass

    def loadImage(self, name):
        return pygame.image.load(self.path + str(self.name) + "/" + name)


# class Peashooter(Plant):
#     def __init__(self, x, y, name, zombie_group):
#         super().__init__(x, y, name, zombie_group)
#
#     def init_plant_list(self):
#         for i in range(0, 13):
#             typeName = self.name + "_" + str(i) + ".png"
#             image = self.loadImage(typeName)
#             self.plant_list.append(image)
#
#     def fire(self, display_surface):
#         pea_normal = PeaNormal(self.rect.centerx, self.rect.centery, 'PeaNormal')
#         self.peas.add(pea_normal)
#         pass


class RepeaterPea(Plant):
    def __init__(self, x, y, name, zombie_group):
        super().__init__(x, y, name, zombie_group)

    def init_plant_list(self):
        for i in range(0, 15):
            typeName = self.name + "_" + str(i) + ".png"
            image = self.loadImage(typeName)
            self.plant_list.append(image)

    def fire(self, display_surface):
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

    def fire(self, display_surface):
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

    def fire(self, display_surface):
        pea_normal = PeaNormal(self.rect.centerx, self.rect.centery, 'PeaNormal')
        self.peas.add(pea_normal)
        pass

# array: 5x9, array[0][0] = x, array[0][1]=y
# current location: x=0,y=0 -> x = 0, y= 1

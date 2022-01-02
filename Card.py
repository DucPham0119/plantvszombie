import pygame

from config import card_name_list, plant_sun_list, plant_frozen_time_list


class Card:
    def __init__(self, x, y, name_index):
        # self.loadFrame(constant.card_name_list[name_index], scale)
        self.name_index = name_index
        self.image = self.loadImage(card_name_list[self.name_index])
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.name_index = int(name_index)
        self.sun_cost = plant_sun_list[self.name_index]
        self.frozen_time = plant_frozen_time_list[self.name_index]
        self.frozen_timer = -self.frozen_time
        self.refresh_timer = 0
        self.select = True

    def loadImage(self, name):
        return pygame.transform.scale(pygame.image.load('assets/Card/' + name + '.png'), (52, 70))

    # Ktra sự click
    def checkMouseClick(self, mouse_pos):
        x, y = mouse_pos
        if self.rect.collidepoint(x, y):
            return True
        return False

    # Có thể click ko
    def canClick(self, sun_value, current_time):
        if self.sun_cost <= sun_value and (current_time - self.frozen_timer) > self.frozen_time:
            return True
        return False

    # có thể chọn không
    def canSelect(self):
        return self.select

    def setSelect(self, can_select):
        self.select = can_select
        if can_select:
            self.image.set_alpha(255)
        else:
            self.image.set_alpha(128)

    def setFrozenTime(self, current_time):
        self.frozen_timer = current_time

    def createShowImage(self, sun_value, current_time):
        '''create a card image to show cool down status
           or disable status when have not enough sun value'''
        time = current_time - self.frozen_timer
        if time < self.frozen_time:  # cool down status
            image = pygame.Surface([self.rect.w, self.rect.h])
            frozen_image = self.image.copy()
            frozen_image.set_alpha(128)
            frozen_height = (self.frozen_time - time) / self.frozen_time * self.rect.h

            image.blit(frozen_image, (0, 0), (0, 0, self.rect.w, frozen_height))
            image.blit(self.image, (0, frozen_height),
                       (0, frozen_height, self.rect.w, self.rect.h - frozen_height))
        elif self.sun_cost > sun_value:  # disable status
            image = self.image.copy()
            image.set_alpha(192)
        else:
            image = self.image
        return image

    def update(self, sun_value, current_time):
        if (current_time - self.refresh_timer) >= 250:
            self.image = self.createShowImage(sun_value, current_time)
            self.refresh_timer = current_time

    def draw(self, surface):
        surface.blit(self.image, self.rect)


class Image(pygame.sprite.Sprite):
    def __init__(self, x, y, name):
        super().__init__()
        self.name = name
        self.image = pygame.image.load('assets/Plant/' + name + '/' + name + '_0.png')
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def move_image(self, x, y):
        self.rect.center = (x, y)

    # def update(self):

    def draw(self, surface):
        surface.blit(self.image, self.rect)


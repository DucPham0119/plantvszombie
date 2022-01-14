import pygame

from config import card_name_list, plant_sun_list, plant_frozen_time_list


class Card:
    def __init__(self, x, y, name_index):
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
        return pygame.transform.scale(pygame.image.load('assets/Card/' + name + '.png').convert_alpha(), (52, 70))

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

    def update(self, current_time):
        if (current_time - self.refresh_timer) >= 250:
            self.refresh_timer = current_time

    def draw(self, surface):
        surface.blit(self.image, self.rect)


class Image(pygame.sprite.Sprite):
    def __init__(self, x, y, name):
        super().__init__()
        self.name = name
        self.image = pygame.image.load('assets/Plant/' + name + '/' + name + '_0.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def move_image(self, x, y):
        self.rect.center = (x, y)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

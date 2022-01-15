import constant
import random
import pygame

from Car import Car
from Card import Image
from MenuBar import MenuBar
from Plant import RepeaterPea, SnowPea, Threepeater, Peashooter
from Sun import Sun
from SunFlower import SunFlower
from Zombie import NormalZombie, FlagZombie, BucketheadZombie
from config import check_map, card_name_list, plant_name_list, plant_sun_list


class Game:
    def __init__(self, display_surface):
        self.image = pygame.sprite.GroupSingle()
        self.type_plant = None
        self.zombie_time = pygame.time.get_ticks()
        self.sun_time = pygame.time.get_ticks()
        self.HUD_font = pygame.font.SysFont('calibri', 64)
        self.title_font = pygame.font.SysFont('calibri', 64)
        # self.update_count = 0
        #
        # self.round_number = 1
        # self.frame_count = 0

        self.is_check = 0

        self.can_pos_plant = False
        self.click_sun = False
        self.click_card = False

        self.zombie_group = pygame.sprite.Group()
        self.plant_group = pygame.sprite.Group()
        self.sunflower_group = pygame.sprite.Group()
        self.pea_group = pygame.sprite.GroupSingle()
        self.car_group = pygame.sprite.Group()
        self.sun_group = pygame.sprite.Group()
        self.head_group = pygame.sprite.Group()
        self.card = card_name_list
        self.menu_bar = MenuBar(50, self.card)
        self.setupCars()
        self.display_surface = display_surface

        self.time = 0
        self.exit = False
        self.again_play = False

    def update(self):
        self.time += 1
        self.add_sun()
        self.add_zombie()

        self.menu_bar.update(pygame.time.get_ticks())
        self.menu_bar.draw(self.display_surface)

        self.image.update()
        self.image.draw(self.display_surface)

        self.zombie_group.update(self.display_surface, self.plant_group, self.sunflower_group)
        self.zombie_group.draw(self.display_surface)

        self.plant_group.update(self.display_surface)
        self.plant_group.draw(self.display_surface)

        self.sunflower_group.update(self.time)
        self.sunflower_group.draw(self.display_surface)

        self.car_group.update(self.zombie_group)
        self.car_group.draw(self.display_surface)

        self.sun_group.update()
        self.sun_group.draw(self.display_surface)

    def add_sun(self):
        if self.time <= constant.LEVEL_1_TIME:
            add_sun_time = constant.LEVEL_1_SUN_TIME
        elif self.time <= constant.LEVEL_2_TIME:
            add_sun_time = constant.LEVEL_2_SUN_TIME
        else:
            add_sun_time = constant.LEVEL_3_SUN_TIME

        if pygame.time.get_ticks() - self.sun_time >= add_sun_time:
            x = random.randint(250, 900)
            des_y = random.randint(200, 550)
            self.sun_group.add(Sun(x, 0, des_y))
            self.sun_time = pygame.time.get_ticks()

    def add_zombie(self):
        if self.time <= constant.LEVEL_1_TIME:
            add_zombie_time = constant.LEVEL_1_ZOMBIE_TIME
            health = constant.LEVEL_1_ZOMBIE_HEALTH
        elif self.time <= constant.LEVEL_2_TIME:
            add_zombie_time = constant.LEVEL_2_ZOMBIE_TIME
            health = constant.LEVEL_2_ZOMBIE_HEALTH
        else:
            add_zombie_time = constant.LEVEL_3_ZOMBIE_TIME
            health = constant.LEVEL_3_ZOMBIE_HEALTH

        if pygame.time.get_ticks() - self.zombie_time >= add_zombie_time:
            x = random.randint(1100, constant.WINDOW_WIDTH)
            line = random.randint(0, 4)
            typeZombie = random.randint(0, 4)
            if typeZombie == 0:
                zombie = NormalZombie(x, line, "zombie", health)
                self.zombie_group.add(zombie)
            elif typeZombie == 1:
                zombie = FlagZombie(x, line, "zombie", health)
                self.zombie_group.add(zombie)
            elif typeZombie == 2:
                zombie = BucketheadZombie(x, line, "zombie", health)
                self.zombie_group.add(zombie)

            self.zombie_time = pygame.time.get_ticks()

    def check_click_sun(self, x, y):
        for item in self.sun_group:
            if item.rect.collidepoint(x, y):
                self.menu_bar.increaseSunValue(item.sun_value)
                item.kill()

    def add_plant_mouse(self, x, y):
        for card in self.menu_bar.card_list:
            if card.rect.collidepoint(x, y):
                number_plant_can_move = filter(lambda plant: plant.can_move, self.plant_group)
                plant_name = plant_name_list[card.name_index]
                sun_plant = plant_sun_list[card.name_index]
                if len(list(number_plant_can_move)) == 0 and self.menu_bar.sun_value >= sun_plant:
                    self.can_pos_plant = True
                    if plant_name == 'SunFlower':
                        self.image.add(Image(x, y, 'SunFlower'))
                        self.menu_bar.decreaseSunValue(sun_plant)
                    elif plant_name == 'Peashooter' and self.menu_bar.sun_value >= sun_plant:
                        self.image.add(Image(x, y, 'Peashooter'))
                        self.menu_bar.decreaseSunValue(sun_plant)
                    elif plant_name == 'RepeaterPea' and self.menu_bar.sun_value >= sun_plant:
                        self.image.add(Image(x, y, 'RepeaterPea'))
                        self.menu_bar.decreaseSunValue(sun_plant)
                    elif plant_name == 'SnowPea' and self.menu_bar.sun_value >= sun_plant:
                        self.image.add(Image(x, y, 'SnowPea'))
                        self.menu_bar.decreaseSunValue(sun_plant)
                    elif plant_name == 'Threepeater' and self.menu_bar.sun_value >= sun_plant:
                        self.image.add(Image(x, y, 'Threepeater'))
                        self.menu_bar.decreaseSunValue(sun_plant)

                    self.type_plant = plant_name
                    pygame.mouse.set_visible(False)

    def moveImage(self, x, y):
        for image in self.image:
            image.move_image(x, y)

    def check_click_menu(self, mouse_pos):
        return self.menu_bar.checkMenuBarClick(mouse_pos)

    def setupCars(self):
        for i in range(5):
            self.car_group.add(Car(190, i))

    def canSeedPlant(self, x, y):
        return check_map[x][y] == 0

    def removeImage(self):
        for item in self.image:
            item.kill()

    def pos_plant(self, mouse_pos, name):
        x, y = mouse_pos
        pos_x = (y - constant.START_Y) // 100
        pos_y = x // constant.START_X - 3
        if self.canSeedPlant(pos_x, pos_y):
            if name == 'RepeaterPea':
                self.plant_group.add(RepeaterPea(pos_x, pos_y, "RepeaterPea", self.zombie_group))
            elif name == 'SnowPea':
                self.plant_group.add(SnowPea(pos_x, pos_y, "SnowPea", self.zombie_group))
            elif name == 'Threepeater':
                self.plant_group.add(Threepeater(pos_x, pos_y, "Threepeater", self.zombie_group))
            elif name == 'Peashooter':
                self.plant_group.add(Peashooter(x, y, "Peashooter", self.zombie_group))
            else:
                self.sunflower_group.add(SunFlower(x, y, "SunFlower", self.sun_group))

            self.removeImage()
            self.plant_seed(pos_x, pos_y)

    def plant_seed(self, x, y):
        for item in self.plant_group:
            if item.can_move:
                item.mouse_pos_plant(x, y)
                pygame.mouse.set_visible(True)
                self.can_pos_plant = False
        for item in self.sunflower_group:
            if item.can_move:
                item.mouse_pos_plant(x, y)
                pygame.mouse.set_visible(True)
                self.can_pos_plant = False

    def check_game_over(self):
        for item in self.zombie_group:
            if item.check_can_remove():
                return True
        return False

    def game_over(self):
        if self.check_game_over():
            self.screen_end_game("screen_game_over.jpg")

    def you_win(self):
        if self.time >= constant.LEVEL_3_TIME:
            self.screen_end_game("screen_win.jpg")

    def screen_end_game(self, image_name):
        image = pygame.transform.scale(pygame.image.load('assets/Background/' + image_name).convert_alpha(),
                                       (1200, 600))
        rect = image.get_rect()
        rect.topleft = (0, 0)
        self.display_surface.blit(image, rect)
        pygame.display.update()
        is_paused = True
        while is_paused:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    is_paused = False
                    self.exit = True

    def start_game(self, image_name, button_name):
        image = pygame.transform.scale(pygame.image.load('assets/Background/' + image_name).convert_alpha(),
                                       (1200, 600))
        rect = image.get_rect()
        rect.topleft = (0, 0)

        button = pygame.transform.scale(pygame.image.load('assets/Background/' + button_name).convert_alpha(), (64, 64))
        button_rect = image.get_rect()
        button_rect.topleft = (560, 280)

        self.display_surface.blit(image, rect)
        self.display_surface.blit(button, button_rect)
        pygame.display.update()

        is_paused = True
        while is_paused:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if (560 <= mouse_pos[0] <= 620 and
                            button_rect.y <= mouse_pos[1] <= 340):
                        is_paused = False
                        self.again_play = True
                if event.type == pygame.QUIT:
                    is_paused = False
                    self.exit = True

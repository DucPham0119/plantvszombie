import constant
import random
import pygame

from Car import Car
from Card import Image
from MenuBar import MenuBar
from Plant import RepeaterPea, SnowPea, Threepeater, Peashooter
from Sun import Sun
from Zombie import Zombie
from config import check_map, card_name_list, plant_name_list


class Game:
    """A class to help manage gameplay"""

    def __init__(self, display_surface):
        """Initialize the game"""
        # Set constant variables
        self.image = pygame.sprite.GroupSingle()
        self.type_plant = None
        self.zombie_time = pygame.time.get_ticks()
        self.sun_time = pygame.time.get_ticks()
        self.HUD_font = pygame.font.SysFont('calibri', 64)
        self.title_font = pygame.font.SysFont('calibri', 64)
        self.update_count = 0
        # Set game values
        self.score = 0
        self.round_number = 1
        self.frame_count = 0

        self.is_check = 0

        self.can_pos_plant = False
        self.click_sun = False
        self.click_card = False

        self.zombie_group = pygame.sprite.Group()
        self.zombie_head_group = pygame.sprite.GroupSingle()
        self.plant_group = pygame.sprite.Group()
        self.pea_group = pygame.sprite.GroupSingle()
        self.car_group = pygame.sprite.Group()
        self.sun_group = pygame.sprite.Group()
        self.card = card_name_list
        self.menu_bar = MenuBar(50, self.card)

        self.display_surface = display_surface

    def get_zombie_group(self):
        return self.zombie_group

    def get_plant_group(self):
        return self.plant_group

    def get_pea_group(self):
        return self.pea_group

    def update(self):
        self.add_sun()
        self.setupCars()
        # self.add_plant()
        self.remove_zombie()
        self.draw()
        self.add_zombie()

        self.menu_bar.update(pygame.time.get_ticks())
        self.menu_bar.draw(self.display_surface)

        self.image.update()
        self.image.draw(self.display_surface)

        self.zombie_head_group.update()
        self.zombie_group.update(self.display_surface, self.plant_group)
        self.zombie_group.draw(self.display_surface)

        self.plant_group.update(self.display_surface)
        self.plant_group.draw(self.display_surface)

        self.car_group.update(self.zombie_group)
        self.car_group.draw(self.display_surface)

        self.sun_group.update()
        self.sun_group.draw(self.display_surface)

    def draw(self):
        """Draw the game HUD"""

        # Set text
        score_text = self.HUD_font.render("Score: " + str(self.score), True, constant.WHITE)
        score_rect = score_text.get_rect()
        score_rect.topleft = (10, constant.WINDOW_HEIGHT - 50)

        round_text = self.HUD_font.render("Night: " + str(self.round_number), True, constant.WHITE)
        round_rect = round_text.get_rect()
        round_rect.topright = (constant.WINDOW_WIDTH - 10, constant.WINDOW_HEIGHT - 50)

        # Draw the HUD
        self.display_surface.blit(score_text, score_rect)
        self.display_surface.blit(round_text, round_rect)

    def add_sun(self):
        if pygame.time.get_ticks() - self.sun_time >= 10000:
            x = random.randint(200, 900)
            des_y = random.randint(200, 550)
            self.sun_group.add(Sun(x, 0, des_y))
            self.sun_time = pygame.time.get_ticks()

    def add_zombie(self):
        if pygame.time.get_ticks() - self.zombie_time >= 7000:
            x = random.randint(1000, constant.WINDOW_WIDTH) + 40
            line = random.randint(0, 4)
            print('zombie_line ', line)
            zombie = Zombie(x, line, "zombie", self.zombie_head_group)
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
                self.can_pos_plant = True
                number_plant_can_move = filter(lambda plant: plant.can_move, self.plant_group)
                plant_name = plant_name_list[card.name_index]
                if len(list(number_plant_can_move)) == 0:
                    # if plant_name == 'SunFlower':
                    #     self.image.add(Image(x, y, 'SunFlower'))
                    if plant_name == 'Peashooter':
                        self.image.add(Image(x, y, 'Peashooter'))
                    elif plant_name == 'RepeaterPea':
                        self.image.add(Image(x, y, 'RepeaterPea'))
                    elif plant_name == 'SnowPea':
                        self.image.add(Image(x, y, 'SnowPea'))
                    elif plant_name == 'Threepeater':
                        self.image.add(Image(x, y, 'Threepeater'))

                    self.type_plant = plant_name
                    pygame.mouse.set_visible(False)

    def moveImage(self, x, y):
        for image in self.image:
            # if image.can_move:
            image.move_image(x, y)

    def remove_zombie(self):
        for item in self.zombie_group:
            if item.check_can_remove():
                self.zombie_group.remove(item)

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
            # else:
            #     self.plant_group.add(SunFlower(x, y, "Threepeater", self.zombie_group))

            self.removeImage()
            self.plant_seed(pos_x, pos_y)

    def plant_seed(self, x, y):
        for item in self.plant_group:
            if item.can_move:
                item.mouse_pos_plant(x, y)
                pygame.mouse.set_visible(True)
                self.can_pos_plant = False

    def checkCarCollisions(self):
        collided_func = pygame.sprite.collide_circle_ratio(0.8)
        for car in self.car_group:
            zombies = pygame.sprite.spritecollide(car, self.zombie_group, False, collided_func)
            for zombie in zombies:
                # if zombie and zombie.state != c.DIE:
                car.setWalk()
                # zombie.setDie()
            if car.dead:
                self.car_group.remove(car)

    def pause_game(self, main_text, sub_text):
        global running

        # Create main pause text
        main_text = self.title_font.render(main_text, True, constant.GREEN)
        main_rect = main_text.get_rect()
        main_rect.center = (constant.WINDOW_WIDTH // 2, constant.WINDOW_HEIGHT // 2)

        # Create sub pause text
        sub_text = self.title_font.render(sub_text, True, constant.WHITE)
        sub_rect = sub_text.get_rect()
        sub_rect.center = (constant.WINDOW_WIDTH // 2, constant.WINDOW_HEIGHT // 2 + 64)

        # Display the pause text
        self.display_surface.fill(constant.BLACK)
        self.display_surface.blit(main_text, main_rect)
        self.display_surface.blit(sub_text, sub_rect)
        pygame.display.update()

        # Pause the game until user hits enter or quits
        is_paused = True
        while is_paused:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    # User wants to continue
                    if event.key == pygame.K_RETURN:
                        is_paused = False
                # User wants to quit
                if event.type == pygame.QUIT:
                    is_paused = False
                    running = False

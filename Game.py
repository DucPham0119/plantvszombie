import constant
import random
import pygame

from Car import Car
from MenuBar import MenuBar
from Plant import RepeaterPea, SnowPea, Threepeater
from Sun import Sun
from Zombie import Zombie


class Game:
    """A class to help manage gameplay"""

    def __init__(self, display_surface):
        """Initialize the game"""
        # Set constant variables
        self.zombie_time = pygame.time.get_ticks()
        self.sun_time = pygame.time.get_ticks()
        self.HUD_font = pygame.font.SysFont('calibri', 64)
        self.title_font = pygame.font.SysFont('calibri', 64)
        self.update_count = 0
        # Set game values
        self.score = 0
        self.round_number = 1
        self.frame_count = 0

        self.zombie_group = pygame.sprite.Group()
        self.plant_group = pygame.sprite.Group()
        self.pea_group = pygame.sprite.Group()
        self.car_group = pygame.sprite.Group()
        self.sun_group = pygame.sprite.Group()
        self.card = constant.card_name_list
        self.menu_bar = MenuBar(50, self.card)
        self.display_surface = display_surface
        self.can_pos_plant = False
        self.click_sun = False
        self.click_card = False

    def get_zombie_group(self):
        return self.zombie_group

    def get_plant_group(self):
        return self.plant_group

    def get_pea_group(self):
        return self.pea_group

    def update(self):
        self.add_sun()
        self.setupCars()
        self.add_plant()
        self.remove_zombie()
        self.draw()
        self.add_zombie()
        self.menu_bar.update(pygame.time.get_ticks())
        self.menu_bar.draw(self.display_surface)
        self.zombie_group.update(self.plant_group)
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

    def add_plant(self):
        keys = pygame.key.get_pressed()
        pos_x = 150
        pos_y = 370
        if keys[pygame.K_1]:
            self.can_pos_plant = True
            number_plant_can_move = filter(lambda x: x.can_move, self.plant_group)
            if len(list(number_plant_can_move)) == 0:
                self.plant_group.add(RepeaterPea(pos_x, pos_y, "RepeaterPea", self.zombie_group))
        if keys[pygame.K_2]:
            self.can_pos_plant = True
            number_plant_can_move = filter(lambda x: x.can_move, self.plant_group)
            if len(list(number_plant_can_move)) == 0:
                self.plant_group.add(SnowPea(pos_x, pos_y, "SnowPea", self.zombie_group))
        if keys[pygame.K_3]:
            self.can_pos_plant = True
            number_plant_can_move = filter(lambda x: x.can_move, self.plant_group)
            if len(list(number_plant_can_move)) == 0:
                self.plant_group.add(Threepeater(pos_x, pos_y, "Threepeater", self.zombie_group))

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
            zombie = Zombie(x, line, "zombie", 30)
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
                number_plant_can_move = filter(lambda x: x.can_move, self.plant_group)
                if len(list(number_plant_can_move)) == 0:
                    self.plant_group.add(Threepeater(x, y, "Threepeater", self.zombie_group))
                    pygame.mouse.set_visible(False)

                # for plant in self.plant_group:
                #     if plant.can_move:
                #         x,y=pygame.mouse.get_pos()
                #         plant.move_plant(x,y)

    def movePlant(self):
        for plant in self.plant_group:
            if plant.can_move:
                x, y = pygame.mouse.get_pos()
                plant.move_plant(x, y)

    def remove_zombie(self):
        for item in self.zombie_group:
            if item.check_can_remove():
                self.zombie_group.remove(item)

    def check_click_menu(self, mouse_pos):
        return self.menu_bar.checkMenuBarClick(mouse_pos)

    def setupCars(self):
        for i in range(5):
            self.car_group.add(Car(190, i))

    def pos_plant(self, mouse_pos):
        for item in self.plant_group:
            if item.can_move:
                item.mouse_pos_plant(mouse_pos)
                self.can_pos_plant = False
                pygame.mouse.set_visible(True)

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

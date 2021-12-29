import constant
import random
import pygame

from Car import Car
from Pea import PeaNormal
from Plant import RepeaterPea, SnowPea, Threepeater
from Zombie import Zombie
from ZombieHead import ZombieHead


class Game:
    """A class to help manage gameplay"""

    def __init__(self, display_surface):
        """Initialize the game"""
        # Set constant variables
        self.HUD_font = pygame.font.SysFont('calibri', 64)
        self.title_font = pygame.font.SysFont('calibri', 64)
        self.update_count = 0
        # Set game values
        self.score = 0
        self.round_number = 1
        self.frame_count = 0

        self.is_check = 0

        self.zombie_group = pygame.sprite.Group()
        self.plant_group = pygame.sprite.Group()
        self.plant_group.add(RepeaterPea(0, 0, "RepeaterPea", self.zombie_group))
        self.pea_group = pygame.sprite.Group()
        self.car_group = pygame.sprite.Group()
        self.zombie_head_group = pygame.sprite.Group()

        self.display_surface = display_surface

    def get_zombie_group(self):
        return self.zombie_group

    def get_plant_group(self):
        return self.plant_group

    def get_pea_group(self):
        return self.pea_group

    def remove_zombie(self):
        for item in self.zombie_group:
            if item.check_can_remove():
                self.zombie_group.remove(item)

    def add_plant(self):
        keys = pygame.key.get_pressed()
        pos_x = random.randint(0, 4)
        pos_y = random.randint(0, 8)
        if keys[pygame.K_1]:
            number_plant_can_move = filter(lambda x: x.can_move, self.plant_group)
            if len(list(number_plant_can_move)) == 0:
                self.plant_group.add(RepeaterPea(pos_x, pos_y, "RepeaterPea", self.zombie_group))
        if keys[pygame.K_2]:
            number_plant_can_move = filter(lambda x: x.can_move, self.plant_group)
            if len(list(number_plant_can_move)) == 0:
                self.plant_group.add(SnowPea(pos_x, pos_y, "SnowPea", self.zombie_group))
        if keys[pygame.K_3]:
            number_plant_can_move = filter(lambda x: x.can_move, self.plant_group)
            if len(list(number_plant_can_move)) == 0:
                self.plant_group.add(Threepeater(pos_x, pos_y, "Threepeater", self.zombie_group))

    def update(self):
        self.setupCars()
        self.add_plant()
        self.remove_zombie()
        self.draw()
        self.add_zombie()
        # self.check_lost_head()
        self.zombie_group.update(self.plant_group)
        self.zombie_group.draw(self.display_surface)
        self.plant_group.update(self.display_surface)
        self.plant_group.draw(self.display_surface)
        self.car_group.update(self.zombie_group)
        self.car_group.draw(self.display_surface)

        # self.zombie_head_group.draw(self.display_surface)
        # self.zombie_head_group.update()
        # self.checkCarCollisions()

    def setupCars(self):
        for i in range(5):
            self.car_group.add(Car(190, i))

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

    def add_zombie(self):
        if len(self.zombie_group) <= 10:
            x = random.randint(1000, constant.WINDOW_WIDTH) + 40
            line = random.randint(0, 4)
            # zombie_head = ZombieHead(x,line)
            # self.setLostHead(zombie_head)
            zombie = Zombie(x, line, "zombie", self.zombie_head_group)
            self.zombie_group.add(zombie)

    # set zombie lost head

    # def setLostHead(self, zombie_head):
    #     if len(self.zombie_head_group) < 1:
    #         self.zombie_head_group.add(zombie_head)

    # def check_lost_head(self):
    #     if self.is_check < 100:
    #         self.setLostHead()
    #         self.is_check += 1
    #     else:
    #         for zombie in self.zombie_head_group:
    #             self.zombie_head_group.remove(zombie)

    def move_plant(self, type):
        for item in self.plant_group:
            if item.can_move:
                item.update_move(type)
        # plant.update_move(type)

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

import constant
import random
import pygame

from Plant import Plant
from Zombie import Zombie


class Game():
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

        self.zombie_group = pygame.sprite.Group()
        self.plant_group = pygame.sprite.Group()
        self.plant_group.add(Plant(250, 200, 'plant'))
        self.pea_group = pygame.sprite.Group()
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

    def update(self):
        self.remove_zombie()
        self.draw()
        self.add_zombie()

    def draw(self):
        """Draw the game HUD"""
        # Set colors
        WHITE = (255, 255, 255)

        # Set text
        score_text = self.HUD_font.render("Score: " + str(self.score), True, WHITE)
        score_rect = score_text.get_rect()
        score_rect.topleft = (10, constant.WINDOW_HEIGHT - 50)

        round_text = self.HUD_font.render("Night: " + str(self.round_number), True, WHITE)
        round_rect = round_text.get_rect()
        round_rect.topright = (constant.WINDOW_HEIGHT - 10, constant.WINDOW_HEIGHT - 50)

        # Draw the HUD
        self.display_surface.blit(score_text, score_rect)
        self.display_surface.blit(round_text, round_rect)

    def add_zombie(self):
        if len(self.zombie_group) <= 10:
            x = random.randint(1000, constant.WINDOW_WIDTH) + 40
            y = random.randint(50, constant.WINDOW_HEIGHT - 100) - 10
            zombie = Zombie(x, y, "zombie")
            self.zombie_group.add(zombie)

    def pause_game(self, main_text, sub_text):
        global running

        # Set colors
        WHITE = (255, 255, 255)
        BLACK = (0, 0, 0)
        GREEN = (25, 200, 25)

        # Create main pause text
        main_text = self.title_font.render(main_text, True, GREEN)
        main_rect = main_text.get_rect()
        main_rect.center = (constant.WINDOW_WIDTH // 2, constant.WINDOW_HEIGHT // 2)

        # Create sub pause text
        sub_text = self.title_font.render(sub_text, True, WHITE)
        sub_rect = sub_text.get_rect()
        sub_rect.center = (constant.WINDOW_WIDTH // 2, constant.WINDOW_HEIGHT // 2 + 64)

        # Display the pause text
        self.display_surface.fill(BLACK)
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

import random

import pygame

pygame.init()

# Set size
WINDOWN_WIDTH = 1200
WINDOWN_HEIGHT = 700

display_surface = pygame.display.set_mode((WINDOWN_WIDTH, WINDOWN_HEIGHT))
pygame.display.set_caption("Game Plant vs Zombie")

# Set FPS and clock
FPS = 60
clock = pygame.time.Clock()

# Load in a background image (we must resize)
background_image = pygame.transform.scale(pygame.image.load("assets/Background/Background_1.jpg"), (1280, 736))
background_rect = background_image.get_rect()
background_rect.topleft = (0, 0)


# class Game
# Define classes
class Game():
    """A class to help manage gameplay"""

    def __init__(self, zombie_group):
        """Initialize the game"""
        # Set constant variables
        self.HUD_font = pygame.font.SysFont('calibri', 64)
        self.title_font = pygame.font.SysFont('calibri', 64)

        # Set game values
        self.score = 0
        self.round_number = 1
        self.frame_count = 0

        self.zombie_group = zombie_group

    def update(self):
        self.add_zombie()

    def draw(self):
        """Draw the game HUD"""
        # Set colors
        WHITE = (255, 255, 255)
        GREEN = (25, 200, 25)

        # Set text
        score_text = self.HUD_font.render("Score: " + str(self.score), True, WHITE)
        score_rect = score_text.get_rect()
        score_rect.topleft = (10, WINDOWN_HEIGHT - 50)

        title_text = self.title_font.render("Zombie Knight", True, GREEN)
        title_rect = title_text.get_rect()
        title_rect.center = (WINDOWN_WIDTH // 2, WINDOWN_WIDTH - 25)

        round_text = self.HUD_font.render("Night: " + str(self.round_number), True, WHITE)
        round_rect = round_text.get_rect()
        round_rect.topright = (WINDOWN_WIDTH - 10, WINDOWN_HEIGHT - 50)

        time_text = self.HUD_font.render("Sunrise In: " + str(self.round_time), True, WHITE)
        time_rect = time_text.get_rect()
        time_rect.topright = (WINDOWN_WIDTH - 10, WINDOWN_HEIGHT - 25)

        # Draw the HUD
        display_surface.blit(score_text, score_rect)
        display_surface.blit(title_text, title_rect)
        display_surface.blit(round_text, round_rect)
        display_surface.blit(time_text, time_rect)

    def add_zombie(self):
        """Add a zombie to the game"""
        # Check to add a zombie every second
        if self.frame_count % FPS == 0:
            # Only add a zombie if zombie creation time has passed
            if len(self.zombie_group) < 10:
                x = random.randint(1000, WINDOWN_WIDTH) + 40
                y = random.randint(50, WINDOWN_HEIGHT - 100) - 10
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
        main_rect.center = (WINDOWN_WIDTH // 2, WINDOWN_HEIGHT // 2)

        # Create sub pause text
        sub_text = self.title_font.render(sub_text, True, WHITE)
        sub_rect = sub_text.get_rect()
        sub_rect.center = (WINDOWN_WIDTH // 2, WINDOWN_HEIGHT // 2 + 64)

        # Display the pause text
        display_surface.fill(BLACK)
        display_surface.blit(main_text, main_rect)
        display_surface.blit(sub_text, sub_rect)
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


# class Zombie
class Zombie(pygame.sprite.Sprite):
    def __init__(self, x, y, name):
        super().__init__()
        self.image = pygame.image.load("assets/Zombies/NormalZombie/Zombie/Zombie_0.png")
        self.rect = self.image.get_rect()
        self.rect.topright = (x, y)
        self.name = name
        self.current_sprite = 0

    def update(self):
        self.animation()

    def animation(self):
        self.zombie_list = []
        self.zombie_list.append(
            pygame.transform.scale(pygame.image.load("assets/Zombies/NormalZombie/Zombie/Zombie_0.png"), (166, 144)))
        self.zombie_list.append(
            pygame.transform.scale(pygame.image.load("assets/Zombies/NormalZombie/Zombie/Zombie_1.png"), (166, 144)))
        self.zombie_list.append(
            pygame.transform.scale(pygame.image.load("assets/Zombies/NormalZombie/Zombie/Zombie_2.png"), (166, 144)))
        self.zombie_list.append(
            pygame.transform.scale(pygame.image.load("assets/Zombies/NormalZombie/Zombie/Zombie_3.png"), (166, 144)))
        self.zombie_list.append(
            pygame.transform.scale(pygame.image.load("assets/Zombies/NormalZombie/Zombie/Zombie_4.png"), (166, 144)))
        self.zombie_list.append(
            pygame.transform.scale(pygame.image.load("assets/Zombies/NormalZombie/Zombie/Zombie_5.png"), (166, 144)))
        self.zombie_list.append(
            pygame.transform.scale(pygame.image.load("assets/Zombies/NormalZombie/Zombie/Zombie_6.png"), (166, 144)))
        self.zombie_list.append(
            pygame.transform.scale(pygame.image.load("assets/Zombies/NormalZombie/Zombie/Zombie_7.png"), (166, 144)))
        self.zombie_list.append(
            pygame.transform.scale(pygame.image.load("assets/Zombies/NormalZombie/Zombie/Zombie_8.png"), (166, 144)))
        self.zombie_list.append(
            pygame.transform.scale(pygame.image.load("assets/Zombies/NormalZombie/Zombie/Zombie_9.png"), (166, 144)))
        self.zombie_list.append(
            pygame.transform.scale(pygame.image.load("assets/Zombies/NormalZombie/Zombie/Zombie_10.png"), (166, 144)))
        self.zombie_list.append(
            pygame.transform.scale(pygame.image.load("assets/Zombies/NormalZombie/Zombie/Zombie_11.png"), (166, 144)))
        self.zombie_list.append(
            pygame.transform.scale(pygame.image.load("assets/Zombies/NormalZombie/Zombie/Zombie_12.png"), (166, 144)))
        self.zombie_list.append(
            pygame.transform.scale(pygame.image.load("assets/Zombies/NormalZombie/Zombie/Zombie_13.png"), (166, 144)))
        self.zombie_list.append(
            pygame.transform.scale(pygame.image.load("assets/Zombies/NormalZombie/Zombie/Zombie_14.png"), (166, 144)))
        if self.current_sprite < len(self.zombie_list) - 1:
            self.current_sprite += 0.1
        else:
            self.current_sprite = 0

        for i in zombie_group:
            if i.rect.x < 50:
                zombie_group.remove(i)
            if self.current_sprite < len(self.zombie_list) - 1:
                self.current_sprite += 0.1
            else:
                self.current_sprite = 0

            i.rect.x -= 0.01
            i.image = self.zombie_list[int(self.current_sprite)]


zombie_group = pygame.sprite.Group()
# zombie_group.add(Zombie(WINDOWN_WIDTH, WINDOWN_HEIGHT // 2, "zombie"))

# Create a game
my_game = Game(zombie_group)
my_game.pause_game("Zombie Knight", "Press 'Enter' to Begin")

# The main game loop
running = True
while running:
    # Check to see if the user wants to quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Blit the background
    display_surface.blit(background_image, background_rect)
    # update and draw sprite group
    my_game.update()
    zombie_group.update()
    zombie_group.draw(display_surface)
    # Update the display and tick the clock
    pygame.display.update()
    clock.tick(FPS)

# End the game
pygame.quit()

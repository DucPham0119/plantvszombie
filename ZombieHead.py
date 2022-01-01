import pygame
import constant


class ZombieHead(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("assets/Zombies/NormalZombie/ZombieHead/ZombieHead_0.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.zombie_head_list = []

        # set value animation
        self.current_sprite = 0
        self.init_zombie_head()

    def update(self):
        self.animation()

    def init_zombie_head(self):
        for i in range(0, 12):
            self.zombie_head_list.append(
                pygame.image.load("assets/Zombies/NormalZombie/ZombieHead/ZombieHead_" + str(i) + ".png"))

    def animation(self):
        if self.current_sprite < len(self.zombie_head_list) - 1:
            self.current_sprite += constant.NUMBER_CHANGE_IMAGE_ZOMBIE
        else:
            self.current_sprite = 0

        self.image = self.zombie_head_list[int(self.current_sprite)]

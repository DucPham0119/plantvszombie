import pygame


class ZombieHead(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        self.zombie_head_list = []
        self.current_sprite = 0
        self.init_zombie_head()
        self.image = self.zombie_head_list[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y

    def update(self):
        self.animation()

    def move(self):
        self.rect.y += 0.001

    def init_zombie_head(self):
        for i in range(0, 12):
            self.zombie_head_list.append(
                pygame.image.load(
                    "assets/Zombies/NormalZombie/ZombieHead/ZombieHead_" + str(i) + ".png").convert_alpha())

    def animation(self):
        self.current_sprite += 0.25
        if self.current_sprite >= len(self.zombie_head_list):
            self.kill()
            return

        self.image = self.zombie_head_list[int(self.current_sprite)]

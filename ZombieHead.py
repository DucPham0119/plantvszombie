import pygame


class ZombieHead(pygame.sprite.Sprite):
    def __init__(self, x, y, head_status):
        super().__init__()
        self.des_y = y + 150
        self.head_status = head_status
        self.zombie_head_list = []
        self.current_sprite = 0
        self.init_zombie_head()
        self.image = self.zombie_head_list[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.y = x
        self.rect.top = y

    def update(self):
        # self.move()
        if self.head_status:
            self.animation()

    def move(self):
        # print("xx")
        # self.rect.x += 10
        self.rect.y += 1
        # if self.rect.top >= self.des_y:
        #     self.kill()

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def init_zombie_head(self):
        for i in range(0, 12):
            self.zombie_head_list.append(
                pygame.image.load("assets/Zombies/NormalZombie/ZombieHead/ZombieHead_" + str(i) + ".png").convert_alpha())

    def animation(self):
        self.current_sprite += 0.4
        if self.current_sprite >= len(self.zombie_head_list):
            self.kill()
            self.head_status = False
            return

        self.image = self.zombie_head_list[int(self.current_sprite)]

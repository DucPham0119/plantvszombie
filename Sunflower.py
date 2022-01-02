import pygame
import constant


class Sunflower(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("assets/Plant/SunFlower/SunFlower_0.png")
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

        # set heal value
        self.STARTING_HEAL = constant.PLANT_HEALTHY
        self.healthy = self.STARTING_HEAL

        # set list cho animation
        self.sunflower_list = []
        self.current_sprite = 0

    def init_sunflower(self):
        for i in range(0,18):
            self.sunflower_list.append(
                pygame.image.load("assets/Plant/SunFlower/SunFlower_"+str(i)+".png")
            )

    def animation(self):
        if self.current_sprite < len(self.sunflower_list) - 1:
            self.current_sprite += constant.NUMBER_CHANGE_IMAGE_ZOMBIE
        else:
            self.current_sprite = 0

        self.image = self.sunflower_list[int(self.current_sprite)]


    def update(self):
        pass

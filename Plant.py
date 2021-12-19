import pygame

class Plant(pygame.sprite.Sprite):
    def __init__(self, x, y, name):
        super().__init__()
        self.name = name
        self.image = pygame.image.load("assets/Plant/Peashooter/Peashooter_0.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y

    # def update(self):
    #     self.attacking(zombie_group)
    #
    # def attacking(self, zombie):
    #     # if zombie.rect.x < 550 :
    #     self.pea.append(PeaNormal(self.rect.centerx, self.rect.centery, "PeaNormal"))
    #     self.pea[0].update()


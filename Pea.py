import pygame


class Pea(pygame.sprite.Sprite):
    def __init__(self, x, y, name):
        super().__init__()

        self.name = name
        self.start_x = x
        self.start_y = y
        self.path = "assets/Pea/"
        self.x_vel = 4
        self.fly_state = True
        self.exist = True

    def update(self, display_surface, zombie_group):
        self.animation(display_surface)
        self.collisionZombie(zombie_group)

    def animation(self, display_surface):
        self.rect.x += self.x_vel
        self.draw(display_surface)
        # if not self.fly_state:
        #     self.draw(display_surface)
        #     self.exist = False
        #     self.kill()

    def draw(self, surface):
        if self.exist:
            surface.blit(self.image, self.rect)

    def collisionZombie(self, zombie):
        pass

    def addPea(self):
        self.rect.x = self.start_x
        self.rect.bottom = self.start_y
        self.image = pygame.image.load("assets/Pea/PeaNormal/PeaNormal_0.png")
        # self.loadImage(self.name)

    def loadImage(self, name):
        return pygame.image.load(self.path + str(self.name) + "/" + name)


class PeaNormal(Pea):
    def __init__(self, x, y, name):
        super().__init__(x, y, name)
        type_name = self.name + "_0.png"
        self.image = self.loadImage(type_name)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.bottom = y

    def collisionZombie(self, zombie):
        # if pygame.sprite.groupcollide(self, zombie, False):
        #     name = "PeaNormalExplode_0.png"
        #     self.image = self.loadImage(name)
        #     # self.kill()
        #     self.exist = False

        for item in zombie:
            if pygame.sprite.collide_mask(self,item):
                name = "PeaNormalExplode_0.png"
                self.image = self.loadImage(name)
                self.exist = False
                print(item)
                break


class PeaIce(Pea):
    def __init__(self, x, y, name):
        super().__init__(x, y, name)
        type_name = self.name + "_0.png"
        self.image = self.loadImage(type_name)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.bottom = y

    def collisionZombie(self, zombie):
        if pygame.sprite.collide_rect(self, zombie, False):
            name = "PeaIceExplode_0.gif"
            self.image = self.loadImage(name)
            self.fly_state = False



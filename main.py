# import random
# import time
#
# import pygame
#
# pygame.init()
#
# # Set size
# WINDOWN_WIDTH = 1280
# WINDOWN_HEIGHT = 736
#
# display_surface = pygame.display.set_mode((WINDOWN_WIDTH, WINDOWN_HEIGHT))
# pygame.display.set_caption("Game Plant vs Zombie")
#
# # Set FPS and clock
# FPS = 60
# clock = pygame.time.Clock()
#
# # Load in a background image (we must resize)
# background_image = pygame.transform.scale(pygame.image.load("assets/Background/Background_1.jpg"), (1280, 736))
# background_rect = background_image.get_rect()
# background_rect.topleft = (0, 0)
#
#
# # class Game
# # Define classes
#
#
#
# # class Zombie
#
# class Pea(pygame.sprite.Sprite):
#     def __init__(self, x, y, name):
#         super().__init__()
#
#         self.name = name
#         self.start_x = x
#         self.start_y = y
#         self.path = "assets/Pea/"
#         self.x_vel = 4
#         self.fly_state = True
#         self.exist = True
#
#     def update(self):
#         self.animation()
#         self.collisionZombie(zombie_group)
#
#     def animation(self):
#         self.rect.x += self.x_vel
#         self.draw(display_surface)
#         if not self.fly_state:
#             self.draw(display_surface)
#             self.exist = False
#             self.kill()
#
#     def draw(self, surface):
#         if self.exist:
#             surface.blit(self.image, self.rect)
#
#     def collisionZombie(self, zombie):
#         pass
#
#     def addPea(self):
#         self.rect.x = self.start_x
#         self.rect.bottom = self.start_y
#         self.image = pygame.image.load("assets/Pea/PeaNormal/PeaNormal_0.png")
#         # self.loadImage(self.name)
#
#     def loadImage(self, name):
#         return pygame.image.load(self.path + str(self.name) + "/" + name)
#
#
# class PeaNormal(Pea):
#     def __init__(self, x, y, name):
#         super().__init__(x, y, name)
#         type_name = self.name + "_0.png"
#         self.image = self.loadImage(type_name)
#         self.rect = self.image.get_rect()
#         self.rect.x = x
#         self.rect.bottom = y
#
#     def collisionZombie(self, zombie):
#         if pygame.sprite.spritecollide(self, zombie, False):
#             name = "PeaNormalExplode_0.png"
#             self.image = self.loadImage(name)
#             self.fly_state = False
#
#
# class PeaIce(Pea):
#     def __init__(self, x, y, name):
#         super().__init__(x, y, name)
#         type_name = self.name + "_0.png"
#         self.image = self.loadImage(type_name)
#         self.rect = self.image.get_rect()
#         self.rect.x = x
#         self.rect.bottom = y
#
#     def collisionZombie(self, zombie):
#         if pygame.sprite.spritecollide(self, zombie, False):
#             name = "PeaIceExplode_0.gif"
#             self.image = self.loadImage(name)
#             self.fly_state = False
#
#
# class Plant(pygame.sprite.Sprite):
#     def __init__(self, x, y, name, pea_group):
#         super().__init__()
#         self.name = name
#         self.pea = []
#         self.image = pygame.image.load("assets/Plant/Peashooter/Peashooter_0.png")
#         self.rect = self.image.get_rect()
#         self.rect.centerx = x
#         self.rect.bottom = y
#
#     def update(self):
#         self.attacking(zombie_group)
#
#     def attacking(self, zombie):
#         # if zombie.rect.x < 550 :
#         self.pea.append(PeaNormal(self.rect.centerx, self.rect.centery, "PeaNormal"))
#         self.pea[0].update()
#
#
# zombie_group = pygame.sprite.Group()
# pea_group = pygame.sprite.Group()
# plant_group = pygame.sprite.Group()
# plant_group.add(Plant(250, 200, "plant", pea_group))
# # Create a game
# my_game = Game(zombie_group, plant_group, pea_group)
# my_game.pause_game("Zombie Knight", "Press 'Enter' to Begin")
#
# # The main game loop
# running = True
# while running:
#     # Check to see if the user wants to quit
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#
#     # Blit the background
#     display_surface.blit(background_image, background_rect)
#     # update and draw sprite group
#     my_game.update()
#     zombie_group.update()
#     zombie_group.draw(display_surface)
#     plant_group.update()
#     plant_group.draw(display_surface)
#     # pea_group.update()
#     # Update the display and tick the clock
#     pygame.display.update()
#     clock.tick(FPS)
#
# # End the game
# pygame.quit()
from Boostrap import Boostrap

bootstrap = Boostrap()

bootstrap.run()

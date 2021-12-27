import pygame

import constant
from Game import Game


class Boostrap():
    def run(self):
        pygame.init()
        display_surface = pygame.display.set_mode((constant.WINDOW_WIDTH, constant.WINDOW_HEIGHT))
        pygame.display.set_caption("Game Plant vs Zombie")
        fps = 60
        clock = pygame.time.Clock()
        background_image = pygame.transform.scale(pygame.image.load("assets/Background/Background_1.jpg"), (1400, 600))
        background_rect = background_image.get_rect()
        background_rect.topleft = (0, 0)

        my_game = Game(display_surface)
        my_game.pause_game("Zombie Knight", "Press 'Enter' to Begin")
        running = True
        while running:
            # Check to see if the user wants to quit
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        my_game.move_plant("right")
                    if event.key == pygame.K_LEFT:
                        my_game.move_plant("left")
                    if event.key == pygame.K_DOWN:
                        my_game.move_plant('down')
                    if event.key == pygame.K_UP:
                        my_game.move_plant('up')
                    if event.key == pygame.K_SPACE:
                        my_game.move_plant('space')
                if event.type == pygame.QUIT:
                    running = False

            # Blit the background
            display_surface.blit(background_image, background_rect)
            # update and draw sprite group
            my_game.update()
            # my_game.zombie_group.update()
            # my_game.zombie_group.draw(display_surface)
            # my_game.plant_group.update()
            # my_game.plant_group.draw(display_surface)
            # pea_group.update()
            # Update the display and tick the clock
            pygame.display.update()
            clock.tick(fps)

        # End the game
        pygame.quit()

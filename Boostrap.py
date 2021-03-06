import pygame

import constant
from Game import Game


class Boostrap:
    def run(self):
        pygame.init()
        display_surface = pygame.display.set_mode((constant.WINDOW_WIDTH, constant.WINDOW_HEIGHT))
        pygame.display.set_caption("Game Plant vs Zombie")
        fps = 30
        clock = pygame.time.Clock()
        background_image = pygame.transform.scale(pygame.image.load("assets/Background/Background_1.jpg").convert_alpha(), (1400, 600))
        background_rect = background_image.get_rect()
        background_rect.topleft = (0, 0)

        pygame.mixer.music.load('assets/Music/Crazy_Dave.mp3')
        pygame.mixer.music.play(-1)
        my_game = Game(display_surface)
        my_game.start_game("plantzombie.jpg", 'play-button.png')
        running = True
        # sound_game.play()
        while running and not my_game.exit:
            # Check to see if the user wants to quit
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    x, y = mouse_pos
                    if my_game.can_pos_plant:
                        my_game.pos_plant(mouse_pos, my_game.type_plant)
                    elif my_game.check_click_menu(mouse_pos):
                        my_game.add_plant_mouse(x, y)
                    else:
                        my_game.check_click_sun(x, y)
                if event.type == pygame.KMOD_LGUI:
                    mouse_pos = pygame.mouse.get_pos()
                    my_game.moveImage(mouse_pos[0], mouse_pos[1])
                if event.type == pygame.QUIT:
                    running = False

            my_game.game_over()
            my_game.you_win()
            display_surface.blit(background_image, background_rect)
            my_game.update()
            pygame.display.update()
            clock.tick(fps)

        # End the game
        pygame.quit()


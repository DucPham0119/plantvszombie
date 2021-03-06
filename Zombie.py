import pygame

import constant
from ZombieHead import ZombieHead
from config import check_map, map_zombie


class Zombie(pygame.sprite.Sprite):
    def __init__(self, x, line, name, health):
        super().__init__()
        self.head_status = True
        self.zombie_list = []
        self.init_zombie_list()
        self.current_sprite = 0
        self.image = self.zombie_list[self.current_sprite]
        self.rect = self.image.get_rect()
        self.line = line
        y = map_zombie[self.line]
        self.rect.centerx = x
        self.rect.bottom = y
        self.name = name

        self.die = False
        self.damage_focus = 5

        self.zombie_lost_head_list = []
        self.zombie_die_list = []
        self.zombie_attack_list = []
        self.zombie_lost_head_attack_list = []
        self.head_zombie = pygame.sprite.GroupSingle()
        self.health = health
        self.can_zombie_move = True
        self.head_status = False

        # current_sprite cua cac trang thai animation zombie
        self.current_zombie_lost_head = 0
        self.current_zombie_dead = 0

        # value check zombie attack
        self.zombie_attack = True
        self.zombie_lost_head_attack = False

        self.init_zombie_lost_head()
        self.init_zombie_die()
        self.init_zombie_attack()
        self.init_zombie_lost_head_attack()

    def init_zombie_list(self):
        pass

    def init_zombie_lost_head(self):
        for i in range(0, 18):
            self.zombie_lost_head_list.append(
                pygame.image.load(
                    "assets/Zombies/NormalZombie/ZombieLostHead/ZombieLostHead_" + str(i) + ".png").convert_alpha()
            )

    def init_zombie_die(self):
        for i in range(0, 10):
            self.zombie_die_list.append(
                pygame.image.load("assets/Zombies/NormalZombie/ZombieDie/ZombieDie_" + str(i) + ".png").convert_alpha()
            )

    def init_zombie_attack(self):
        pass

    def init_zombie_lost_head_attack(self):
        for i in range(0, 11):
            self.zombie_lost_head_attack_list.append(
                pygame.image.load(
                    "assets/Zombies/NormalZombie/ZombieLostHeadAttack/ZombieLostHeadAttack_" + str(
                        i) + ".png").convert_alpha()
            )

    def update(self, surface, plant, flower):
        self.move()
        self.head_zombie.update()
        self.head_zombie.draw(surface)
        self.check_animation_zombie()
        self.collisionPlant(plant)
        self.collisionPlant(flower)

    def move(self):
        if self.can_zombie_move:
            self.rect.x -= constant.NUMBER_CHANGE_MOVE_ZOMBIE

    def check_can_remove(self):
        return self.rect.x < constant.NUMBER_POSITION_CAN_REMOVE_ZOMBIE

    # Animation cho zombie di
    def animation(self, zombie_list):
        if self.current_sprite < len(zombie_list) - 1:
            self.current_sprite += constant.NUMBER_CHANGE_IMAGE_ZOMBIE
        else:
            self.current_sprite = 0

        self.image = zombie_list[int(self.current_sprite)]

    # Animation cho zombie bi mat dau
    def animation_lost_head(self, zombie_list):
        if not self.zombie_lost_head_attack:
            if self.current_zombie_lost_head < len(zombie_list) - 1:
                self.current_zombie_lost_head += constant.NUMBER_CHANGE_IMAGE_ZOMBIE
            else:
                self.current_zombie_lost_head = 0

            self.image = zombie_list[int(self.current_zombie_lost_head)]

    # Animation cho zombie khi chet
    def animation_zombie_dead(self, zombie_list):
        if self.current_zombie_dead < len(zombie_list) - 1:
            self.current_zombie_dead += constant.NUMBER_CHANGE_IMAGE_ZOMBIE
        else:
            self.kill()
            return
        self.image = zombie_list[int(self.current_zombie_dead)]

    def walk(self):
        self.animation(self.zombie_list)
        self.can_zombie_move = True

    def lost_head(self):
        self.animation_lost_head(self.zombie_lost_head_list)
        if not self.head_status:
            self.head()

    def head(self):
        self.head_status = True
        self.head_zombie.add(ZombieHead(self.rect.right, self.rect.bottom))

    def collisionCar(self):
        self.health = 0

    def die_zombie(self):
        self.zombie_attack = False
        self.can_zombie_move = False
        self.die = True
        self.animation_zombie_dead(self.zombie_die_list)

    def attack(self):
        self.animation(self.zombie_attack_list)

    def attack_lost_head(self):
        self.zombie_lost_head_attack = True
        self.animation(self.zombie_lost_head_attack_list)

    # Check cac trang thai animate cua zombie
    def check_animation_zombie(self):
        if self.health > 100:
            self.walk()
        elif 100 >= self.health > 10:
            self.lost_head()
            self.zombie_attack = False
        else:
            self.die_zombie()

    # collision voi plant
    def collisionPlant(self, plant):
        for item in plant:
            if pygame.sprite.collide_mask(self, item) and item.location_x == self.line:
                self.can_zombie_move = False
                if self.zombie_attack:
                    self.attack()
                else:
                    self.attack_lost_head()

                item.health -= self.damage_focus

                if self.health <= 0:
                    self.die_zombie()
                if item.health == 0:
                    item.kill()
                    check_map[item.location_x][item.location_y] = 0
                    self.zombie_lost_head_attack = False
                    self.can_zombie_move = True


class NormalZombie(Zombie):
    def __init__(self, x, line, name, health):
        super().__init__(x, line, name, health)

    def init_zombie_list(self):
        for i in range(0, 22):
            self.zombie_list.append(pygame.transform.scale(
                pygame.image.load("assets/Zombies/NormalZombie/Zombie/Zombie_" + str(i) + ".png").convert_alpha(),
                (166, 144)))

    def init_zombie_attack(self):
        for i in range(0, 21):
            self.zombie_attack_list.append(
                pygame.image.load(
                    "assets/Zombies/NormalZombie/ZombieAttack/ZombieAttack_" + str(i) + ".png").convert_alpha()
            )


class FlagZombie(Zombie):
    def __init__(self, x, line, name, health):
        super().__init__(x, line, name, health)
        self.damage_focus = 8
        self.health = health + 5

    def init_zombie_list(self):
        for i in range(0, 12):
            self.zombie_list.append(pygame.transform.scale(
                pygame.image.load("assets/Zombies/FlagZombie/FlagZombie/FlagZombie_" + str(i) + ".png").convert_alpha(),
                (166, 144)))

    def init_zombie_lost_head(self):
        for i in range(0, 12):
            self.zombie_lost_head_list.append(
                pygame.image.load(
                    "assets/Zombies/FlagZombie/FlagZombieLostHead/FlagZombieLostHead_" + str(
                        i) + ".png").convert_alpha()
            )

    def init_zombie_attack(self):
        for i in range(0, 11):
            self.zombie_attack_list.append(
                pygame.image.load(
                    "assets/Zombies/FlagZombie/FlagZombieAttack/FlagZombieAttack_" + str(i) + ".png").convert_alpha()
            )

    def init_zombie_lost_head_attack(self):
        for i in range(0, 11):
            self.zombie_lost_head_attack_list.append(
                pygame.image.load(
                    "assets/Zombies/FlagZombie/FlagZombieLostHeadAttack/FlagZombieLostHeadAttack_" + str(
                        i) + ".png").convert_alpha()
            )


class BucketheadZombie(Zombie):
    def __init__(self, x, line, name, health):
        super().__init__(x, line, name, health)
        self.damage_focus = 10
        self.health = health + 8

    def init_zombie_list(self):
        for i in range(0, 15):
            self.zombie_list.append(pygame.transform.scale(
                pygame.image.load("assets/Zombies/BucketheadZombie/BucketheadZombie/BucketheadZombie_" + str(
                    i) + ".png").convert_alpha(),
                (166, 144)))

    def init_zombie_attack(self):
        for i in range(0, 11):
            self.zombie_attack_list.append(
                pygame.image.load(
                    "assets/Zombies/BucketheadZombie/BucketheadZombieAttack/BucketheadZombieAttack_" + str(
                        i) + ".png").convert_alpha()
            )

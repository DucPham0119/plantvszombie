import random
import time

import pygame

import constant


class Zombie(pygame.sprite.Sprite):
    def __init__(self, x, line, name, head_group=None):
        super().__init__()

        self.zombie_list = []
        self.init_zombie_list("Zombie", 22)
        self.current_sprite = 0
        self.image = self.zombie_list[self.current_sprite]
        self.rect = self.image.get_rect()
        self.line = line
        y = constant.START_Y + (self.line - 1) * constant.LINE_Y + constant.LINE_Y // 2
        self.rect.topright = (x, y)

        self.name = name
        self.die = False
        self.damage_focus = 30
        self.health = 200
        self.can_move = True
        self.state = constant.WALK
        self.head_group = head_group
        self.losHead = False
        self.helmet = None

    def init_zombie_list(self, type_name, number):
        name = type_name + '/' + type_name + '_'
        for i in range(0, number):
            self.zombie_list.append(pygame.transform.scale(
                pygame.image.load("assets/Zombies/NormalZombie/"+name + str(i) + ".png"),
                (166, 144)))

    def update(self, plant):
        self.move()
        # self.handleState()
        self.animation()
        self.collisionPlant(plant)

    # def handleState(self):
    #     if self.state == constant.WALK:
    #         self.walking()
        # elif self.state == constant.ATTACK:
        #     self.attacking()
        # elif self.state == constant.DIE:
        #     self.dying()
        # elif self.state == constant.FREEZE:
        #     self.freezing()

    def move(self):
        if self.can_move:
            self.rect.x -= constant.NUMBER_CHANGE_MOVE_ZOMBIE

    def check_can_remove(self):
        return self.rect.x < constant.NUMBER_POSITION_CAN_REMOVE_ZOMBIE

    def animation(self):

        if self.current_sprite < len(self.zombie_list) - 1:
            self.current_sprite += constant.NUMBER_CHANGE_IMAGE_ZOMBIE
        else:
            self.current_sprite = 0

        self.image = self.zombie_list[int(self.current_sprite)]

    def collisionPlant(self, plant):
        for item in plant:
            if pygame.sprite.collide_mask(self, item):
                self.can_move = False
                item.health -= self.damage_focus
                if item.health == 0:
                    item.remove(plant)
                    self.can_move = True
                break

    # def walking(self):
    #     if self.health <= 0:
    #         self.setDie()
    #     # elif self.health <= constant.LOSTHEAD_HEALTH and not self.losHead:
    #         # self.changeFrames(self.losthead_walk_frames)
    #         # self.setLostHead()
    #     elif self.health <= constant.NORMAL_HEALTH and self.helmet:
    #         # self.changeFrames(self.walk_frames)
    #         self.helmet = False
    #         if self.name == constant.NEWSPAPER_ZOMBIE:
    #             self.speed = 2
    #
    #     # if (self.current_time - self.walk_timer) > (c.ZOMBIE_WALK_INTERVAL * self.getTimeRatio()):
    #     #     self.walk_timer = self.current_time
    #     #     if self.is_hypno:
    #     #         self.rect.x += self.speed
    #     #     else:
    #     #         self.rect.x -= self.speed

    # def attacking(self):
    #     if self.health <= 0:
    #         self.setDie()
    #     # elif self.health <= constant.LOSTHEAD_HEALTH and not self.losHead:
    #     #     # self.changeFrames(self.losthead_attack_frames)
    #     #     self.setLostHead()
    #     elif self.health <= constant.NORMAL_HEALTH and self.helmet:
    #         # self.changeFrames(self.attack_frames)
    #         self.helmet = False
    #     if (self.current_time - self.attack_timer) > (constant.ATTACK_INTERVAL * self.getTimeRatio()):
    #         if self.prey.health > 0:
    #             if self.prey_is_plant:
    #                 self.prey.setDamage(self.damage, self)
    #             else:
    #                 self.prey.setDamage(self.damage)
    #         self.attack_timer = self.current_time
    #
    #     if self.prey.health <= 0:
    #         self.prey = None
    #         self.setWalk()
    #
    # def dying(self):
    #     pass

    # def freezing(self):
    #     if self.health <= 0:
    #         self.setDie()
    #     elif self.health <= constant.LOSTHEAD_HEALTH and not self.losHead:
    #         if self.old_state == constant.WALK:
    #             # self.changeFrames(self.losthead_walk_frames)
    #             self.init_zombie_list("ZombieLostHead", 18)
    #             self.current_sprite = 0
    #         else:
    #             # self.changeFrames(self.losthead_attack_frames)
    #             self.init_zombie_list("ZombieLostHeadAttack", 11)
    #             self.current_sprite = 0
            # self.setLostHead()
        # if (self.current_time - self.freeze_timer) > constant.FREEZE_TIME:
        #     self.setWalk()

    def setDie(self):
        self.state = constant.DIE
        # self.animate_interval = 200
        # set ảnh chết
        self.init_zombie_list("ZombieDie", 10)

    # def setLostHead(self):
    #     self.losHead = True
    #     if self.head_group is not None:
    #         self.head_group.add(ZombieHead(self.rect.centerx, self.rect.bottom))
# from Sun import Sun
#
#
# class Zombie(pygame.sprite.Sprite):
#     def __init__(self, x, line, name, health, sun_group, head_group=None, damage=1):
#         pygame.sprite.Sprite.__init__(self)
#
#         self.name = name
#         self.zombie_list = []
#         self.init_zombie_list("Zombie", 22)
#         self.current_sprite = 0
#         self.image = self.zombie_list[self.current_sprite]
#         self.rect = self.image.get_rect()
#         self.line = line
#         y = constant.START_Y + (self.line - 1) * constant.LINE_Y + constant.LINE_Y // 2
#         self.rect.topright = (x, y)
#
#         self.health = health
#         self.damage = damage
#         self.dead = False
#         self.losHead = False
#         self.helmet = False
#         self.head_group = head_group
#         self.sun_group = sun_group
#
#         self.walk_timer = 0
#         self.animate_timer = 0
#         self.attack_timer = 0
#         self.state = constant.WALK
#         self.animate_interval = 150
#         self.ice_slow_ratio = 1
#         self.ice_slow_timer = 0
#         self.hit_timer = 0
#         self.speed = 1
#         self.freeze_timer = 0
#         self.is_hypno = False  # the zombie is hypo and attack other zombies when it ate a HypnoShroom
#
#     def init_zombie_list(self, type_name, number):
#         name = type_name + '/' + type_name + '_'
#         for i in range(0, number):
#             self.zombie_list.append(pygame.transform.scale(
#                 pygame.image.load("assets/Zombies/NormalZombie/" + name + str(i) + ".png"),
#                 (166, 144)))
#
#     def update(self):
#         self.current_time = time.time_ns()
#         self.handleState()
#         self.updateIceSlow()
#         self.animation()
#
#     def handleState(self):
#         if self.state == constant.WALK:
#             self.walking()
#         elif self.state == constant.ATTACK:
#             self.attacking()
#         elif self.state == constant.DIE:
#             self.dying()
#         elif self.state == constant.FREEZE:
#             self.freezing()
#
#     def check_can_remove(self):
#         return self.rect.x < constant.NUMBER_POSITION_CAN_REMOVE_ZOMBIE
#
#     def walking(self):
#         if self.health <= 0:
#             self.setDie()
#         elif self.health <= constant.LOSTHEAD_HEALTH and not self.losHead:
#             # self.changeFrames(self.losthead_walk_frames)
#             self.init_zombie_list("ZombieLostHead", 18)
#             self.current_sprite = 0
#             self.setLostHead()
#         elif self.health <= constant.NORMAL_HEALTH and self.helmet:
#             # self.changeFrames(self.walk_frames)
#             self.init_zombie_list("Zombie", 18)
#             self.current_sprite = 0
#             self.helmet = False
#             if self.name == constant.NEWSPAPER_ZOMBIE:
#                 self.speed = 2
#
#         if (self.current_time - self.walk_timer) > (constant.ZOMBIE_WALK_INTERVAL * self.getTimeRatio()):
#             self.walk_timer = self.current_time
#             if self.is_hypno:
#                 self.rect.x += self.speed
#             else:
#                 self.rect.x -= self.speed
#
#     def attacking(self):
#         if self.health <= 0:
#             self.setDie()
#         elif self.health <= constant.LOSTHEAD_HEALTH and not self.losHead:
#             # self.changeFrames(self.losthead_attack_frames)
#             self.init_zombie_list("ZombieLostHeadAttack", 11)
#             self.current_sprite = 0
#             self.setLostHead()
#         elif self.health <= constant.NORMAL_HEALTH and self.helmet:
#             # self.changeFrames(self.attack_frames)
#             self.init_zombie_list("ZombieAttack", 21)
#             self.current_sprite = 0
#             self.helmet = False
#         if (self.current_time - self.attack_timer) > (constant.ATTACK_INTERVAL * self.getTimeRatio()):
#             if self.prey.health > 0:
#                 if self.prey_is_plant:
#                     self.prey.setDamage(self.damage, self)
#                 else:
#                     self.prey.setDamage(self.damage)
#             self.attack_timer = self.current_time
#
#         if self.prey.health <= 0:
#             self.prey = None
#             self.setWalk()
#
#     def dying(self):
#         pass
#
#     def freezing(self):
#         if self.health <= 0:
#             self.setDie()
#         elif self.health <= constant.LOSTHEAD_HEALTH and not self.losHead:
#             if self.old_state == constant.WALK:
#                 # self.changeFrames(self.losthead_walk_frames)
#                 self.init_zombie_list("ZombieLostHead", 18)
#                 self.current_sprite = 0
#             else:
#                 # self.changeFrames(self.losthead_attack_frames)
#                 self.init_zombie_list("ZombieLostHeadAttack", 11)
#                 self.current_sprite = 0
#             self.setLostHead()
#         if (self.current_time - self.freeze_timer) > constant.FREEZE_TIME:
#             self.setWalk()
#
#     def setLostHead(self):
#         self.losHead = True
#         if self.head_group is not None:
#             self.head_group.add(ZombieHead(self.rect.centerx, self.rect.bottom))
#
#     # def changeFrames(self, frames):
#     #     '''change image frames and modify rect position'''
#     #     self.frames = frames
#     #     self.frame_num = len(self.frames)
#     #     self.frame_index = 0
#     #
#     #     bottom = self.rect.bottom
#     #     centerx = self.rect.centerx
#     #     self.image = self.frames[self.frame_index]
#     #     self.rect = self.image.get_rect()
#     #     self.rect.bottom = bottom
#     #     self.rect.centerx = centerx
#
#     def animation(self):
#         if self.state == constant.FREEZE:
#             self.image.set_alpha(192)
#             return
#
#         if (self.current_time - self.animate_timer) > (self.animate_interval * self.getTimeRatio()):
#             self.current_sprite += 1
#             if self.current_sprite >= len(self.zombie_list):
#                 if self.state == constant.DIE:
#                     x = random.randint(200, 900)
#                     des_y = random.randint(200, 550)
#                     self.sun_group.add(Sun(x, 0, des_y))
#                     self.kill()
#                     return
#                 self.current_sprite = 0
#             self.animate_timer = self.current_time
#
#         self.image = self.zombie_list[self.current_sprite]
#         if self.is_hypno:
#             self.image = pygame.transform.flip(self.image, True, False)
#         if (self.current_time - self.hit_timer) >= 200:
#             self.image.set_alpha(255)
#         else:
#             self.image.set_alpha(192)
#
#     def getTimeRatio(self):
#         return self.ice_slow_ratio
#
#     def setIceSlow(self):
#         """when get a ice bullet damage, slow the attack or walk speed of the zombie"""
#         self.ice_slow_timer = self.current_time
#         self.ice_slow_ratio = 2
#
#     def updateIceSlow(self):
#         if self.ice_slow_ratio > 1:
#             if (self.current_time - self.ice_slow_timer) > constant.ICE_SLOW_TIME:
#                 self.ice_slow_ratio = 1
#
#     def setDamage(self, damage, ice=False):
#         self.health -= damage
#         self.hit_timer = self.current_time
#         if ice:
#             self.setIceSlow()
#
#     def setWalk(self):
#         self.state = constant.WALK
#         self.animate_interval = 150
#
#         if self.losHead:
#             # self.changeFrames(self.losthead_walk_frames)
#             self.init_zombie_list("ZombieLostHead", 18)
#             self.current_sprite = 0
#         else:
#             # self.changeFrames(self.walk_frames)
#             self.init_zombie_list("Zombie", 22)
#             self.current_sprite = 0
#
#     def setAttack(self, prey, is_plant=True):
#         self.prey = prey  # prey can be plant or other zombies
#         self.prey_is_plant = is_plant
#         self.state = constant.ATTACK
#         self.attack_timer = self.current_time
#         self.animate_interval = 100
#
#         # if self.helmet:
#         #     self.changeFrames(self.helmet_attack_frames)
#         if self.losHead:
#             # self.changeFrames(self.losthead_attack_frames)
#             self.init_zombie_list("ZombieLostHeadAttack", 11)
#             self.current_sprite = 0
#         else:
#             # self.changeFrames(self.attack_frames)
#             self.init_zombie_list("ZombieAttack", 21)
#             self.current_sprite = 0
#
#     def setDie(self):
#         self.state = constant.DIE
#         self.animate_interval = 200
#         # set ảnh chết
#         # self.changeFrames(self.die_frames)
#         self.init_zombie_list("ZombieDie", 10)
#         self.current_sprite = 0
#
#     def setBoomDie(self):
#         self.state = constant.DIE
#         self.animate_interval = 200
#         # self.changeFrames(self.boomdie_frames)
#         self.init_zombie_list("BoomDie", 20)
#         self.current_sprite = 0
#
#     def setFreeze(self, ice_trap_image):
#         self.old_state = self.state
#         self.state = constant.FREEZE
#         self.freeze_timer = self.current_time
#         self.ice_trap_image = ice_trap_image
#         self.ice_trap_rect = ice_trap_image.get_rect()
#         self.ice_trap_rect.centerx = self.rect.centerx
#         self.ice_trap_rect.bottom = self.rect.bottom
#
#     def drawFreezeTrap(self, surface):
#         if self.state == constant.FREEZE:
#             surface.blit(self.ice_trap_image, self.ice_trap_rect)
#
#     def setHypno(self):
#         self.is_hypno = True
#         self.setWalk()
#
#
# class ZombieHead(Zombie):
#     def __init__(self, x, y):
#         Zombie.__init__(self, x, y, "ZombieHead", 0)
#         self.state = constant.DIE
#
#     def init_zombie_list(self, type_name, number):
#         name = type_name + '/' + type_name + '_'
#         for i in range(0, number):
#             self.zombie_list.append(pygame.transform.scale(
#                 pygame.image.load("assets/Zombies/NormalZombie/" + name + str(i) + ".png"),
#                 (166, 144)))
#
#     def setWalk(self):
#         self.animate_interval = 100

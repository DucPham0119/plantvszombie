import pygame

import constant
from Card import Card
from config import plant_name_list


def getSunValueImage(sun_value):
    font = pygame.font.SysFont(None, 22)
    width = 32
    # lấy gtrị, màu
    msg_image = font.render(str(sun_value), True, constant.NAVYBLUE, constant.LIGHTYELLOW)
    msg_rect = msg_image.get_rect()
    msg_w = msg_rect.width

    image = pygame.Surface([width, 17])
    x = width - msg_w

    image.fill(constant.LIGHTYELLOW)
    image.blit(msg_image, (x, 0), (0, 0, msg_rect.w, msg_rect.h))
    image.set_colorkey(constant.BLACK)
    return image


class MenuBar:
    def __init__(self, sun_value, card_list):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load("assets/Background/ChooserBackground.png").convert_alpha(), (522, 87))
        self.rect = self.image.get_rect()
        self.rect.x = 200
        self.rect.y = 0
        self.sun_value = sun_value
        self.card_list = card_list
        self.card_offset_x = 220
        self.setupCards(card_list)

    def update(self, current_time):
        self.current_time = current_time
        for card in self.card_list:
            card.update(self.current_time)
            self.openCard(card, self.current_time)

    def setupCards(self, card_list):
        self.card_list = []
        x = self.card_offset_x
        y = 8
        for index in range(0, len(card_list)):
            x += 55
            self.card_list.append(Card(x, y, index))
            print(self.card_list[index].rect)

    def checkCardClick(self, mouse_pos):
        result = None
        for card in self.card_list:
            if card.checkMouseClick(mouse_pos):
                if card.canClick(self.sun_value, self.current_time):
                    result = (plant_name_list[card.name_index], card)
                break
        return result

    def checkMenuBarClick(self, mouse_pos):
        x, y = mouse_pos
        if self.rect.collidepoint(x, y):
            print('click')
            return True
        return False

    def decreaseSunValue(self, value):
        self.sun_value -= value

    def increaseSunValue(self, value):
        self.sun_value += value

    def setCardFrozenTime(self, plant_name):
        for card in self.card_list:
            if plant_name_list[card.name_index] == plant_name:
                card.setFrozenTime(self.current_time)
                break

    def openCard(self, card, current_time):
        # for card in self.card_list:
        if card.canClick(self.sun_value, current_time):
            card.image.set_alpha(250)
        elif not card.canClick(self.sun_value, current_time):
            card.image.set_alpha(120)
        # else:
        #     card.image.set_alpha(120)

    def drawSunValue(self):
        self.value_image = getSunValueImage(self.sun_value)
        self.value_rect = self.value_image.get_rect()
        self.value_rect.x = 21
        self.value_rect.y = self.rect.bottom - 21

        self.image.blit(self.value_image, self.value_rect)

    def draw(self, surface):
        self.drawSunValue()
        surface.blit(self.image, self.rect)
        for card in self.card_list:
            card.draw(surface)

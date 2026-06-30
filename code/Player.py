from code.Const import WIN_HEIGHT, WIN_WIDTH
from code.Entity import Entity

import pygame as pg


class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self, aux_counter):
        pressed_key = pg.key.get_pressed()

        if pressed_key[pg.K_UP] and self.rect.top > 100:
            self.rect.centery -= 1

        if pressed_key[pg.K_DOWN] and self.rect.bottom < WIN_HEIGHT:
            self.rect.centery += 1

        if pressed_key[pg.K_LEFT] and self.rect.left > 0:
            self.rect.centerx -= 1

        if pressed_key[pg.K_RIGHT] and self.rect.right < WIN_WIDTH:
            self.rect.centerx += 1

        pass

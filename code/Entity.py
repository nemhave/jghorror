from abc import ABC, abstractmethod

import pygame as pg

from code.Const import ENTITY_VISIBLE


class Entity(ABC):
    def __init__(self, name: str, position: tuple):
        self.name = name
        self.surf = pg.image.load('./asset/level/' + name + '.png').convert_alpha()
        self.rect = self.surf.get_rect(left=ENTITY_VISIBLE[self.name], top=position[1])
        self.speed = 0

    @abstractmethod
    def move(self, aux_counter):
        pass

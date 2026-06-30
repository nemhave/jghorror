from code.AudioManager import AudioManager
from code.Const import PLAYLIST
from code.Entity import Entity
from code.EntityFactory import EntityFactory

import pygame as pg


class Level:
    def __init__(self, window, name):
        self.window = window
        self.name = name
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('Level1Bg'))

    def run(self):
        AudioManager.change_music(PLAYLIST["Level"])
        clock = pg.time.Clock()
        aux_counter = 0
        while True:
            clock.tick(60)
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move(aux_counter)
            pg.display.flip()

            if aux_counter > 12000:
                aux_counter = 0

            aux_counter += 1

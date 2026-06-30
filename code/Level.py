from pygame import Surface, Rect
from pygame.font import Font

from code.AudioManager import AudioManager
from code.Const import PLAYLIST, WIN_HEIGHT, COLOR_WHITE, TIMEOUT_LEVEL, EVENT_ENEMY
from code.Entity import Entity
from code.EntityFactory import EntityFactory

import pygame as pg


class Level:
    def __init__(self, window, name):
        self.timeout = TIMEOUT_LEVEL
        self.window = window
        self.name = name
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('Level1Bg'))
        self.entity_list.append(EntityFactory.get_entity('Player1'))

        pg.time.set_timer(EVENT_ENEMY, 2000)

    def run(self):
        AudioManager.change_music(PLAYLIST["Level"])
        clock = pg.time.Clock()
        aux_counter = 0
        while True:
            clock.tick(60)
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move(aux_counter)

            if aux_counter > 720:
                aux_counter = 0

            aux_counter += 1

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    quit()
                if event.type == EVENT_ENEMY:
                    self.entity_list.append(EntityFactory.get_entity('Enemy1'))

            # self.level_text(14, f'{self.name} - Timeout: {self.timeout / 1000:.1f}s', COLOR_WHITE, (10, 5))
            self.level_text(14, f'fps: {clock.get_fps():.0f}', COLOR_WHITE, (10, WIN_HEIGHT - 35))

            pg.display.flip()

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pg.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)
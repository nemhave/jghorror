import pygame as pg
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import WIN_WIDTH, COLOR_TITLE, COLOR_OPTION, MENU_OPTION, POS_INIT_MENU


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pg.image.load('./asset/MenuBg.png')
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self):
        pg.mixer_music.load('./asset/Menu.mp3')
        pg.mixer_music.play(-1)
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(90, "HorrorFight", COLOR_TITLE, ((WIN_WIDTH / 2), POS_INIT_MENU))

            for n in range(len(MENU_OPTION)):
                self.menu_text(60, MENU_OPTION[n], COLOR_OPTION, ((WIN_WIDTH / 2), POS_INIT_MENU+20+(50*(n+1))))

            pg.display.flip()

            # check for all events
            for event in pg.event.get():
                if event.type == pg.QUIT:  # close window
                    pg.quit()  # close cod

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pg.font.SysFont(name="Chiller", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)

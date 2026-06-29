import pygame as pg
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import WIN_WIDTH, COLOR_TITLE, MENU_OPTION, POS_INIT_MENU, COLOR_OPTION_DEFAULT, \
    COLOR_OPTION_SELECT


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pg.image.load('./asset/MenuBg.png')
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self):
        pg.mixer_music.load('./asset/Menu.mp3')
        pg.mixer_music.play(-1)

        menu_select = 0

        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(90, "HorrorFight", COLOR_TITLE, ((WIN_WIDTH / 2), POS_INIT_MENU))

            for n in range(len(MENU_OPTION)):
                if n == menu_select:
                    cor_select = COLOR_OPTION_SELECT
                    size_select = 70
                else:
                    cor_select = COLOR_OPTION_DEFAULT
                    size_select = 50

                self.menu_text(size_select, MENU_OPTION[n], cor_select,
                               ((WIN_WIDTH / 2), POS_INIT_MENU + 20 + (50 * (n + 1))))

            # check for all events
            for event in pg.event.get():
                if event.type == pg.QUIT:  # close window
                    pg.quit()  # close cod
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_DOWN:
                        menu_select = (menu_select + 1) % len(MENU_OPTION)
                    elif event.key == pg.K_UP:
                        menu_select = (menu_select - 1) % len(MENU_OPTION)
                    elif event.key == pg.K_RETURN:
                        return MENU_OPTION[menu_select]

            pg.display.flip()

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pg.font.SysFont(name="Chiller", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)

import pygame as pg


class AudioManager:

    @staticmethod
    def change_music(name):
        if pg.mixer_music.get_busy():
            # pg.mixer_music.stop()
            pg.mixer_music.fadeout(1000)

        pg.mixer_music.unload()  # Libera o arquivo anterior da memória
        pg.mixer_music.load(name)
        pg.mixer_music.play(-1)

# C
import pygame

COLOR_TITLE = (255, 30, 30)
COLOR_OPTION_DEFAULT = (255, 80, 0)
COLOR_OPTION_SELECT = (255, 201, 15)
COLOR_WHITE = (255, 255, 255)

PLAYLIST = {
    "Menu": "./asset/Menu.mp3",
    "Select": "./asset/Select.flac",
    "Level": "./asset/level.wav"
}

# E
ENTITY_VISIBLE = {
    'Level1Bg0': 0,
    'Level1Bg1': -186,
    'Level1Bg2': -278,
    'Level1Bg3': -371,
    'Level1Bg4': -464,
    'Level1Bg5': -557,
    'Player1': 0,
    'Enemy1': 0,
    'Enemy2': 0,
}

ENTITY_MOVE = {
    'Level1Bg0': 60,
    'Level1Bg1': 120,
    'Level1Bg2': 180,
    'Level1Bg3': 240,
    'Level1Bg4': 300,
    'Level1Bg5': 360,
}

EVENT_ENEMY = pygame.USEREVENT + 1

# M
MENU_OPTION = ('Start Game',
               'Choose Game',
               'Quit Game')

MENU_HELP = ('Pressione [Setas] para Navegar menu / Mover personagem',
             'Pressione [Enter] para escolha',
             'Quit Game')

# W
WIN_WIDTH = 768
WIN_HEIGHT = 432

# P
POS_INIT_MENU = 100

# T
TIMEOUT_STEP = 100  # 100ms
TIMEOUT_LEVEL = 20000  # 20s

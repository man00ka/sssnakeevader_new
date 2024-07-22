# SCALING AND FPS
import pygame
import pygame_menu

pygame.font.init()

FULL_SCALE = 0
SCALE = 1
FPS = 60

# DISPLAY INFORMATION
# Noch anpassen, damit 1080p ganzzalig dadurch Teilbar ist
# was aber auch wieder änderungen an der Anzahl Grass-Tiles
# bedeutet
NATIVE_WIDTH = 816
NATIVE_HEIGHT = 612
NATIVE_SIZE = (NATIVE_WIDTH, NATIVE_HEIGHT)
NATIVE_WIDTH_CENTER = NATIVE_WIDTH // 2
NATIVE_HEIGHT_CENTER = NATIVE_HEIGHT // 2
NATIVE_CENTER = (NATIVE_WIDTH_CENTER, NATIVE_HEIGHT_CENTER)
NATIVE_TOP = 0
NATIVE_RIGHT = NATIVE_WIDTH
NATIVE_BOTTOM = NATIVE_HEIGHT
NATIVE_LEFT = 0
NATIVE_TOP_LEFT = (NATIVE_LEFT, NATIVE_TOP)
NATIVE_TOP_CENTER = (NATIVE_WIDTH_CENTER, NATIVE_TOP)
NATIVE_TOP_RIGHT = (NATIVE_WIDTH, NATIVE_TOP)
NATIVE_RIGHT_CENTER = (NATIVE_WIDTH, NATIVE_HEIGHT_CENTER)
NATIVE_BOTTOM_RIGHT = NATIVE_SIZE
NATIVE_BOTTOM_CENTER = (NATIVE_WIDTH_CENTER, NATIVE_BOTTOM)
NATIVE_BOTTOM_LEFT = (NATIVE_LEFT, NATIVE_BOTTOM)
NATIVE_LEFT_CENTER = (NATIVE_LEFT, NATIVE_HEIGHT_CENTER)

# If we scale the display we would do the same as above but
# with a scaling factor, e.g.:
# DISPLAY_WIDTH = NATIVE_WIDTH * SCALE etc.
DISPLAY_WIDTH = 816 * SCALE
DISPLAY_HEIGHT = 612 * SCALE
DISPLAY_SIZE = (DISPLAY_WIDTH, DISPLAY_HEIGHT)
DISPLAY_WIDTH_CENTER = DISPLAY_WIDTH // 2
DISPLAY_HEIGHT_CENTER = DISPLAY_HEIGHT // 2
DISPLAY_CENTER = (DISPLAY_WIDTH_CENTER, DISPLAY_HEIGHT_CENTER)
DISPLAY_TOP = 0
DISPLAY_RIGHT = DISPLAY_WIDTH
DISPLAY_BOTTOM = DISPLAY_HEIGHT
DISPLAY_LEFT = 0
DISPLAY_TOP_LEFT = (DISPLAY_LEFT, DISPLAY_TOP)
DISPLAY_TOP_CENTER = (DISPLAY_WIDTH_CENTER, DISPLAY_TOP)
DISPLAY_TOP_RIGHT = (DISPLAY_WIDTH, DISPLAY_TOP)
DISPLAY_RIGHT_CENTER = (DISPLAY_WIDTH, DISPLAY_HEIGHT_CENTER)
DISPLAY_BOTTOM_RIGHT = DISPLAY_SIZE
DISPLAY_BOTTOM_CENTER = (DISPLAY_WIDTH_CENTER, DISPLAY_BOTTOM)
DISPLAY_BOTTOM_LEFT = (DISPLAY_LEFT, DISPLAY_BOTTOM)
DISPLAY_LEFT_CENTER = (DISPLAY_LEFT, DISPLAY_HEIGHT_CENTER)

# GAME STATE INFORMATION
STATE_SPLASH_SCREEN = "SPLASH_SCREEN"
STATE_MAIN_MENU = "MAIN_MENU"
STATE_PLAY = "PLAY"
STATE_PAUSE = "PAUSE"
STATE_GAME_OVER = "GAME_OVER"
GAME_STATES = [
    STATE_SPLASH_SCREEN,
    STATE_MAIN_MENU,
    STATE_PLAY,
    STATE_PAUSE,
    STATE_GAME_OVER,
]
STARTING_STATE = GAME_STATES[0]

# TILE INFORMATION
    # SMALLE_TILE_SIZE = ...
    # MEDIUM_TILE_SIZE = ...
    # LARGE_TILE_SIZE = ...

# VELOCITY INFORMATION
SPEED_BACKGROUND = -1  # Because we move from right to left, we need a negative value
SPEED_INCREMENT = 0.25
SLOW_DOWN_FACTOR = 0.75  # Percent to slow down when number of enemies is increased
INITIAL_SPEED_FACTOR = 1.0
VELOCITY_PLAYER_MOVEMENT = 5

# ENEMY INFORMATION
INITIAL_NUM_ENEMIES = 4
DEFAULT_ENEMY_INCREMENT = 1

# DIFFICULTY INFORMATION
TIME_UNTIL_SPEED_INCREASE = 15  # Seconds
TIME_UNTIL_MORE_ENEMIES = 60  # Seconds

# FONT INFORMATION
FONT_8BIT = pygame_menu.font.FONT_8BIT
FONT_COURIER_30 = pygame.font.SysFont("Courier", 30)

# MENU INFORMATION
MENU_FONT = pygame_menu.font.FONT_8BIT
MENU_THEME = pygame_menu.themes.THEME_SOLARIZED.copy()
MENU_THEME.widget_font = MENU_FONT
MENU_WIDTH = DISPLAY_WIDTH * 0.75
MENU_HEIGHT = DISPLAY_HEIGHT * 0.75
MENU_SIZE = (MENU_WIDTH, MENU_HEIGHT)



# DIRECTORY INFORMATION
DIR_FONTS = "fonts"
DIR_IMG = "img"  # Image directory needs to stay named 'img' to do the web build
DIR_MUSIC = "music"
DIR_SOUNDS = "sounds"


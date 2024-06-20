import pygame
import constants as c
from main_menu import MainMenu
from game_state_splash import GameStateSplash
from game_state_play import GameStatePlay
from game_state_pause import GameStatePause
from controller import Controller
from graphicsmanager import GraphicsManager

pygame.init()

def get_display():
    display = pygame.display.set_mode(c.DISPLAY_SIZE)  # Try parameter 'vsync=1' some time.
    return display

def get_graphics_manager():
    graphics_manager = GraphicsManager()
    return graphics_manager

def get_clock():
    clock = pygame.time.Clock()
    return clock


def get_game_states():
    # This dict will contain all the different game states
    game_states = {
        c.STATE_SPLASH_SCREEN: GameStateSplash,
        c.STATE_MAIN_MENU: MainMenu,
        c.STATE_PLAY: GameStatePlay,
        c.STATE_PAUSE: GameStatePause
    }
    return game_states

def get_controller(display, graphics_manager, clock, game_states, starting_state):
    controller = Controller(display, graphics_manager, clock, game_states, starting_state)
    return controller

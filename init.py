import pygame
import constants as c
from main_menu import MainMenu
from splash_screen import SplashScreen
from controller import Controller

pygame.init()

def get_display():
    display = pygame.display.set_mode(c.DISPLAY_SIZE)
    return display


def get_clock():
    clock = pygame.time.Clock()
    return clock


def get_game_states():
    # This dict will contain all the different game states
    game_states = {
        c.STATE_SPLASH_SCREEN: SplashScreen,
        c.STATE_MAIN_MENU: MainMenu,
    }
    return game_states


def get_controller(display, clock, game_states, starting_state):
    controller = Controller(display, clock, game_states, starting_state)
    return controller

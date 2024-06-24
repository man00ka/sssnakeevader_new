import pygame
import constants as c
from subscription import Subscriber

# EventHandler inherits from Subject, to add the functionality of notifying
# different game states (subscribers) about a key press for example.
from subscription import Subject
from pygame.locals import (KEYDOWN,
                           QUIT,
                           K_ESCAPE,
                           K_SPACE,
                           K_RETURN,
                           K_w,
                           K_a,
                           K_s,
                           K_d,
                           K_p,)


class EventHandler:
    def __init__(self, controller):
        self.controller = controller

    def handle_events(self):
        # The pressed keys contain the currently held down keys
        # which is necessary for continues movement of the player
        # character. If we used a key *event* for that, the player
        # character would move only once per button press. For menus,
        # however, this is a desired behaviour, so wie evaluate *only*
        # the keys for player movement and leave the key event logic
        # for menu navigation, play, pause, quit game, etc.
        pressed_keys = pygame.key.get_pressed()
        self.check_player_movement(pressed_keys)
        # self.check_joystick_event(pressed_keys)

        # The following evaluations happen only once per key press
        for event in pygame.event.get():
            self.check_quit_event(event)
            self.check_keyboard_event(event)

    def check_quit_event(self, event):
        if event.type == QUIT:
            pygame.quit()
            quit()  # I don't know why wie need this here.

    def check_player_movement(self, pressed_keys):
        if pressed_keys[K_w]:
            self.controller.current_state.on_key_press_W()
        if pressed_keys[K_a]:
            self.controller.current_state.on_key_press_A()
        if pressed_keys[K_s]:
            self.controller.current_state.on_key_press_S()
        if pressed_keys[K_d]:
            self.controller.current_state.on_key_press_D()

    def check_keyboard_event(self, event):
        if event.type == KEYDOWN:
            if event.key == K_p:
                self.controller.current_state.on_key_press_P()
            if event.key == K_ESCAPE:
                self.controller.current_state.on_key_press_ESCAPE()
            if event.key == K_SPACE:
                self.controller.current_state.on_key_press_SPACE()
            if event.key == K_RETURN:
                self.controller.current_state.on_key_press_RETURN()

    def check_joystick_event(self, event):
        pass


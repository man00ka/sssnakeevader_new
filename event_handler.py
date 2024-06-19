import pygame
import constants as c

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


class EventHandler():
    def __init__(self, controller):
        self.controller = controller

    def handle_events(self):
        for event in pygame.event.get():
            self.check_quit_event(event)
            self.check_keyboard_event(event)
            self.check_joystick_event(event)

    def check_quit_event(self, event):
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            pygame.quit()
            quit()  # I don't know why wie need this here.

    def check_keyboard_event(self, event):
        if event.type == KEYDOWN:
            if event.key == K_w:
                self.controller.current_state.on_key_press_W()
            if event.key == K_a:
                self.controller.current_state.on_key_press_A()
            if event.key == K_s:
                self.controller.current_state.on_key_press_S()
            if event.key == K_d:
                self.controller.current_state.on_key_press_D()
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

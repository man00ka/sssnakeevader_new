import pygame
import constants as c
import init

class EventHandler():
    def __init__(self):
        pass

    def handle_events(self, controller):
        for event in pygame.event.get():
            self.check_quit_event(event)
            self.check_keyboard_event(event, controller)
            self.check_joystick_event(event, controller)

    def check_quit_event(self, event):
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            pygame.quit()
            quit()  # I don't know why wie need this here.

    def check_keyboard_event(self, event, controller):
        if event.type == pygame.KEYDOWN:
            if (controller.current_state.name == c.STATE_SPLASH_SCREEN
                    and event.key == pygame.K_SPACE):
                controller.current_state = controller.game_states[c.STATE_PLAY].get_instance(controller.graphics_manager)
    def check_joystick_event(self, event, controller):
        pass
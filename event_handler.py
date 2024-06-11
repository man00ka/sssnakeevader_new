import pygame


class EventHandler():
    def __init__(self):
        pass

    def handle_events(self):
        for event in pygame.event.get():
            self.check_quit_event(event)
            self.check_keyboard_event(event)
            self.check_joystick_event(event)  # maybe rename to controller event

    def check_quit_event(self, event):
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN
                                         and event.key == pygame.K_ESCAPE):
            pygame.quit()
            quit()  # warum?

    def check_keyboard_event(self, event):
        pass

    def check_joystick_event(self, event):
        pass
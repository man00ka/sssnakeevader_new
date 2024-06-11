import constants as c
from event_handler import EventHandler
class Controller():
    def __init__(self, display, clock, game_states, starting_state):
        self.display = display
        self.clock = clock
        self.game_states = game_states
        self.current_state = self.game_states[starting_state](display)
        self.event_handler = EventHandler()

    def run_game(self):
        while True:
            # Tick Clock
            self.clock.tick(c.FPS)

            # Handle Events
            self.event_handler.handle_events()



            # Update State
            self.current_state.update()


            # Render State
            self.current_state.render(self.display)
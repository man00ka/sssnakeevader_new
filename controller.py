import constants as c
from event_handler import EventHandler
class Controller():
    def __init__(self, display, graphics_manager, clock, game_states, starting_state):
        self.display = display
        self.graphics_manager = graphics_manager  # Rename to assets_manager?
        self.clock = clock
        self.game_states = game_states
        self.current_state = self.game_states[starting_state](self)
        self.event_handler = EventHandler(self)

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


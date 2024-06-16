# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import init
import constants as c


def main():
    display = init.get_display()
    clock = init.get_clock()
    game_states = init.get_game_states()
    graphics_manager = init.get_graphics_manager()
    controller = init.get_controller(display, graphics_manager, clock, game_states, c.STARTING_STATE)
    controller.run_game()


if __name__ == '__main__':
    main()
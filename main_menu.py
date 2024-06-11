import pygame_menu
from game_state import GameState
import constants as c

class MainMenu(pygame_menu.Menu, GameState):
    def __init__(self, controller):
        super(MainMenu, self).__init__('Welcome', 600, 400,
                                       theme=c.MENU_THEME,
                                       onclose=pygame_menu.events.CLOSE
                                       )
        self.controller = controller
        self.add.text_input('Name: ', default='username', maxchar=20)
        self.add.button('Play', self.start_the_game)
        self.add.button('Levels', self.level_menu)
        self.add.button('Quit', pygame_menu.events.EXIT)

        difficulty_level = pygame_menu.Menu('Select a Difficulty', 600, 400,
                                            theme=c.MENU_THEME)
        difficulty_level.add.selector('Difficulty:',
                                      [('Hard', 1), ('Easy', 2)],
                                      onchange=self.set_difficulty
                                      )

    def update(self):
        # Implemented by pygame_menu.Menu
        pass

    def set_difficulty(self, value, difficulty):
        print(value)
        print(difficulty)

    def start_the_game(self):
        # To start the game we simply close the main menu which fires
        # the onclose event `pygame_menu.events.CLOSE`.
        self.close()
        # And change the game state to 'Play'
        self.controller.change_state(c.STATE_PLAY)


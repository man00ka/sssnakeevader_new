from pygame.time import Clock
import constants as c
from time import sleep

class DifficultyManager:
    # TODO:
    #  - update game-time-events
    #  - update game time in game_state_play
    #  before updating difficulty Manager
    def __init__(self, game_state_play):
        self._game_state_play = game_state_play
        self._num_speed_increases = 0
        self._frames_passed = 0
        self._GO_FASTER = False
        self._MORE_ENEMIES = False

    def update(self):
        """This will check in every frame if enough in-game time has passed
        to trigger different events for increasing difficulty."""
        self._check_for_timed_events()
        self._frames_passed += 1

    def _check_for_timed_events(self):
        """This will check if enough time has passed for any timed event to
        trigger. It will take the appropriate action if so and also reset the
        event timers."""

        # Every `c.TIME_UNTIL_MORE_ENEMIES` seconds MORE_ENEMIES is reset to False

        if self._game_state_play.ingame_time.sec_total > 0:
            # We don't want to increase enemies or speed if the game time is still zero!

            self._MORE_ENEMIES = (self._game_state_play
                                  .ingame_time
                                  .sec_total) % (c.TIME_UNTIL_MORE_ENEMIES) == 0
            self._GO_FASTER = (self._game_state_play
                               .ingame_time
                               .sec_total) % (c.TIME_UNTIL_SPEED_INCREASE) == 0

        # TODO: Make enemies spawn richtig
        # TODO: git commit --ammend ausführen

        TARGET_FPS_PASSED = self._frames_passed % c.FPS == 0

        if self._MORE_ENEMIES and TARGET_FPS_PASSED:
            self._increase_enemies()
            # print(f"{self._game_state_play.ingame_time._text} - MORE_ENEMIES")

        if self._GO_FASTER and TARGET_FPS_PASSED and not self._MORE_ENEMIES:
            self._increase_speed()
            # print(f"{self._game_state_play.ingame_time._text} - GO_FASTER")

    def _increase_speed(self):
        """This will increment the velocity for new enemies (and the background).
        Existing enemies will stay on the same velocity for now."""
        # TODO: Should we also increase the players velocity? --> nee!
        self._game_state_play.speed_factor += c.SPEED_INCREMENT
        self._num_speed_increases += 1
        self._GO_FASTER = False


    def _increase_enemies(self):
        """This will increase the total number of enemies on the screen
        by a given amount (default = 1). The Game State Play will produce
        the lacking enemies in its update method. After that, we want to
        slow the game a bit down again."""
        self._game_state_play.num_enemies += c.DEFAULT_ENEMY_INCREMENT
        self._slow_back_down()
        self._MORE_ENEMIES = False

    def _slow_back_down(self):
        """After we increased the number of enemies we want to slow the
        speed back down a bit. When we increase the num enemies, we will have
        increased the speed four times. So we want to slow it back down by
        three times I would say. Thus, SPEED_DECREMENT is set to 3 x SPEED_INCREMENT
         in the constants.py.

         NOTE: We could also derive the amount dynamically somehow from the number
         of times we have increased the speed since the last decrease or so."""
        amount = (self._num_speed_increases * c.SPEED_INCREMENT) * c.SLOW_DOWN_FACTOR
        self._game_state_play.speed_factor -= amount




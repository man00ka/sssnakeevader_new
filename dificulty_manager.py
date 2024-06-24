from pygame.time import Clock
import constants as c


class DifficultyManager:
    # TODO:
    #  - remember old game time
    #  - compare to current time
    #  - update game-time-events
    #  - update game time in game_state_play
    #  before updating difficulty Manager
    def __init__(self, game_state_play):
        self._game_state_play = game_state_play
        self._num_speed_increases = 0
        self._enemy_timer = Clock()
        self._speed_timer = Clock()

        # self._ingame_time_current = game_state_play.ingame_time.get_time()
        # self._ingame_time_previous = self._ingame_time_current

    def update(self):
        """This will check in every frame if enough in-game time has passed
        to trigger different events for increasing difficulty."""
        self._enemy_timer.tick()
        self._speed_timer.tick()
        self._check_for_timed_events()

    def _check_for_timed_events(self):
        """This will check if enough time has passed for any timed event to
        trigger. It will take the appropriate action if so and also reset the
        event timers."""
        MORE_ENEMIES = self._enemy_timer.get_time() // 1000 == c.TIME_UNTIL_MORE_ENEMIES
        GO_FASTER = self._speed_timer.get_time() // 1000 == c.TIME_UNTIL_SPEED_INCREASE

        if MORE_ENEMIES:
            self._increase_enemies()
            print(f"enemy_timer: {self._enemy_timer}")
            self._enemy_timer = Clock()
            print(f"enemy_timer: {self._enemy_timer}")

        if GO_FASTER:
            self._increase_speed()
            print(f"speed_timer: {self._speed_timer}")
            self._speed_timer = Clock()
            print(f"speed_timer: {self._speed_timer}")

    def _increase_speed(self):
        """This will increment the velocity for new enemies (and the background).
        Existing enemies will stay on the same velocity for now."""
        # TODO: Should we also increase the players velocity?
        self._game_state_play.speed_factor += c.SPEED_INCREMENT
        self._num_speed_increases += 1

    def _increase_enemies(self):
        """This will increase the total number of enemies on the screen
        by a given amount (default = 1). The Game State Play will produce
        the lacking enemies in its update method. After that, we want to
        slow the game a bit down again."""
        self._game_state_play.num_enemies += c.DEFAULT_ENEMY_INCREMENT
        self._slow_back_down()

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




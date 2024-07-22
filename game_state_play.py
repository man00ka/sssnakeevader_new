import numpy as np
from itertools import product

import constants as c
from game_state import GameState
from static_entity import StaticEntity, BackgroundTile
from dynamic_entity import DynamicEntity, Player, Enemy
from game_time import GameTime
from dificulty_manager import DifficultyManager
from collision_manager import CollisionManager


# TODO:
#  - Fix game time still counting during PAUSE
#  - Find a way to update back ground tile speed
class GameStatePlay(GameState):
    instance = None

    def __init__(self, *args, **kwargs):
        super(GameStatePlay, self).__init__(*args, **kwargs)
        # The speed factor gets higher by c.SPEED_INCREMENT \
        # when certain events occur (e.g. a certain time has \
        # elapsed).
        self.name = c.STATE_PLAY
        self.speed_factor = c.INITIAL_SPEED_FACTOR
        self.num_enemies = c.INITIAL_NUM_ENEMIES
        self._num_speed_increases = 0
        self.ingame_time = None
        self.difficuelty_manager = DifficultyManager(self)  # Needs the game state to modify the speed_factor
        self.collision_manager = CollisionManager(self)

        self.background = None
        self.player = None
        self.HUD = None

        self._init_background()
        self._init_player()
        self._init_enemies(self.num_enemies)
        self._init_HUD()

    @staticmethod
    def get_instance(*args, **kwargs):
        if not GameStatePlay.instance:
            GameStatePlay.instance = GameStatePlay(*args, **kwargs)
        return GameStatePlay.instance

    def update(self):
        self._check_if_new_enemies_needed()
        self._update_ingame_clock()
        self._update_difficulty_manager()
        self.collision_manager.update()
        super().update()  # This will update the background tiles and enemies

    def _update_player(self):
        pass

    def _update_ingame_clock(self):
        self.ingame_time.update()

    def _update_difficulty_manager(self):
        self.difficuelty_manager.update()

    def _check_if_new_enemies_needed(self):
        # Enemies kill themselves if they go off-screen. However,
        # we need to "refill" the enemies to match `self.num_enemies`
        while len(self.gfx.layers_dict["Enemies"]) < self.num_enemies:
            new_enemy = self._create_enemy()
            self.gfx.add_to_layer("Enemies", new_enemy)

    def _update_HUD(self):
        pass

    def _init_background(self):
        bg_tile_image = self.controller.graphics_manager.grass_tile_image
        num_bg_tiles_x, num_bg_tiles_y = _get_num_bg_tiles(bg_tile_image.get_size())

        # First create the coordinates for the tiles by creating a linear spaced array
        # for the x and y coordinates and then use itertools.product to create
        # a list of tuples with all combinations.
        bg_tiles_coords_x = np.linspace(0, c.DISPLAY_WIDTH, num_bg_tiles_x + 1)
        bg_tiles_coords_y = np.linspace(0, c.DISPLAY_HEIGHT, num_bg_tiles_y + 1)
        bg_tiles_coords = list(product(bg_tiles_coords_x, bg_tiles_coords_y))

        # Then create the tiles and add them to the background layer
        bg_tiles = [
            BackgroundTile(
                image=bg_tile_image,
                pos_x=coords[0],
                pos_y=coords[1])
            for coords in bg_tiles_coords
        ]
        self.gfx.add_to_layer(layer_name="Background", sprites=bg_tiles)

    def _init_player(self):
        player_image = self.controller.graphics_manager.player_image
        self.player = Player(image=player_image, pos_x=0, pos_y=c.DISPLAY_HEIGHT_CENTER)
        self.gfx.add_to_layer(layer_name="Player", sprites=self.player)

    def _create_enemy(self):
        image = self.controller.graphics_manager.enemy_image
        return Enemy(image, self.speed_factor)

    def _init_enemies(self, num_enemies: int):
        enemies = [self._create_enemy() for _ in range(0, num_enemies)]
        self.gfx.add_to_layer("Enemies", enemies)

    def _init_HUD(self):
        # The y offset of the in-game timer sprite is dynamically accounted for
        # by GameTime itself.
        self.ingame_time = GameTime(pos_x=c.DISPLAY_WIDTH_CENTER, pos_y=c.DISPLAY_TOP)

        # Since GameTime inherits from pygame.Sprite and defines a .surf and
        # .rect property, we can just add it to our HUD layer.
        self.gfx.add_to_layer("HUD", self.ingame_time)

        # TODO: Add health bar

    def on_key_press_W(self):
         self.player.go_up()

    def on_key_press_A(self):
        self.player.go_left()

    def on_key_press_S(self):
        self.player.go_down()

    def on_key_press_D(self):
        self.player.go_right()

    def on_key_press_P(self):
        self._switch_to_game_state_pause()

    def on_key_press_ESCAPE(self):
        self._switch_to_game_state_pause()

    def on_key_press_RETURN(self):
        # Nothing
        pass

    def on_key_press_SPACE(self):
        # Player attack
        pass

    def _switch_to_game_state_pause(self):
        self.controller.current_state = (self.controller.game_states[c.STATE_PAUSE]
                                         .get_instance(self.controller))



def _get_num_bg_tiles(tile_size: tuple[int, int]):
    """Returns a tuple of the number of tiles in x and y
    direction. If the tile size does not fit neatly into
    the display size 1 is added to num_x and num_y respectively.

    Args
        tile_size: Tuple[width, height]

    Returns
        Number of tiles: Tuple[num_x, num_y]
    """
    tile_width = tile_size[0]
    tile_height = tile_size[1]

    TILE_FITS_DISPLAY_WIDTH = True \
        if (c.DISPLAY_WIDTH % tile_width) == 0 \
        else False
    TILE_FITS_DISPLAY_HEIGHT = True \
        if (c.DISPLAY_HEIGHT % tile_height) == 0 \
        else False

    num_bg_tiles_x = c.DISPLAY_WIDTH // tile_width \
        if TILE_FITS_DISPLAY_WIDTH \
        else c.DISPLAY_WIDTH // tile_width + 1
    num_bg_tiles_y = c.DISPLAY_HEIGHT // tile_height \
        if TILE_FITS_DISPLAY_HEIGHT \
        else c.DISPLAY_HEIGHT // tile_height + 1

    return num_bg_tiles_x, num_bg_tiles_y

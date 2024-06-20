import numpy as np
import constants as c
from game_state import GameState
from static_entity import StaticEntity, BackgroundTile
from dynamic_entity import DynamicEntity, Player, Enemy
from itertools import product
from random import randint

class GameStatePlay(GameState):
    instance = None

    def __init__(self, *args, **kwargs):
        super(GameStatePlay, self).__init__(*args, **kwargs)
        # The speed factor gets higher by c.SPEED_INCREMENT \
        # when certain events occur (e.g. a certain time has \
        # elapsed).
        self.name = c.STATE_PLAY
        self.speed_factor = c.INITIAL_SPEED_FACTOR
        self.player = None
        self.background = None
        self.enemies = None  # Will be a sprite group
        self.num_enemies = None
        self._init_background()
        self._init_player()
        self._init_enemies()

    def update(self):
        self._update_enemies()
        super().update()

    @staticmethod
    def get_instance(*args, **kwargs):
        if not GameStatePlay.instance:
            GameStatePlay.instance = GameStatePlay(*args, **kwargs)
        return GameStatePlay.instance

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

    def _init_enemies(self):
        enemy_image = self.controller.graphics_manager.enemy_image
        self.num_enemies = 4
        self.enemies = [Enemy(enemy_image,
                              speed_factor=self.speed_factor)
                        for _ in range(0, self.num_enemies)]
        for sprite in self.enemies:
            print(f"pos_x: {sprite.pos_x}")
            print(f"pos_y: {sprite.pos_y}")
            print(f"vel_x: {sprite.vel_x}")
            print(f"vel_y: {sprite.vel_y}")
        self.gfx.add_to_layer("Enemies", self.enemies)

    def _update_enemies(self):
        pass

    def on_key_press_W(self):
         self.player.go_up()

    def on_key_press_A(self):
        self.player.go_left()

    def on_key_press_S(self):
        self.player.go_down()

    def on_key_press_D(self):
        self.player.go_right()

    def on_key_press_P(self):
        self._swith_to_game_state_pause()

    def on_key_press_ESCAPE(self):
        self._swith_to_game_state_pause()

    def on_key_press_RETURN(self):
        # Nothing
        pass

    def on_key_press_SPACE(self):
        # Player attack
        pass

    def _swith_to_game_state_pause(self):
        # TODO: Switch current game state to Pause
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

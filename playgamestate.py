import numpy as np
import constants as c
from game_state import GameState
from static_entity import StaticEntity, BackgroundTile
from dynamic_entity import DynamicEntity, Player
from itertools import product
from typing import TYPE_CHECKING

if True:
    # For static type checking by e.g. mypy.
    from graphicsmanager import GraphicsManager
    from static_entity import StaticEntity
    from dynamic_entity import DynamicEntity

class PlayGameState(GameState):
    # TODO: Maybe rename all GameStates that way and move them \
    #  into game_states.py?
    instance = None

    def __init__(self, *args, **kwargs):
        super(PlayGameState, self).__init__(*args, **kwargs)
        # The speed factor gets higher by c.SPEED_INCREMENT \
        # when certain events occur (e.g. a certain time has \
        # elapsed).
        self.name = c.STATE_PLAY
        self.speed_factor = 1.0
        self._init_background()
        self._init_player()

    @staticmethod
    def get_instance(graphics_manager):
        if not PlayGameState.instance:
            PlayGameState.instance = PlayGameState(graphics_manager)
        return PlayGameState.instance

    def _init_background(self):
        # TODO: Implementieren, dass sprites links vom bild wieder\
        #  rechts eingefügt werden
        bg_tile_image = self.graphics_manager.grass_tile_image
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
        player_image = self.graphics_manager.player_image
        player = Player(image=player_image, pos_x=0, pos_y=c.DISPLAY_HEIGHT_CENTER)
        self.gfx.add_to_layer(layer_name="Player", sprites=player)

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

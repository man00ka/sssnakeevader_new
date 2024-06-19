import pygame
from os.path import join
import constants as c
from pygame.locals import RLEACCEL


class GraphicsManager:
    """The Graphics Manager does tasks like preloading and converting of
    images. It holds the converted images as member variables which can
    be passed to GameObject constructors. It is initialized once and
    passed to the game logic.
    """

    def __init__(self):
        # The load_image function also converts to correct pixel format
        # and sets the color key for the transparent color in the .png
        # file.
        self.player_image = load_image("dog.png", 2)
        self.enemy_image = load_image("snake.png", 1.6)
        self.grass_tile_image = load_image("grass_3_small.png")


def load_image(file_name: str,
               scaling_factor: float = 0.0,
               color_key: tuple[int, int, int] = (0, 0, 0),
               convert: bool = True) -> pygame.Surface:
    """This loads an image file and returns as Surface. It uses the given
    default parameters to convert the Surface to the correct pixel format
    and set black as the transparent color."""
    file_path = join(c.DIR_IMG, file_name)
    image = pygame.image.load(file_path)

    if scaling_factor != 0.0:
        image = pygame.transform.scale_by(image, scaling_factor)

    if color_key:
        image.set_colorkey(color_key, RLEACCEL)

    # This converts to the correct pixel format beforehand, so it doesn't
    # have to be done for every blit which would add up for assets that
    # have to be drawn many times. So this should stay enabled:
    if convert:
        image = image.convert()

    return image

import pygame
from os.path import join
import constants as c


class GraphicsManager:
    """The Graphics Manager does work like preloading and converting of
    images. It holds the converted images as member variables which can
    be passed to GameObject constructors. It is initialized once and
    passed to the game logic.
    """
    def __init__(self):
        self.player_image = load_image("dog.png")
        self.enemy_image = load_image("snake.png")
        self.grass_tile_image = load_image("grass_3_small.png")


def load_image(file_name: str, convert: bool=True):
    file_path = join(c.DIR_IMG, file_name)
    image = pygame.image.load(file_path)

    # This converts to the correct pixel format beforehand, so it doesn't
    # have to be done for every blit which would add up for assets that
    # have to be drawn many times. So this should stay enabled:
    if convert:
        image = image.convert()

    return image

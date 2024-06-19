import pygame
from pygame.sprite import Sprite
import constants as c
from os.path import join


class StaticEntity(Sprite):
    def __init__(self, image=pygame.Surface((32, 32)), pos_x: int = 0, pos_y: int = 0):
        super(StaticEntity, self).__init__()
        self.image = image  # Pixel conversion is done by the GraphicsManager
        self.rect = self.image.get_rect(left=pos_x, top=pos_y)
        self.pos_x = pos_x
        self.pos_y = pos_y
        # for later use with velocity vectors:
        self.vel_x = 0.0
        self.vel_y = 0.0

    def update(self, *args, **kwargs):
        self.update_position()

    def update_position(self):
        self.pos_x += self.vel_x
        self.rect.x = int(self.pos_x)  # Explicitly cast to int to enable pixel perfect movement
        self.pos_y += self.vel_y
        self.rect.y = int(self.pos_y)


class BackgroundTile(StaticEntity):
    def __init__(self, *args, **kwargs):
        super(BackgroundTile, self).__init__(*args, **kwargs)
        self.vel_x = c.SPEED_BACKGROUND

    def update_position(self):
        super().update_position()

        # Check if tile has left the screen and move it if so.
        if self.rect.right < 0:
            self.pos_x = c.DISPLAY_WIDTH

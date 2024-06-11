import pygame
from pygame.sprite import Sprite
import constants as c


class StaticEntity(Sprite):
    def __init__(self, image=pygame.Surface((32, 32))):
        super(StaticEntity, self).__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.pos_x = 0.0
        self.pos_y = 0.0
        # for later use with velocity vectors:
        self.vel_x = 0.0
        self.vel_y = 0.0

    def update(self, *args, **kwargs):
        self.update_position()

    def update_position(self):
        pass
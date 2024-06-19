import pygame
from static_entity import StaticEntity
import ultracolors as colors
import constants as c
# from animation import AnimationGroup
# from entity_state import EntityState()

class DynamicEntity(StaticEntity):
    def __init__(self, *args, **kwargs):
        super(DynamicEntity, self).__init__(*args, **kwargs)
        # self.animation = AnimationGroup()
        # self.state = EntityState()

    def update(self, *args, **kwargs):
        self.update_position()  # inherited
        # self.update_state()
        # self.update_animation()  # not needed yet

    def update_state(self):
        pass

    def update_animation(self):
        pass


class Player(DynamicEntity):
    def __init__(self, *args, **kwargs):
        super(Player, self).__init__(*args, **kwargs)

    def update_position(self):
        super().update_position()

        # Keep player inside display boundaries
        if self.pos_x < 0:
            self.pos_x = 0
            self.rect.x = 0
        if self.pos_y < 0:
            self.pos_y = 0
            self.rect.y = 0
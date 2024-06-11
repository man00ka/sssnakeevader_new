import pygame
from static_entity import StaticEntity
import ultracolors as colors
import constants as c
# from animation import AnimationGroup
# from entity_state import EntityState()

class DynamicEntity(StaticEntity):
    def __init__(self, image=pygame.Surface((32, 32))):
        super(DynamicEntity, self).__init__(image)
        # self.animation = AnimationGroup()
        # self.state = EntityState()

    def update(self, *args, **kwargs):
        self.update_position()  # inherited
        self.update_state()
        self.update_animation()  # not needed yet

    def update_state(self):
        pass

    def update_animation(self):
        pass

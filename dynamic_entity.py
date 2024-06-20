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
        super().update_position()  # Updates movement introduced by velocity vectors
        self._keep_player_on_screen()

    def go_up(self):
        # self.pos_y -= 5
        self.rect.move_ip(0, -5)
        self.pos_y = self.rect.y

    def go_left(self):
        self.pos_x -= 5
        self.rect.x -= 5

    def go_down(self):
        self.pos_y += 5
        self.rect.y += 5

    def go_right(self):
        self.pos_x += 5
        self.rect.x += 5

    def _keep_player_on_screen(self):
        if self.pos_x < 0:
            self.pos_x = 0
            self.rect.x = 0
        if self.pos_y < 0:
            self.pos_y = 0
            self.rect.y = 0

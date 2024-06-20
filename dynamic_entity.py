import pygame
from static_entity import StaticEntity
import ultracolors as colors
import constants as c
from random import randint
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
        self.pos_y -= c.VELOCITY_PLAYER_MOVEMENT
        self.rect.y -= c.VELOCITY_PLAYER_MOVEMENT

    def go_left(self):
        self.pos_x -= c.VELOCITY_PLAYER_MOVEMENT
        self.rect.x -= c.VELOCITY_PLAYER_MOVEMENT

    def go_down(self):
        self.pos_y += c.VELOCITY_PLAYER_MOVEMENT
        self.rect.y += c.VELOCITY_PLAYER_MOVEMENT

    def go_right(self):
        self.pos_x += c.VELOCITY_PLAYER_MOVEMENT
        self.rect.x += c.VELOCITY_PLAYER_MOVEMENT

    def _keep_player_on_screen(self):
        if self.pos_x < 0:
            self.pos_x = 0
            self.rect.x = 0
        if self.pos_y < 0:
            self.pos_y = 0
            self.rect.y = 0


class Enemy(DynamicEntity):
    def __init__(self, *args, speed_factor: float= 1.0, **kwargs):
        super(Enemy, self).__init__(*args, **kwargs)
        self.pos_x, self.pos_y = self._get_random_position()
        self.vel_x = self._get_random_velocity(speed_factor)

    def update_position(self):
        super().update_position()
        self._check_enemy_off_screen()

    def _get_random_position(self):
        pos_x, pos_y = (randint(c.DISPLAY_RIGHT + 20, c.DISPLAY_RIGHT + 100),
                        randint(0, c.DISPLAY_HEIGHT))
        return pos_x, pos_y

    def _get_random_velocity(self, speed_factor):
        return randint(-6, -3) * speed_factor

    def _check_enemy_off_screen(self):
        IS_OFF_SCREEN = self.rect.right < 0
        if IS_OFF_SCREEN:
            self.kill()
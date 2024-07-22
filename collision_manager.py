import pygame
from pygame.sprite import spritecollideany

from pygame.rect import Rect


class CollisionManager:
    def __init__(self, game_state_play):
        self._game_state_play = game_state_play

    def update(self):
        self._detect_collisions()

    def _custom_collided(self, sprite_a, sprite_b):
        sprite_a.rect.colliderect(sprite_b)

    def _detect_collisions(self):
        enemies = self._game_state_play.gfx.get_layer("Enemies")
        player = self._game_state_play.gfx.get_layer("Player").sprites()[0]
        collided_sprite = spritecollideany(player, enemies, collided=self._custom_collided)

        if collided_sprite:
            print("collision")
            pygame.quit()
            # TODO: Transition to game over screen
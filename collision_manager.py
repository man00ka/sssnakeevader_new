import pygame
from pygame import Surface
from pygame.sprite import spritecollideany
from pygame.sprite import Sprite
import constants as c
import ultracolors as uc


class HitBox(Sprite):
    """Takes a (normally scaled down) rect from e.g. enemy or player
    and creates an .image attribute from it. The .rect attribute of
    HitBox itself is then derived via self.image.get_rect()"""

    def __init__(self, rect: pygame.rect.Rect, color: tuple = (0, 0, 0)):
        super(HitBox, self).__init__()
        self.image = Surface(rect.size)
        self.rect = self.image.get_rect()
        self.rect.topleft = rect.topleft  # Das ist wichtig! Wenn wir das nicht machen (die position vom Player-Rect
        # auf das neue HitBox-Rect übertragen), werden alle HitBoxen initial auf
        # 0,0 platziert → es kommt direkt zu einer collision detection → das
        # Spiel wird beendet.
        self.color = color
        self.draw()

    def draw(self):
        self.image.fill(uc.BLACK)
        pygame.draw.rect(surface=self.image,
                         color=self.color,
                         rect=self.image.get_rect(), # Hier brauchen wir unbedingt `image.get_rect()`
                         width=2)
        self.image.set_colorkey(uc.BLACK)


class CollisionManager:
    def __init__(self, game_state_play):
        self._game_state_play = game_state_play

    def update(self):
        self._detect_collisions()
        # ... add more update methods if necessary

    def _custom_collided(self, sprite_a, sprite_b):
        hitbox_a = sprite_a.hitbox.rect  # This is a rect
        hitbox_b = sprite_b.hitbox.rect  # This is a rect
        return hitbox_a.colliderect(hitbox_b)  # Returns True if collided

    def _detect_collisions(self):
        enemies = self._game_state_play.gfx.get_layer("Enemies")
        player = self._game_state_play.gfx.get_layer("Player").sprites()[0]

        # Check for collisions between the enemies srite group
        # and the player sprite with a custom collision function
        # collided_sprite = self._custom_collideany(player, enemies)

        collided_sprite = spritecollideany(player, enemies, collided=self._custom_collided)

        if collided_sprite:
            print("collision")
            pygame.quit()
            quit()
            # TODO: Decrease health instead of quitting
            # TODO: Transition to game over screen if health = 0

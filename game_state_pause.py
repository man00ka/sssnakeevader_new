from game_state import GameState
import pygame
from pygame.sprite import Sprite
import constants as c
import ultracolors as uc
from pygame.locals import SRCALPHA  # Flag to create transparent Surfaces
from pygame.locals import BLEND_RGBA_ADD  # Flag to smoothly blend in the pause screen


class GameStatePause(GameState):
    instance = None
    def __init__(self, *args, **kwargs):
        super(GameStatePause, self).__init__(*args, **kwargs)

        # The Backgroundlayer expects RGB or RGBA tuple.
        # Passing RGBA gives a nice blending and overlay effect.
        # Since ultracolors.py only has RGB tuples we add the
        # A-tuple manually. Values [1-4] work great, default is 2.
        self._add_background_layer(uc.DARK_GREY + (2,))
        self._add_text_layer("PAUSE")
        self.name = c.STATE_SPLASH_SCREEN

    @staticmethod
    def get_instance(*args, **kwargs):
        if not GameStatePause.instance:
            GameStatePause.instance = GameStatePause(*args, **kwargs)
        return GameStatePause.instance

    def _add_background_layer(self, color: tuple[int, int, int] | tuple[int, int, int, int]) -> None:
        background = Sprite()
        # In order for our sprite to work with our layers (sprite groups) it needs
        # to implement an `image` and a `rect` property. So we can call `.draw()`
        # on the sprite group.
        background.image = pygame.Surface(size=c.DISPLAY_SIZE, flags=SRCALPHA)
        background.image.fill(color, special_flags=BLEND_RGBA_ADD)
        background.rect = background.image.get_rect()

        self.gfx.add_to_layer("Background", background)

    def _add_text_layer(self, text):
        text_sprite = Sprite()
        text_surf = self._create_text_surface(text)
        text_sprite.image = text_surf
        text_sprite.rect = text_sprite.image.get_rect(center=c.DISPLAY_CENTER)

        self.gfx.add_to_layer("HUD", text_sprite)

    def _create_text_surface(self, text: str) -> pygame.Surface:
        font = pygame.font.Font("fonts/press-start-2p-font/PressStart2P-vaV7.ttf", 30)
        # font = pygame.font.SysFont("Courier", 30)  # Alternative font
        text_surf = font.render(
            text,
            0,  # no antialiasing for 8-bit
            uc.BLANCHED_ALMOND  # text color
        )
        return text_surf

    def on_key_press_W(self):
        pass

    def on_key_press_A(self):
        pass

    def on_key_press_S(self):
        pass

    def on_key_press_D(self):
        pass

    def on_key_press_P(self):
        self._switch_to_game_state_play()

    def on_key_press_RETURN(self):
        # For selecting menu entries
        pass

    def on_key_press_ESCAPE(self):
        self._switch_to_game_state_play()

    def on_key_press_SPACE(self):
        pass

    def _switch_to_game_state_play(self):
        self.controller.current_state = (self.controller.game_states[c.STATE_PLAY]
                                         .get_instance(self.controller))

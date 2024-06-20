from game_state import GameState
import pygame
from pygame.sprite import Sprite
import constants as c
import ultracolors as uc


class SplashScreen(GameState):
    instance = None
    def __init__(self, *args, **kwargs):
        super(SplashScreen, self).__init__(*args, **kwargs)
        self._add_background_layer(uc.DARK_GREY)
        self._add_text_layer("sssnake evader")
        self.name = c.STATE_SPLASH_SCREEN

    @staticmethod
    def get_instance(*args, **kwargs):
        if not SplashScreen.instance:
            SplashScreen.instance = SplashScreen(*args, **kwargs)
        return SplashScreen.instance

    def _add_background_layer(self, color: tuple[int, int, int]) -> None:
        background = Sprite()
        # Every sprite we add to a sprite group needs to have an `image` and
        # a rect property defined in order to be automatically drawn when
        # calling `.draw()` on the sprite group. Although the image is just
        # a colored Surface in this case:
        background.image = pygame.Surface(size=c.DISPLAY_SIZE)
        background.image.fill(color)
        background.rect = background.image.get_rect()

        self.gfx.add_to_layer("Background", background)

    def _add_text_layer(self, text):
        text_sprite = Sprite()
        text_surf = self._create_text_surface(text)
        text_sprite.image = text_surf
        text_sprite.rect = text_sprite.image.get_rect(center=c.DISPLAY_CENTER)

        self.gfx.add_to_layer("HUD", text_sprite)

    def _create_text_surface(self, text: str) -> pygame.Surface:
        # font = pygame.font.Font("fonts/press-start-2p-font/PressStart2P-vaV7.ttf", 30)
        font = pygame.font.SysFont("Courier", 30)  # Alternative font
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
        pass

    def on_key_press_RETURN(self):
        self._switch_to_game_state_play()

    def on_key_press_ESCAPE(self):
        pygame.quit()
        quit()

    def on_key_press_SPACE(self):
        self._switch_to_game_state_play()

    def _switch_to_game_state_play(self):
        self.controller.current_state = (self.controller.game_states[c.STATE_PLAY]
                                         .get_instance(self.controller))

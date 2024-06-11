from game_state import GameState
import pygame
import constants as c
import ultracolors as uc
class SplashScreen(GameState):
    def __init__(self, display):
        super(SplashScreen, self).__init__()
        self.surf = pygame.Surface(c.DISPLAY_SIZE)
        pygame.draw.rect(self.surf, uc.DARK_GREY, (c.DISPLAY_TOP_LEFT, c.DISPLAY_SIZE))
        self._text = "sssnake evader"
        self.text_surf_size, self.text_surf = self._create_text_surface(self._text)
        self._text_surf_position = (
            c.DISPLAY_CENTER[0] - self.text_surf_size[0]/2,
            c.DISPLAY_CENTER[1] - self.text_surf_size[1]/2
        )
        self.surf.blit(self.text_surf, self._text_surf_position)

    def _create_text_surface(self, text: str) -> tuple[tuple[int, int], pygame.Surface]:
        font = pygame.font.Font("fonts/press-start-2p-font/PressStart2P-vaV7.ttf", 30)
        # font = pygame.font.SysFont("Courier", 30)
        text_surf_size = font.size(self._text)
        text_surf = font.render(
            text,
            0,  # no antialiasing
            uc.BLANCHED_ALMOND  # text color
        )
        return text_surf_size, text_surf

    # We overwrite the GameState class' update and render
    # method because the SplashScreen game state does not have
    # any Sprites, and thus we do not have any gfx layers we need
    # to (or can) update.
    def update(self):
        pass

    def render(self, display):
        display.blit(self.surf, c.DISPLAY_TOP_LEFT)
        pygame.display.flip()  # I don't know why we need to use `pygame.display` here
                               # instead of `display`.
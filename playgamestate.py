from game_state import GameState
from pygame.sprite import Sprite


class Play(GameState):
    def __init__(self, *game_objects: Sprite):
        super(Play, self).__init__()
        self._init_background()


    def _init_background(self):
        # TODO: Num tile sprites ermitteln (von display maßen)
        # TODO: Mehrere Tile-Sprites erstellen mit unterschiedlicher position
        # TODO: Tile sprites zu background layer hinzufügen
        # TODO: Implementieren, dass sprites links vom bild wieder\
        #  rechts eingefügt werden

        tiles = []
        self.gfx.add_to_layer()
        pass

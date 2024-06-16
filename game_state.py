from gfx import GFX
from abc import ABC


class GameState(ABC):
    """This is the Abstract Base Class for any game state.

    Its static `getGameState` method is a blueprint for its
    children to implement. This helps to switch between game
    states because the method will automatically instantiate
    the game state when we switch to this game state for the
    first time but return the already existing instance if we
    have already switched to that particular game state before.
    """
    def __init__(self, graphics_manager):
        self.gfx = GFX()
        self.name = None
        self.graphics_manager = graphics_manager

    def update(self):
        self.gfx.update()

    def render(self, display):
        self.gfx.render(display)
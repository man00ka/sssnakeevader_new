from gfx import GFX

class GameState():
    def __init__(self):
        self.gfx = GFX()

    def update(self):
        self.gfx.update()

    def render(self, display):
        self.gfx.render(display)
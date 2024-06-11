import pygame


class GFX():
    def __init__(self):
        self.layer_0 = pygame.sprite.Group()  # BG Tiles
        self.layer_1 = pygame.sprite.Group()  # Enemies
        self.layer_2 = pygame.sprite.Group()  # Player
        self.layer_3 = pygame.sprite.Group()  # HUD
        self.layers = [
            self.layer_0,
            self.layer_1,
            self.layer_2,
            self.layer_3,
        ]

    def update(self):
        for layer in self.layers:
            layer.update()

    def render(self, display):
        for layer in self. layers:
            layer.draw(display)
        display.flip()
        # TODO: here is still something missing to put everything
        # on the screen.
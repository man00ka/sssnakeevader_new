import pygame


class GFX:
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
        self.layers_dict = {
            "Background": self.layer_0,
            "Enemies": self.layer_1,
            "Player": self.layer_2,
            "HUD": self.layer_3,
        }

    def add_to_layer(self, layer_name: str, sprites: "Sprite or List of Sprites"):
        layer = self.layers_dict[layer_name]
        layer.add(sprites)

    def get_layer(self, name: str):
        return self.layers_dict[name]

    def update(self):
        for layer in self.layers:
            layer.update()

    def render(self, display):
        for layer in self. layers:
            layer.draw(display)
        pygame.display.flip()

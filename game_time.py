import pygame.sprite
from pygame.time import Clock
from pygame.sprite import Sprite
import constants as c


class GameTime(Sprite):
    def __init__(self, image=pygame.Surface((32, 32)),
                 pos_x: int = 0,
                 pos_y: int = 0):
        super(GameTime, self).__init__()
        self.image = image
        self.pos_x = pos_x
        self.pos_y = pos_y
        # self.rect = image.get_rect(center=(pos_x, pos_y))
        self.rect = image.get_rect()
        self.font = c.FONT_COURIER_30
        self.sec = 0
        self.min = 0
        self._text = self._get_time_as_text(self.min, self.sec)
        self._text_size = None
        self.clock = Clock()  # Because Clock is set @final and should not be inherited from
        self.sec_total = None
        self.current_time = 0

    def update(self):
        """`tick` is time in milliseconds of the last game cycle
        and is added incrementally to the current time.
        """
        tick = self.clock.tick()
        self.current_time = self.current_time + tick
        self.sec_total = self.current_time // 1000
        self.min = self.sec_total // 60

        # Correct the seconds by the minutes already counted
        self.sec = self.sec_total - self.min * 60

        self._text = self._get_time_as_text(self.min, self.sec)
        self._text_size = self.font.size(self._text)

        self.image = self.font.render(self._text,
                                      False,  # no antialiasing for 8-bit
                                      (220, 220, 220))  # text color
        self.rect = self.image.get_rect(centerx=self.pos_x)

    def _get_time_as_text(self, min: int, sec: int):
        return f"{self.min:02}:{self.sec:02}"

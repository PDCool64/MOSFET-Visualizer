import pygame as pg
from mosfet import MOSFET, font


class P_MOSFET(MOSFET):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.color = (100, 100, 255)
        self.text = font.render("P MOSFET", True, (0, 0, 0))

    def _draw(self, screen: pg.Surface):
        pass

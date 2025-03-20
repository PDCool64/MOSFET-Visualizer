import pygame as pg
from mosfet import MOSFET, font


class N_MOSFET(MOSFET):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.color = (255, 100, 100)
        self.text = font.render("N MOSFET", True, (0, 0, 0))

    def _draw(self, screen: pg.Surface):
        pass

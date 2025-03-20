import pygame as pg

pg.font.init()
font = pg.font.Font(None, 20)

SOURCE_COLOR = (255, 255, 0)
GATE_COLOR = (0, 255, 0)
DRAIN_COLOR = (0, 0, 255)


class MOSFET:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = 50
        self.color = (255, 255, 255)
        self.text = font.render("MOSFET", True, (0, 0, 0))

        self.source = pg.Rect(
            self.x + self.radius * 0.8,
            self.y - self.radius / 4,
            self.radius / 2,
            self.radius / 2,
        )
        self.gate = pg.Rect(
            self.x - self.radius * 1.3,
            self.y - self.radius / 4,
            self.radius / 2,
            self.radius / 2,
        )
        self.drain = pg.Rect(
            self.x - self.radius / 4,
            self.y + self.radius * 0.8,
            self.radius / 2,
            self.radius / 2,
        )

    def draw(self, screen: pg.Surface):
        pg.draw.circle(screen, self.color, (self.x, self.y), self.radius)
        rect = self.text.get_rect(center=(self.x, self.y))
        screen.blit(self.text, rect)
        self._draw_source(screen)
        self._draw_gate(screen)
        self._draw_drain(screen)

        self._draw(screen)

    def _draw_source(self, screen: pg.Surface):
        pg.draw.rect(
            screen,
            SOURCE_COLOR,
            self.source,
            self.radius // 2,
        )

    def _draw_gate(self, screen: pg.Surface):
        pg.draw.rect(
            screen,
            GATE_COLOR,
            self.gate,
            self.radius // 2,
        )

    def _draw_drain(self, screen: pg.Surface):
        pg.draw.rect(
            screen,
            DRAIN_COLOR,
            self.drain,
            self.radius // 2,
        )

    def _draw(self, screen):
        pass

    def update(self):
        self.source = pg.Rect(
            self.x + self.radius * 0.8,
            self.y - self.radius / 4,
            self.radius / 2,
            self.radius / 2,
        )
        self.gate = pg.Rect(
            self.x - self.radius * 1.3,
            self.y - self.radius / 4,
            self.radius / 2,
            self.radius / 2,
        )
        self.drain = pg.Rect(
            self.x - self.radius / 4,
            self.y + self.radius * 0.8,
            self.radius / 2,
            self.radius / 2,
        )

    def is_clicked(self, pos) -> bool:
        mouse_x, mouse_y = pos
        # Cirlce
        distance_from_middle_point = (
            (mouse_x - self.x) ** 2 + (mouse_y - self.y) ** 2
        ) ** 0.5
        circle_hit = distance_from_middle_point <= self.radius

        # Rectangles
        source_hit = self.source.collidepoint(pos)
        gate_hit = self.gate.collidepoint(pos)
        drain_hit = self.drain.collidepoint(pos)

        return circle_hit or source_hit or gate_hit or drain_hit

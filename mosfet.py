import pygame as pg

from terminal import Terminal, Source, Gate, Drain, font

pg.font.init()

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

        self.source = Source(
            self.x - self.radius * 1.3,
            self.y - self.radius / 4,
            self.radius / 2,
            self.radius / 2,
            SOURCE_COLOR,
            "",
        )
        self.gate = Gate(
            self.x - self.radius / 4,
            self.y + self.radius * 0.8,
            self.radius / 2,
            self.radius / 2,
            GATE_COLOR,
            "",
        )
        self.drain = Drain(
            self.x + self.radius * 0.8,
            self.y - self.radius / 4,
            self.radius / 2,
            self.radius / 2,
            DRAIN_COLOR,
            "",
        )

    def draw(self, screen: pg.Surface):
        pg.draw.circle(screen, self.color, (self.x, self.y), self.radius)
        rect = self.text.get_rect(center=(self.x, self.y))
        screen.blit(self.text, rect)
        self.source.draw(screen, 10)
        self.gate.draw(screen, 10)
        self.drain.draw(screen, 10)

        self._draw(screen)

    def _draw(self, screen):
        pass

    def update(self):
        # Source on the right
        self.source.update_position(
            self.x - self.radius * 1.3, self.y - self.radius / 4
        )
        # Gate on the left
        self.gate.update_position(self.x - self.radius / 4, self.y + self.radius * 0.8)
        # Drain at the bottom
        self.drain.update_position(self.x + self.radius * 0.8, self.y - self.radius / 4)

    def is_clicked(self, pos) -> bool:
        mouse_x, mouse_y = pos
        distance_from_middle_point = (
            (mouse_x - self.x) ** 2 + (mouse_y - self.y) ** 2
        ) ** 0.5
        circle_hit = distance_from_middle_point <= self.radius
        return circle_hit

    def get_clicked(self, pos):
        if self.source.is_clicked(pos):
            return self.source
        if self.gate.is_clicked(pos):
            return self.gate
        if self.drain.is_clicked(pos):
            return self.drain
        if self.is_clicked(pos):
            return self

    def handle_click(self, pos):
        self.mouse_diff = (
            pos[0] - self.x,
            pos[1] - self.y,
        )

    def handle_drag(self, pos):
        self.x, self.y = pos
        self.x -= self.mouse_diff[0]
        self.y -= self.mouse_diff[1]

    def handle_drop(self, pos, terminal):
        self.x, self.y = pos
        self.x -= self.mouse_diff[0]
        self.y -= self.mouse_diff[1]

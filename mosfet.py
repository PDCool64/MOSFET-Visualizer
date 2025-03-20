import pygame as pg

pg.font.init()
font = pg.font.Font(None, 20)

SOURCE_COLOR = (255, 255, 0)
GATE_COLOR = (0, 255, 0)
DRAIN_COLOR = (0, 0, 255)


class Terminal:
    """Represents a connection point on the MOSFET (Source, Gate, or Drain)"""

    def __init__(
        self,
        x: float,
        y: float,
        width: float,
        height: float,
        color: tuple[int, int, int],
        name: str,
    ):
        self.rect = pg.Rect(x, y, width, height)
        self.color = color
        self.name = name
        self.text = font.render(name, True, (0, 0, 0))

        self.line_end = None

    def draw(self, screen: pg.Surface, border_radius: int):
        """Draw the terminal with its label"""
        pg.draw.rect(screen, self.color, self.rect)
        # Text
        # text_rect = self.text.get_rect(center=self.rect.center)
        # screen.blit(self.text, text_rect)

        if self.line_end:
            pg.draw.line(screen, self.color, self.rect.center, self.line_end, 5)

    def update_position(self, x: float, y: float):
        """Update the terminal's position"""
        self.rect.x = x
        self.rect.y = y

    def is_clicked(self, pos: tuple[int, int]) -> bool:
        """Check if this terminal was clicked"""
        return self.rect.collidepoint(pos)

    def handle_click(self, pos: tuple[int, int]):
        self.mouse_diff = (pos[0] - self.rect.center[0], pos[1] - self.rect.center[1])

    def handle_drag(self, pos: tuple[int, int]):
        self.line_end = (pos[0] - self.mouse_diff[0], pos[1] - self.mouse_diff[1])

    def handle_drop(self, pos: tuple[int, int], terminal):
        self.line_end = None
        print(terminal)

    def __repr__(self):
        return f"""Terminal: {self.name} 
    pos: {self.rect.topleft}
    line_end: {self.line_end}
        """


class MOSFET:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = 50
        self.color = (255, 255, 255)
        self.text = font.render("MOSFET", True, (0, 0, 0))

        self.source = Terminal(
            self.x + self.radius * 0.8,
            self.y - self.radius / 4,
            self.radius / 2,
            self.radius / 2,
            SOURCE_COLOR,
            "",
        )
        self.gate = Terminal(
            self.x - self.radius * 1.3,
            self.y - self.radius / 4,
            self.radius / 2,
            self.radius / 2,
            GATE_COLOR,
            "",
        )
        self.drain = Terminal(
            self.x - self.radius / 4,
            self.y + self.radius * 0.8,
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
            self.x + self.radius * 0.8, self.y - self.radius / 4
        )
        # Gate on the left
        self.gate.update_position(self.x - self.radius * 1.3, self.y - self.radius / 4)
        # Drain at the bottom
        self.drain.update_position(self.x - self.radius / 4, self.y + self.radius * 0.8)

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

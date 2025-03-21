import pygame as pg


font = pg.font.Font(None, 20)


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
        self.connection = None

    def draw(self, screen: pg.Surface, border_radius: int):
        """Draw the terminal with its label"""
        pg.draw.rect(screen, self.color, self.rect)
        # Text
        # text_rect = self.text.get_rect(center=self.rect.center)
        # screen.blit(self.text, text_rect)

        if self.line_end:
            pg.draw.line(screen, self.color, self.rect.center, self.line_end, 5)
        if self.connection:
            pg.draw.line(
                screen, self.color, self.rect.center, self.connection.rect.center, 5
            )

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
        if isinstance(terminal):
            self.connection = terminal
        print(terminal)

    def __repr__(self):
        return f"""Terminal: {self.name} 
    pos: {self.rect.topleft}
    line_end: {self.line_end}
        """


class Source(Terminal):
    def __repr__(self):
        return f"""Source: {self.name}
    pos: {self.rect.topleft}
    line_end: {self.line_end}
        """

    def handle_drop(self, pos, terminal):
        self.line_end = None
        if not isinstance(terminal, Terminal):
            return
        if isinstance(terminal, Source):
            return
        if isinstance(terminal, Gate):
            return

        # connection is a drain
        self.connection = terminal


class Gate(Terminal):
    def __repr__(self):
        return f"""Gate: {self.name}
    pos: {self.rect.topleft}
    line_end: {self.line_end}
        """

    def handle_drop(self, pos, terminal):
        self.line_end = None
        if not isinstance(terminal, Terminal):
            return
        if isinstance(terminal, Source):
            return
        if isinstance(terminal, Gate):
            return

        # connection is a drain
        self.connection = terminal


class Drain(Terminal):
    def __repr__(self):
        return f"""Drain: {self.name}
    pos: {self.rect.topleft}
    line_end: {self.line_end}
        """

    def handle_drop(self, pos, terminal):
        self.line_end = None
        if not isinstance(terminal, Terminal):
            return
        if isinstance(terminal, Drain):
            return
        terminal.connection = self

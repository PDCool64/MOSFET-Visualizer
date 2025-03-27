import pygame as pg


class Pole:
    def update(self):
        pass

    def handle_click(self, pos):
        pass

    def handle_drag(self, pos):
        return

    def handle_drop(self, pos, terminal):
        return


class PoleConnector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = 0
        self.rect = pg.Rect(x, y, self.radius, self.radius)
        self.color = (155, 155, 155)


class MinusPole(Pole):
    border: int
    """
    The x border of the pole
    """

    def __init__(self):
        self.border = 50

    def draw(self, screen):
        center = pg.draw.rect(screen, (255, 255, 255), (0, 0, 50, screen.get_height()))
        # minus
        pg.draw.line(
            screen,
            (0, 0, 0),
            (center.centerx - 10, center.centery),
            (center.centerx + 10, center.centery),
            5,
        )

    def is_clicked(self, pos):
        clicked = pos[0] < self.border

        return clicked

    def get_clicked(self, pos):
        if self.is_clicked(pos):
            return MinusPoleConnector(pos[1])


class MinusPoleConnector(PoleConnector):
    def __init__(self, y):
        super().__init__(50, y)
        print(self.x, self.y)

    def draw(self, screen):
        pg.draw.circle(screen, self.color, (self.x, self.y), self.radius)


class PlusPole(Pole):

    border: int
    """
    The x border of the pole
    """

    def __init__(self):
        self.border = 0

    def draw(self, screen: pg.Surface):
        center = pg.draw.rect(
            screen,
            (255, 255, 255),
            (screen.get_width() - 50, 0, 50, screen.get_height()),
        )

        self.border = screen.get_width() - 50
        """
            Some text
        """

        # plus
        pg.draw.line(
            screen,
            (0, 0, 0),
            (center.centerx - 10, center.centery),
            (center.centerx + 10, center.centery),
            5,
        )

        pg.draw.line(
            screen,
            (0, 0, 0),
            (center.centerx, center.centery - 10),
            (center.centerx, center.centery + 10),
            5,
        )

    def __repr__(self):
        return f"Pole: {self.charge}"

    def is_clicked(self, pos):
        return pos[0] > self.border

    def get_clicked(self, pos):
        if self.is_clicked(pos):
            return PlusPoleConnector(pos[1])


class PlusPoleConnector(PoleConnector):
    def __init__(self, y):
        super().__init__(50, y)

    def draw(self, screen: pg.Surface):
        pg.draw.circle(screen, self.color, (self.x, self.y), self.radius)
        self.x = screen.get_width() - 50

    def update(self):
        self.rect = pg.Rect(self.x, self.y, self.radius, self.radius)

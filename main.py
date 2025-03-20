import pygame as pg

pg.init()

from mosfet import MOSFET
from nmosfet import N_MOSFET
from pmosfet import P_MOSFET

SCREEN_WIDTH, SCREEN_HEIGHT = 1920, 1080
BACKGROUND_COLOR = (210, 210, 235)


font = pg.font.Font(None, 20)
"""
    default font
"""


# Set up the drawing window
screen: pg.Surface = pg.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
"""
    The main screen that will be displayed
"""

entities: list[MOSFET] = []
"""
    List of entities that will be drawn on the screen
"""
entities.append(P_MOSFET(100, 100))
entities.append(N_MOSFET(400, 100))
entities.append(P_MOSFET(700, 100))
run: bool = True
"""
    The main loop that will run the program
"""

active_element = None
active_element_diff = None

clock = pg.time.Clock()

while run:
    ev = pg.event.get()
    for event in ev:
        if event.type == pg.QUIT:
            run = False
        if event.type == pg.KEYDOWN:
            pass
        if event.type == pg.MOUSEBUTTONUP:
            active_element = None

        if event.type == pg.MOUSEBUTTONDOWN:
            mouse_pos = pg.mouse.get_pos()
            for entity in entities:
                if entity.is_clicked(mouse_pos):
                    # active_element = entity.get_clicked(mouse_pos)
                    active_element = entity
                    active_element_diff = (
                        mouse_pos[0] - entity.x,
                        mouse_pos[1] - entity.y,
                    )
                    break
        if event.type == pg.MOUSEMOTION:
            if active_element:
                active_element.x, active_element.y = pg.mouse.get_pos()
                active_element.x -= active_element_diff[0]
                active_element.y -= active_element_diff[1]

    screen.fill(BACKGROUND_COLOR)
    clock.tick(165)
    if pg.event.get(pg.QUIT):
        run = False
    for entity in entities:
        entity.draw(screen)
        entity.update()
    if pg.key.get_pressed()[pg.K_LEFT]:
        entities[0].x -= 1
    if pg.mouse.get_pressed()[0]:
        # print("Mouse pressed")
        # print(pg.mouse.get_pressed())
        pass
    pg.display.flip()

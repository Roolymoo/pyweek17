##############################################################################
# Copyright (C) 2013  Dickson Wong, Lucas Ashbury-Bridgwood
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
##############################################################################

import pygame
from time import perf_counter


class Button:
    def __init__(self, COORD, WIDTH, HEIGHT, TEXT, FONT_FAMILY=None,
            FONT_SIZE=12, LINE_WIDTH=1, COLOUR=(0, 0, 0), FOO=None):
        '''(Button, tuple, int, int, str, str, int, int, tuple, function) -> NoneType

        rect - border of text
        line_width - width of border lines
        colour - colour of border and text
        text - 
        foo - function to execute on activation'''
        X, Y = COORD

        ANTIALIAS = True
        BACKGROUND = None

        self.rect = pygame.Rect(X, Y, WIDTH, HEIGHT)
        self.line_width = LINE_WIDTH
        self.colour = COLOUR
        self.text = pygame.font.Font(FONT_FAMILY, FONT_SIZE).render(
                TEXT, ANTIALIAS, COLOUR, BACKGROUND)
        self.foo = FOO

    def unrender(self, app):
        '''(Button, App) -> NoneType
        Blits over self.rect with app.background on app.window.'''
        if type(app.background) == tuple:
            app.window.fill(app.background, self.rect)

    def is_clicked(self, MOUSE_POS):
        '''(Button, tuple) -> bool'''
        return self.rect.collidepoint(MOUSE_POS)

    def render(self, surface):
        '''(Button, pygame.Surface) -> NoneType'''
        pygame.draw.rect(surface, self.colour, self.rect, self.line_width)

        TEXT_XPADDING = 10
        TEXT_YPADDING = 5
        X, Y = self.rect.x + TEXT_XPADDING, self.rect.y + TEXT_YPADDING
        surface.blit(self.text, (X, Y))

    def execute(self, app, MOUSE_POS):
        '''(Button, App, tuple) -> NoneType'''
        if not self.foo == None:
            self.foo(app, MOUSE_POS)


def exit_app(app, MOUSE_POS=None):
    '''(App, tuple) -> NoneType'''
    app.running = False

def play(app, MOUSE_POS=None):
    '''(App, tuple) -> NoneType'''
    app.play = True

def reset(app, MOUSE_POS=None):
    '''(App, tuple) -> NoneType'''
    app.play = False
    app.reset = True
    app.selected_moon = None
    app.asteroids_ingame = app.asteroids.copy()

    # unrender everything first
    for moon in app.moons:
        app.to_update.append(moon.unrender(app))
        old_time = perf_counter()
        app.to_update.append(moon.update_parameter(
                app.window, perf_counter() - old_time))

    for asteroid in app.asteroids_ingame:
        app.to_update.append(asteroid.unrender(app))
        asteroid.parameter = perf_counter() - old_time

    # start rendering now
    for moon in app.moons:
        old_time = perf_counter()
        app.to_update.append(moon.update_parameter(
                app.window, perf_counter() - old_time))

    for orbit in app.orbits:
        app.to_update.append(pygame.draw.circle(*orbit))

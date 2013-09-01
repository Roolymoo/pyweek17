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
from os.path import join
from button import Button, exit_app


def render_level_screen(app, MOUSE_POS):
    '''(App, tuple) -> NoneType'''
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)

    FONT_FAMILY = join("data", "font", "Alien-Encounters-Regular.ttf")
    FONT_SIZE = 30
    FONT_COLOUR = WHITE

    app.window.fill(BLACK)

    # title screen button
    COORD = (100, 100)
    WIDTH = 300
    HEIGHT = 40
    TEXT = "title screen"
    FOO = None
    title_screen_button = Button(COORD, WIDTH, HEIGHT, TEXT, FONT_FAMILY,
            FONT_SIZE, COLOUR=FONT_COLOUR, FOO=FOO)
    app.ui_elements.append(title_screen_button)
    title_screen_button.render(app.window)

    pygame.display.update()

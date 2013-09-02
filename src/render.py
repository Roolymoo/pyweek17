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

def render_title_menu_screen(app, MOUSE_POS=None):
    '''(App) -> NoneType'''
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)

    app.ui_elements = [] # remove old ui elements in old screen, if any

    FONT_FAMILY = join("data", "font", "Alien-Encounters-Regular.ttf")
    FONT_SIZE = 30
    FONT_COLOUR = WHITE

    app.window.fill(BLACK)

    # title
    TEXT = "title"
    ANTIALIAS = True
    BACKGROUND = None
    TITLE = pygame.font.Font(FONT_FAMILY, FONT_SIZE).render(
                TEXT, ANTIALIAS, FONT_COLOUR, BACKGROUND)
    COORD = (100, 100)
    app.window.blit(TITLE, COORD)

    # levels button
    COORD = (100, 200)
    WIDTH = 600
    HEIGHT = 40
    TEXT = "levels"
    FOO = render_level_menu_screen
    exit_button = Button(COORD, WIDTH, HEIGHT, TEXT, FONT_FAMILY, FONT_SIZE,
            COLOUR=FONT_COLOUR, FOO=FOO)
    app.ui_elements.append(exit_button)
    exit_button.render(app.window)

    # exit button
    COORD = (100, 300)
    WIDTH = 600
    HEIGHT = 40
    TEXT = "exit"
    FOO = exit_app
    exit_button = Button(COORD, WIDTH, HEIGHT, TEXT, FONT_FAMILY, FONT_SIZE,
            COLOUR=FONT_COLOUR, FOO=FOO)
    app.ui_elements.append(exit_button)
    exit_button.render(app.window)

    pygame.display.update()

def render_level_menu_screen(app, MOUSE_POS=None):
    '''(App, tuple) -> NoneType'''
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)

    app.ui_elements = [] # remove old ui elements in old screen, if any

    FONT_FAMILY = join("data", "font", "Alien-Encounters-Regular.ttf")
    FONT_SIZE = 30
    FONT_COLOUR = WHITE

    app.window.fill(BLACK)

    # title screen button
    COORD = (100, 50)
    WIDTH = 600
    HEIGHT = 40
    TEXT = "title screen"
    FOO = render_title_menu_screen
    title_screen_button = Button(COORD, WIDTH, HEIGHT, TEXT, FONT_FAMILY,
            FONT_SIZE, COLOUR=FONT_COLOUR, FOO=FOO)
    app.ui_elements.append(title_screen_button)
    title_screen_button.render(app.window)

    # level 1 button
    COORD = (100, 150)
    WIDTH = 600
    HEIGHT = 40
    TEXT = "level 1"
    FOO = None # TODO ########################################################
    level1_button = Button(COORD, WIDTH, HEIGHT, TEXT, FONT_FAMILY,
            FONT_SIZE, COLOUR=FONT_COLOUR, FOO=FOO)
    app.ui_elements.append(level1_button)
    level1_button.render(app.window)

    # level 2 button
    COORD = (100, 200)
    WIDTH = 600
    HEIGHT = 40
    TEXT = "level 2"
    FOO = None # TODO ########################################################
    level2_button = Button(COORD, WIDTH, HEIGHT, TEXT, FONT_FAMILY,
            FONT_SIZE, COLOUR=FONT_COLOUR, FOO=FOO)
    app.ui_elements.append(level2_button)
    level2_button.render(app.window)

    pygame.display.update()

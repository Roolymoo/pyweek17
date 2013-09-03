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
from label import Label

def render_title_menu_screen(app, MOUSE_POS=None):
    '''(App, tuple) -> NoneType'''
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)

    app.ui_elements.clear() # remove old ui elements in old screen, if any

    FONT_FAMILY = join("data", "font", "Alien-Encounters-Regular.ttf")
    FONT_SIZE = 30
    FONT_COLOUR = WHITE

    app.background = BLACK
    app.window.fill(BLACK)

    # title
    TEXT = "title"
    COORD = (100, 100)
    title_label = Label(TEXT, COORD, FONT_FAMILY, FONT_SIZE, FONT_COLOUR)
    app.ui_elements.append(title_label)
    title_label.render(app.window)

    # levels button
    COORD = (100, 200)
    WIDTH = 800
    HEIGHT = 40
    TEXT = "levels"
    FOO = render_level_menu_screen
    levels_button = Button(COORD, WIDTH, HEIGHT, TEXT, FONT_FAMILY, FONT_SIZE,
            COLOUR=FONT_COLOUR, FOO=FOO)
    app.ui_elements.append(levels_button)
    levels_button.render(app.window)

    # exit button
    COORD = (100, 300)
    WIDTH = 800
    HEIGHT = 40
    TEXT = "exit"
    FOO = exit_app
    exit_button = Button(COORD, WIDTH, HEIGHT, TEXT, FONT_FAMILY, FONT_SIZE,
            COLOUR=FONT_COLOUR, FOO=FOO)
    app.ui_elements.append(exit_button)
    exit_button.render(app.window)

    app.to_update.append(None) # update whole software display

    app.status = 0

def render_level_menu_screen(app, MOUSE_POS=None):
    '''(App, tuple) -> NoneType'''
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)

    app.ui_elements.clear() # remove old ui elements in old screen, if any

    FONT_FAMILY = join("data", "font", "Alien-Encounters-Regular.ttf")
    FONT_SIZE = 30
    FONT_COLOUR = WHITE

    app.background = BLACK
    app.window.fill(BLACK)

    # title screen button
    COORD = (100, 50)
    WIDTH = 800
    HEIGHT = 40
    TEXT = "title screen"
    FOO = render_title_menu_screen
    title_screen_button = Button(COORD, WIDTH, HEIGHT, TEXT, FONT_FAMILY,
            FONT_SIZE, COLOUR=FONT_COLOUR, FOO=FOO)
    app.ui_elements.append(title_screen_button)
    title_screen_button.render(app.window)

    # level 1 button
    COORD = (100, 200)
    WIDTH = 800
    HEIGHT = 40
    TEXT = "level 1"
    FOO = render_level_screen # DEBUG ########################################
    level1_button = Button(COORD, WIDTH, HEIGHT, TEXT, FONT_FAMILY,
            FONT_SIZE, COLOUR=FONT_COLOUR, FOO=FOO)
    app.ui_elements.append(level1_button)
    level1_button.render(app.window)

    # level 2 button
    COORD = (100, 250)
    WIDTH = 800
    HEIGHT = 40
    TEXT = "level 2"
    FOO = render_level_screen # DEBUG ########################################
    level2_button = Button(COORD, WIDTH, HEIGHT, TEXT, FONT_FAMILY,
            FONT_SIZE, COLOUR=FONT_COLOUR, FOO=FOO)
    app.ui_elements.append(level2_button)
    level2_button.render(app.window)

    app.to_update.append(None) # update whole software display

    app.status = 1

def render_level_screen(app, MOUSE_POS=None):
    '''(App, tuple) -> NoneType'''
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)

    app.ui_elements.clear() # remove old ui elements in old screen, if any

    FONT_FAMILY = join("data", "font", "Alien-Encounters-Regular.ttf")
    FONT_SIZE = 30
    FONT_COLOUR = WHITE

    BUTTON_PADDING = app.width - 200 + 25
    BUTTON_WIDTH = 150
    BUTTON_HEIGHT = 40

    app.background = BLACK
    app.window.fill(BLACK)

    # line separator between planet and game interface
    START_POS = (app.width - 200, 0)
    END_POS = (app.width - 200, app.height)
    pygame.draw.line(app.window, WHITE, START_POS, END_POS)

    # play button
    COORD = (BUTTON_PADDING, 100 - BUTTON_HEIGHT)
    TEXT = "play"
    FOO = None # TODO ########################################################
    play_button = Button(COORD, BUTTON_WIDTH, BUTTON_HEIGHT, TEXT,
            FONT_FAMILY, FONT_SIZE, COLOUR=FONT_COLOUR, FOO=FOO)
    app.ui_elements.append(play_button)
    play_button.render(app.window)

    # reset button
    COORD = (BUTTON_PADDING, 200 - BUTTON_HEIGHT)
    TEXT = "reset"
    FOO = None # TODO ########################################################
    reset_button = Button(COORD, BUTTON_WIDTH, BUTTON_HEIGHT, TEXT,
            FONT_FAMILY, FONT_SIZE, COLOUR=FONT_COLOUR, FOO=FOO)
    app.ui_elements.append(reset_button)
    reset_button.render(app.window)

    # levels button
    COORD = (BUTTON_PADDING, app.height - 200)
    TEXT = "levels"
    FOO = render_level_menu_screen
    levels_button = Button(COORD, BUTTON_WIDTH, BUTTON_HEIGHT, TEXT,
            FONT_FAMILY, FONT_SIZE, COLOUR=FONT_COLOUR, FOO=FOO)
    app.ui_elements.append(levels_button)
    levels_button.render(app.window)

    # exit button
    COORD = (BUTTON_PADDING, app.height - 100)
    TEXT = "exit"
    FOO = exit_app
    exit_button = Button(COORD, BUTTON_WIDTH, BUTTON_HEIGHT, TEXT,
            FONT_FAMILY, FONT_SIZE, COLOUR=FONT_COLOUR, FOO=FOO)
    app.ui_elements.append(exit_button)
    exit_button.render(app.window)

    app.to_update.append(None) # update whole software display

    app.status = 2

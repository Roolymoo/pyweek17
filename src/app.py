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
from pygame.locals import QUIT, MOUSEBUTTONUP
from init import get_init_data
from render import render_title_menu_screen


class App:
    def __init__(self):
        '''(App) -> NoneType

        width       - window width
        height      - window height
        fps         - software display FPS
        fps_clock   - controls software display FPS
        running     - running status of game
        ui_elements - currently used UI elements
        window      - the software display
        title       - game name
        background  - current background. Either a colour (tuple) ...
        status      - what kind of screen is being rendered currently.
                        - -1 no kind
                        - 0 title menu screen
                        - 1 level menu screen
                        - 2 game screen
        to_update   - pygame.Rect's of window that need updating, or None to
                      indicate that the whole display must be updated'''
        self.width = None
        self.height = None
        self.fps = None
        self.fps_clock = None
        self.running = None
        self.ui_elements = None
        self.window = None
        self.title = None
        self.background = None
        self.status = None
        self.to_update = None

    def __del__(self):
        '''(App) -> NoneType
        Exit Pygame.'''
        pygame.quit()

    def init(self):
        '''(App) -> int
        Initializes Pygame and loads initization data for pygame. If the data
        fails to load, returns -1. Otherwise returns 0.'''
        pygame.init()

        DATA = get_init_data()

        #get_init_data failed to get anything meaningful
        if DATA == {}:
            return -1

        #Sets up the window
        self.width = int(*DATA["width"])
        self.height = int(*DATA["height"])
        self.fps = int(*DATA["fps"])
        self.fps_clock = pygame.time.Clock()
        self.running = True
        self.ui_elements = []
        self.window = pygame.display.set_mode((self.width, self.height))
        self.title = "title"
        self.status = -1 # no kind, game is loading
        self.to_update = []

        pygame.display.set_caption(self.title)

        render_title_menu_screen(self)

        return 0

    def exit(self):
        '''(App) -> NoneType'''
        self.running = False

    def main(self):
        '''(App) -> int
        Main routine of the game. Returns the return of self.init() if it does
        not return 0, otherwise returns 0.'''
        #Starts the game window
        init_status = self.init()
        #Failed to initialize properly
        if init_status != 0:
            return init_status

        while self.running:

            #Checks for events
            for event in pygame.event.get():

                #Exit event
                if event.type == QUIT:
                    self.exit()

                #Mouse click event
                elif event.type == MOUSEBUTTONUP:

                    #Elements for ui include button
                    for ui_elem in self.ui_elements:
                        mouse_pos = pygame.mouse.get_pos()
                        if ui_elem.is_clicked(mouse_pos):
                            ui_elem.execute(self, mouse_pos)

            for rect in self.to_update:
                if rect == None:
                    pygame.display.update()
                    break
                pygame.display.update(rect)
            self.to_update.clear()

            self.fps_clock.tick(self.fps)

        return 0

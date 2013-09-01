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
from pygame.locals import QUIT
from init import get_init_data, render_title_screen


class App:
    def __init__(self):
        '''(App) -> NoneType'''
        self.width = None
        self.height = None
        self.running = None
        self.fps = None
        self.fps_clock = None
        self.window = None

    def __del__(self):
        '''(App) -> NoneType'''
        pygame.quit()

    def init(self):
        '''(App) -> int
        Loads initization data for pygame. If the data fails to load, returns
        -1. Otherwise returns 0.'''
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
        self.window = pygame.display.set_mode((self.width, self.height))

        return 0

    def exit(self):
        '''(App) -> NoneType'''
        self.running = False

    def main(self):
        '''(App) -> int
        ...'''
        #Starts the game window
        init_status = self.init()
        #Failed to initialize properly
        if init_status != 0:
            return init_status

        while self.running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.exit()

            self.fps_clock.tick(self.fps)

        return 0
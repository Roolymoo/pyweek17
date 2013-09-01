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


class App:
    def __init__(self):
        '''(App) -> NoneType'''
        self.width = None
        self.height = None
        self.running = None
        self.window = None

    def init(self):
        '''(App) -> int'''
        self.width = 600 # TODO change from hardcode #########################
        self.height = 600 # TODO change from hardcode ########################
        self.running = True
        self.window = pygame.display.set_mode((self.width, self.height))

        # pygame.display.update()

        return 0

    def exit(self):
        '''(App) -> NoneType'''
        self.running = False

    def main(self):
        '''(App) -> int'''
        init_status = self.init()
        if init_status != 0:
            return init_status

        while self.running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.exit()

        return 0

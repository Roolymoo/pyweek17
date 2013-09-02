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


class Label:
    def __init__(self, TEXT, COORD, FONT_FAMILY=None, FONT_SIZE=12,
            FONT_COLOUR=(0, 0, 0)):
        '''(Label, str, tuple, str, int, tuple) -> NoneType

        label - pygame.Surface of rendered text
        coord - location to render
        rect - pygame.Rect of text'''
        ANTIALIAS = True
        BACKGROUND = None
        font = pygame.font.Font(FONT_FAMILY, FONT_SIZE)

        self.label = font.render(TEXT, ANTIALIAS, FONT_COLOUR, BACKGROUND)
        self.coord = COORD
        self.rect = pygame.Rect(COORD, font.size(TEXT))

    def is_clicked(self, MOUSE_POS):
        '''(App, tuple) -> bool'''
        return False # not used by Label

    def render(self, surface):
        '''(Button, pygame.Surface) -> NoneType'''
        surface.blit(self.label, self.coord)

    def unrender(self, app):
        '''(Label, App) -> NoneType
        Blits over self.rect with app.background on app.window.'''
        if type(app.background) == tuple:
            app.window.fill(app.background, self.rect)

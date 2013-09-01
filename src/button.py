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


class Button:
    def __init__(self, COORD, WIDTH, HEIGHT, TEXT, LINE_WIDTH=1, COLOUR=(0, 0, 0)):
        '''(Button, tuple, int, int, str, int, tuple) -> NoneType
        ...'''
        X, Y = COORD

        FONT_FAMILY = None # use user pygame default
        FONT_SIZE = 12
        ANTIALIAS = True
        BACKGROUND = None

        self.rect = pygame.Rect(X, Y, WIDTH, HEIGHT)
        self.line_width = LINE_WIDTH
        self.colour = COLOUR
        self.text = pygame.font.Font(FONT_FAMILY, FONT_SIZE).render(
                TEXT, ANTIALIAS, COLOUR, BACKGROUND)

    def render(self, SURFACE, UPDATE=False):
        '''(Button, pygame.Surface, bool) -> NoneType
        ...'''
        pygame.draw.rect(SURFACE, self.colour, self.rect, self.line_width)

        TEXT_XPADDING = 0.1 * self.rect.width
        TEXT_YPADDING = 0.1 * self.rect.height
        X, Y = self.rect.x + TEXT_XPADDING, self.rect.y + TEXT_YPADDING
        SURFACE.blit(self.text, (X, Y))

        if UPDATE:
            pygame.display.update(self.rect)

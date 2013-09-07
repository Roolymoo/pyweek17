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

class Planet:
    def __init__(self, COLOUR, CENTER, RADIUS):
        '''(Planet, tuple, tuple, int) -> NoneType
        ...'''
        self.colour = COLOUR
        self.center = CENTER
        self.radius = RADIUS
        self.rect = None

    def get_data(self):
        '''(Planet) -> list
        ...'''
        return self.colour, self.center, self.radius

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

import math

#Note: The asteroid class should handle a few things:
#1. Check collision with the moon/planet
#2. Keep track of its own parameter on the path
class Asteroid():

    #Radius may not be needed; we may hard code the size
    def __init__(self, starting_x, starting_y, radius):
        '''(Asteroid, int, int, int) -> Asteroid'''
        self.radius = radius

        #Sets up the image
        self.image = pygame.image.load(
                join("data", "img", "asteroid", "asteroid_" + str(radius) + ".bmp"))

        #Note: Parameter, in addition to the orbit it is on determines coords
        self.parameter = 0
        self.current_x = starting_x
        self.curreny_y = starting_y

        #Note: this rect is the rect used to check for collision
        #Note: since the angle is 45 degrees, then the side length of the
        # square hitbox is 2(r/sqrt(2))
        self.area_halflength = int(self.radius / math.sqrt(2))
        self.area = (self.current_x - self.area_halflength, self.current_y - self.area_halflength,
                     self.area_halflength * 2, self.area_halflength * 2)

    def update_area(self, SURFACE):
        '''(Moon, pygame.display) -> Rect
        This updates the rectangle used to check for collisions with the
        moon class.  The rectangle is a hitbox that has diagonals
        45 degrees against the centre axes of symmetry.  This will return
        a Rect bounding the Asteroid.'''
        #Note: since the angle is 45 degrees, then the side length of the
        # square hitbox is 2(r/sqrt(2)); we use an approximation of 1.41 for
        # sqrt(2)
        self.area = (self.current_x - self.area_halflength, self.current_y - self.area_halflength,
                     self.area_halflength * 2, self.area_halflength * 2)
        return self.draw(SURFACE)

    def is_collision_moon(self, moon):
        '''(Asteroid, Moon) -> bool
        Returns if there is a collision with the asteroid and the moon.
        '''
        #Checks for a collision between the asteroid and the moon square hitboxes
        if self.area.colliderect(moon.area):
            return True



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
import pygame
from os.path import join

#Note: The asteroid class should handle a few things:
#1. Check collision with the moon/planet
#2. Keep track of its own parameter on the path
class Asteroid():

    #Radius may not be needed; we may hard code the size
    def __init__(self, starting_x, starting_y, radius):
        '''(Asteroid, int, int, int) -> Asteroid'''
        self.radius = radius

        #Sets up the image
        self.image = pygame.image.load(join("data", "img", "asteroid", "asteroid_" + str(radius) + ".bmp"))

        #Note: Parameter, in addition to the orbit it is on determines coords
        self.parameter = 0
        self.current_x = starting_x
        self.current_y = starting_y

        self.starting_x = starting_x
        self.starting_y = starting_y

        #self.rate describes how fast the asteroid will be approaching the planet
        #changes depending on which quadrant the asteroid starts on (origin is planet)
        self.x_rate = (400 - self.starting_x) / radius / 3

        self.y_rate = (400 - self.starting_y) / radius / 3

        #Note: this rect is the rect used to check for collision
        #Note: since the angle is 45 degrees, then the side length of the
        # square hitbox is 2(r/sqrt(2))
        self.area_halflength = int(self.radius / math.sqrt(2))
        self.area = pygame.Rect(self.current_x - self.area_halflength, self.current_y - self.area_halflength,
                     self.area_halflength * 2, self.area_halflength * 2)

    #Note: will be called when the player moves the moon around the orbit
    def update_parameter(self, SURFACE, param):
        '''(Asteroid, pygame.display, int) -> Rect
        Updates the parameter that represents the location of the asteroid
        on its path and updates the coordinates. Draws the asteroid in its
        new location and returns the Rect bounding it.
        '''
        self.parameter = param
        return self.update_coordinates(SURFACE)

    def update_coordinates(self, SURFACE):
        '''(Asteroid, pygame.display) -> Rect
        Updates the coordinates of the Asteroid and redraws it, returning
        the Rect bounding it.
        '''
        #Note that the coordinates should be as follows:
        #x = starting_x + x_rate / parameter
        #y = starting_y + y_rate / parameter
        self.current_x = self.starting_x + (self.x_rate * self.parameter)
        self.current_y = self.starting_y + (self.y_rate * self.parameter)

        return self.update_area(SURFACE)

    def update_area(self, SURFACE):
        '''(Asteroid, pygame.display) -> Rect
        This updates the rectangle used to check for collisions with the
        asteroid class.  The rectangle is a hitbox that has diagonals
        45 degrees against the centre axes of symmetry.  This will return
        a Rect bounding the Asteroid.'''
        #Note: since the angle is 45 degrees, then the side length of the
        # square hitbox is 2(r/sqrt(2)); we use an approximation of 1.41 for
        # sqrt(2)
        self.area = pygame.Rect(self.current_x - self.area_halflength, self.current_y - self.area_halflength,
                     self.area_halflength * 2, self.area_halflength * 2)
        return self.draw(SURFACE)

    def draw(self, SURFACE):
        '''(Asteroid, pygame.Surface) -> Rect
        Draws the asteroid on the surface provided and returns a Rect bounding
        the Asteroid.
        '''
        return SURFACE.blit(self.image, (self.current_x - self.radius, self.current_y - self.radius))

    def get_rect(self):
        '''(Asteroid) -> Rect
        Returns the Rect bounding the Asteroid in its current location.  This
        Rect top left corner is relative to the location of the asteroid's
        coordinates on the SURFACE.
        '''
        return pygame.Rect(self.current_x - self.radius, self.current_y - self.radius, self.radius * 2, self.radius * 2)

    def unrender(self, app):
        '''(Asteroid, App) -> Rect
        Blits over self.rect with app.background on app.window.'''
        if type(app.background) == tuple:
            app.window.fill(app.background, self.get_rect())
        return self.get_rect()

    def collides_with(self, RECT):
        '''(Asteroid, Rect) -> bool
        Returns if there is a collision with the asteroid and the Rect.
        '''
        #Checks for a collision between the asteroid and the Rect
        if self.area.colliderect(RECT):
            return True



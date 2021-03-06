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
import math
from os.path import join

#Note: the radius from the centre of the planet is determined as follows:
#Orbit 1: 100, Orbit 2: 150, ..., all the way to Orbit 5: 300 (increment 50)

#The full speed of the moon without any restrictions takes 2pi seconds to complete the revolution

#Restriction 1: Orbit path
#The path that the moon is placed on affects the speed of the moon.
#The closer it is to the planet, the faster it will go:
# Orbit 1: x1, Orbit 2: x2, ..., Orbit 5: x5 (period is multiplied by which orbit number)

#Restriction 2: Size of the moon
#The higher the radius of the moon, the slower it will go (smaller effect than orbit path)
#Radius: x(0.15 x radius) effect on the moon's period
#Note: the radius always ranges from 10 to 20, so it will have effect for sure

class Moon:

    def __init__(self, orbit_path, radius):
        '''(Moon, int, int) -> NoneType'''
        self.path = orbit_path
        self.radius = radius

        #Sets up the image
        self.image = pygame.image.load(
                join("data", "img", "moon", "moon_" + str(radius) + ".bmp"))

        #Restriction based on path and radius
        self.restrict = orbit_path * 0.1 * radius

        #Note: Parameter, in addition to the orbit it is on determines coords
        self.parameter = 0
        self.parameter_mod = 0 # for user moving moon around
        self.current_x = (((self.path - 1) * 50) + 100) * math.cos(self.parameter / self.restrict) + 400
        self.current_y = (((self.path - 1) * 50) + 100) * math.sin(self.parameter / self.restrict) + 400

        #Note: this rect is the rect used to check for collision
        #Note: since the angle is 45 degrees, then the side length of the
        # square hitbox is 2(r/sqrt(2))
        self.area_halflength = int(self.radius / math.sqrt(2))
        self.area = pygame.Rect(self.current_x - self.area_halflength, self.current_y - self.area_halflength,
                     self.area_halflength * 2, self.area_halflength * 2)

    #Note: will be called when the player places the moon on a new orbit
    def update_orbit(self, SURFACE, orbit):
        '''(Moon, pygame.display int) -> Rect
        Updates the Moon's path to the new orbit and updates the coordinates.
        Draws the Moon in its new location and returns the Rect bounding it.
        '''
        self.path = orbit
        self.restrict = orbit_path * 0.1 * radius
        return self.update_coordinates(SURFACE)

    #Note: will be called when the player moves the moon around the orbit
    def update_parameter(self, SURFACE, param):
        '''(Moon, pygame.display, int) -> Rect
        Updates the parameter that represents the location of the moon
        on the orbit path and updates the coordinates. Draws the Moon in its
        new location and returns the Rect bounding it.
        '''
        self.parameter = param + self.parameter_mod
        return self.update_coordinates(SURFACE)

    def update_coordinates(self, SURFACE):
        '''(Moon, pygame.display) -> Rect
        Updates the coordinates of the Moon and redraws the Moon, returning
        the Rect bounding it.
        '''
        #Note that the coordinates should be as follows:
        #x = (orbit radius) * cos(parameter / restriction) + planet_x
        #y = (orbit radius) * sin(parameter / restriction) + planet_y
        self.current_x = (((self.path - 1) * 50) + 100) * math.cos(self.parameter / self.restrict) + 400
        self.current_y = (((self.path - 1) * 50) + 100) * math.sin(self.parameter / self.restrict) + 400

        return self.update_area(SURFACE)

    def update_area(self, SURFACE):
        '''(Moon, pygame.display) -> Rect
        This updates the rectangle used to check for collisions with the
        asteroid class.  The rectangle is a hitbox that has diagonals
        45 degrees against the centre axes of symmetry.  This will return
        a Rect bounding the moon.'''
        #Note: since the angle is 45 degrees, then the side length of the
        # square hitbox is 2(r/sqrt(2)); we use an approximation of 1.41 for
        # sqrt(2)
        self.area = pygame.Rect(self.current_x - self.area_halflength, self.current_y - self.area_halflength,
                     self.area_halflength * 2, self.area_halflength * 2)

        return self.draw(SURFACE)

    #May not need: checking collision through rectangle bounds is less "accurate"
    def get_rect(self):
        '''(Moon) -> Rect
        Returns the Rect bounding the Moon in its current location.  This
        Rect top left corner is relative to the location of the moons
        coordinates on the SURFACE.
        '''
        return pygame.Rect(self.current_x - self.radius, self.current_y - self.radius, self.radius * 2, self.radius * 2)

    def draw(self, SURFACE):
        '''(Moon, pygame.Surface) -> Rect
        Draws the moon on the surface provided and returns a Rect bounding
        the Moon.
        '''
        return SURFACE.blit(self.image, (self.current_x - self.radius, self.current_y - self.radius))

    def unrender(self, app):
        '''(Moon, App) -> Rect
        Blits over self.rect with app.background on app.window.'''
        if type(app.background) == tuple:
            app.window.fill(app.background, self.get_rect())
        return self.get_rect()

    def is_clicked(self, MOUSE_POS):
        '''(Moon, tuple) -> bool'''
        return self.get_rect().collidepoint(MOUSE_POS)

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

#orbit_test.py
#Purpose: -understand effects of the orgiin being at the top left of the screen
#         -see how the orbit looks like
#         -(add more later)

import pygame
import math
import time

pygame.init()

black = (0, 0, 0)
white = (255, 255, 255)
colour = (141, 111, 23)

size = width, height = 800, 600

#Coordinate for the centre (planet)
centre_x = 400
centre_y = 300
centre_radius = 25

#Coodinates for the radius 15 moon
moon_radius = centre_radius + 15

screen = pygame.display.set_mode(size)

#Note: the planet is radius 25, so add on another 25 away for the first path
while 1:
    screen.fill(black)
    pygame.draw.circle(screen, colour, (centre_x, centre_y), 25)
    pygame.draw.circle(screen, colour, (int(moon_radius * math.cos(time.clock()) + centre_x), int(moon_radius * math.sin(time.clock()) + centre_y)), 15)
    pygame.display.flip()




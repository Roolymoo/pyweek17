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

size = width, height = 1000, 800

#Coordinate for the centre (planet)
centre_x = 400
centre_y = 400
centre_radius = 25

#Coodinates for the radius 15 moon
#This moon radius should depend on which orbit path
screen = pygame.display.set_mode(size)

#Note: the planet is radius 25, so add on another 25 away for the first path
while 1:
    screen.fill(black)

    #Draw the planet first
    pygame.draw.circle(screen, colour, (centre_x, centre_y), 50)

    #Example orbit paths
    pygame.draw.circle(screen, colour, (centre_x, centre_y), 100, 2)
    pygame.draw.circle(screen, colour, (centre_x, centre_y), 150, 2)
    pygame.draw.circle(screen, colour, (centre_x, centre_y), 200, 2)
    pygame.draw.circle(screen, colour, (centre_x, centre_y), 250, 2)
    pygame.draw.circle(screen, colour, (centre_x, centre_y), 300, 2)

    #Idea moon sizes: Because the paths have a radius difference of 50,
    # then at most a moon can be radius 25;
    #Ideally, we want it to be 10 to 20
    pygame.draw.rect(screen, colour, (800, 0, 200, 800))

    pygame.draw.circle(screen, colour, (int(150 * math.cos(time.clock()) + centre_x), int(150 * math.sin(time.clock()) + centre_y)), 15)
    pygame.draw.circle(screen, colour, (int(300 * math.cos(time.clock()) + centre_x), int(300 * math.sin(time.clock()) + centre_y)), 20)
    pygame.draw.circle(screen, colour, (int(250 * math.cos(time.clock()) + centre_x), int(250 * math.sin(time.clock()) + centre_y)), 10)
    pygame.display.flip()



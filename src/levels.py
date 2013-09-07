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

from planet import Planet
from moon import Moon
from asteroid import Asteroid


def load_level1(app):
    '''(App) -> NoneType
    ...'''
    RED = (255, 0, 0)

    MOON1_ORBIT, MOON1_RADIUS = 1, 20

    ASTEROID1_STARTX, ASTEROID1_STARTY, ASTEROID1_RADIUS = 0, 0, 12

    PLANET_RADIUS = 50

    app.num_orbits = 1

    app.planet = Planet(RED, app.level_center, PLANET_RADIUS)

    app.moons.append(Moon(MOON1_ORBIT, MOON1_RADIUS))

    app.asteroids.append(
            Asteroid(ASTEROID1_STARTX, ASTEROID1_STARTY, ASTEROID1_RADIUS))

    app.asteroids_ingame = app.asteroids.copy()

def load_level2(app):
    '''(App) -> NoneType
    ...'''
    BLUE = (0, 0, 255)

    MOON1_ORBIT, MOON1_RADIUS = 1, 15
    MOON2_ORBIT, MOON2_RADIUS = 3, 20

    ASTEROID1_STARTX, ASTEROID1_STARTY, ASTEROID1_RADIUS = 100, 0, 12
    ASTEROID2_STARTX, ASTEROID2_STARTY, ASTEROID2_RADIUS = 780, 800, 12
    ASTEROID3_STARTX, ASTEROID3_STARTY, ASTEROID3_RADIUS = 780, 400, 12

    PLANET_RADIUS = 50

    app.num_orbits = 3

    app.planet = Planet(BLUE, app.level_center, PLANET_RADIUS)

    app.moons.append(Moon(MOON1_ORBIT, MOON1_RADIUS))
    app.moons.append(Moon(MOON2_ORBIT, MOON2_RADIUS))

    app.asteroids.append(
            Asteroid(ASTEROID1_STARTX, ASTEROID1_STARTY, ASTEROID1_RADIUS))
    app.asteroids.append(
            Asteroid(ASTEROID2_STARTX, ASTEROID2_STARTY, ASTEROID2_RADIUS))
    app.asteroids.append(
            Asteroid(ASTEROID3_STARTX, ASTEROID3_STARTY, ASTEROID3_RADIUS))

    app.asteroids_ingame = app.asteroids.copy()

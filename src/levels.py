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

from moon import Moon


def load_level1(app):
    '''(App) -> NoneType
    ...'''
    RED = (255, 0, 0)

    MOON1_ORBIT, MOON1_RADIUS = 1, 20

    PLANET_RADIUS = 50
    app.planet = (app.window, RED, app.level_center, PLANET_RADIUS)

    app.moons.append(Moon(MOON1_ORBIT, MOON1_RADIUS))

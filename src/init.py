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

def get_init_data():
    '''(NoneType) -> dict
    Loads pygame initialization data from INIT_FILE, given below, into a dict.
    If successful, returns this dict. Otherwise, returns empty dict.'''
    INIT_FILE = "init.txt"

    INIT_DATA = ["width", "height"]
    data = {property: None for property in INIT_DATA}
    with open(INIT_FILE, "r") as FILE:
        for line in FILE:
            property, *vals = line.split()

            if property in INIT_DATA:
                data[property] = vals

    if None in data.values():
        return {}

    return data

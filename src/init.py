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

    INIT_DATA = ["width", "height", "fps"]
    
    #Initializes data for storage of width and height to NONE
    data = {property: None for property in INIT_DATA} #data[property] = None
    
    #Opens the file
    with open(INIT_FILE, "r") as FILE:
        
        #Saves the property and values
        for line in FILE:
            property, *vals = line.split() #property:string, *vals:list

            #Stores the property and values in data
            if property in INIT_DATA:
                data[property] = vals

    #We opened a stupid file with none of the properties we wanted
    if None in data.values():
        return {}

    return data

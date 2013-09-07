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
from pygame.locals import QUIT, MOUSEBUTTONUP, KEYDOWN, K_LEFT, K_RIGHT
from time import perf_counter
from os.path import join
from init import get_init_data
from render import render_title_menu_screen, render_level_menu_screen
from button import reset


class App:
    def __init__(self):
        '''(App) -> NoneType

        width           - window width
        height          - window height
        fps             - software display FPS
        fps_clock       - controls software display FPS
        running         - running status of game
        ui_elements     - currently used UI elements
        window          - the software display
        title           - game name
        background      - current background. Either a colour (tuple) ...
        status          - what kind of screen is being rendered currently.
                            - -1 no kind
                            - 0 title menu screen
                            - 1 level menu screen
                            - 2 game screen
        to_update       - pygame.Rect's of window that need updating, or None to
                          indicate that the whole display must be updated
        moons           - ...
        level_center    - ...
        planet          - ...
        play            - ...
        orbits          - ...
        old_time        - ...
        reset           - ...
        asteroids       - ...
        asteroids_ingame - ...
        selected_moon   - ...
        updated_moon_pos - ...
        num_orbits      - ...'''
        self.width = None
        self.height = None
        self.fps = None
        self.fps_clock = None
        self.running = None
        self.ui_elements = None
        self.window = None
        self.title = None
        self.background = None
        self.status = None
        self.to_update = None
        self.moons = None
        self.level_center = None
        self.planet = None
        self.play = None
        self.orbits = None
        self.old_time = None
        self.reset = None
        self.asteroids = None
        self.asteroids_ingame = None
        self.selected_moon = None
        self.updated_moon_pos = None
        self.num_orbits = None

    def __del__(self):
        '''(App) -> NoneType
        Exit Pygame.'''
        pygame.quit()

    def init(self):
        '''(App) -> int
        Initializes Pygame and loads initization data for pygame. If the data
        fails to load, returns -1. Otherwise returns 0.'''
        pygame.init()

        pygame.key.set_repeat(50, 25) # allow holding down of keys

        DATA = get_init_data()

        #get_init_data failed to get anything meaningful
        if DATA == {}:
            return -1

        #Sets up the window
        self.width = int(*DATA["width"])
        self.height = int(*DATA["height"])
        self.fps = int(*DATA["fps"])
        self.fps_clock = pygame.time.Clock()
        self.running = True
        self.ui_elements = []
        self.window = pygame.display.set_mode((self.width, self.height))
        self.title = "title"
        self.status = -1 # no kind, game is loading
        self.to_update = []
        self.moons = []
        self.level_center = (400, 400)
        self.planet = None
        self.play = False
        self.orbits = []
        self.old_time = 0
        self.reset = False
        self.asteroids = []
        self.asteroids_ingame = []
        self.selected_moon = None
        self.updated_moon_pos = False
        self.num_orbits = 0

        pygame.display.set_caption(self.title)

        render_title_menu_screen(self)

        return 0

    def exit(self):
        '''(App) -> NoneType'''
        self.running = False

    def main(self):
        '''(App) -> int
        Main routine of the game. Returns the return of self.init() if it does
        not return 0, otherwise returns 0.'''
        #Starts the game window
        init_status = self.init()
        #Failed to initialize properly
        if init_status != 0:
            return init_status

        while self.running:
            #Checks for events
            for event in pygame.event.get():
                #Exit event
                if event.type == QUIT:
                    self.exit()
                #Mouse click event
                elif event.type == MOUSEBUTTONUP:
                    mouse_pos = pygame.mouse.get_pos()
                    #Elements for ui include button
                    for ui_elem in self.ui_elements:
                        if ui_elem.is_clicked(mouse_pos):
                            ui_elem.execute(self, mouse_pos)

                    if not self.play:
                        for moon in self.moons:
                            if moon.is_clicked(mouse_pos):
                                self.selected_moon = moon
                elif event.type == KEYDOWN:
                    if self.play or (self.selected_moon == None):
                        continue

                    if event.key == K_LEFT:
                        self.selected_moon.parameter_mod -= 0.1
                        self.updated_moon_pos = True
                    elif event.key == K_RIGHT:
                        self.selected_moon.parameter_mod += 0.1
                        self.updated_moon_pos = True

            if self.play:
                for moon in self.moons:
                    self.to_update.append(moon.unrender(self))
                    if self.reset:
                        self.old_time = perf_counter()
                        self.reset = False
                    self.to_update.append(moon.update_parameter(
                                    self.window, perf_counter() - self.old_time))
                                    # self.window, moon.parameter + 0.1))

                keep = []
                i = 0
                for i in range(len(self.asteroids_ingame)):
                    asteroid = self.asteroids_ingame[i]
                    self.to_update.append(asteroid.unrender(self))
                    self.to_update.append(
                            asteroid.update_parameter(self.window, 
                                    perf_counter() - self.old_time))
                                    # asteroid.parameter + 0.1))

                    #Checks for collision with each of the moons
                    # TODO optimize ##########################################
                    for moon in self.moons:
                        if asteroid.collides_with(moon.area):
                            FILE = join("data", "audio", "effects", "moon_planet_collision.wav")
                            pygame.mixer.music.load(FILE)
                            pygame.mixer.music.play()
                            self.to_update.append(asteroid.unrender(self))
                            break
                    else:
                        keep.append(i)

                    # check for planet collision
                    if asteroid.collides_with(self.planet.rect):
                        FILE = join("data", "audio", "effects", "moon_planet_collision.wav")
                        pygame.mixer.music.load(FILE)
                        pygame.mixer.music.play()
                        reset(self)
                    i += 1

                if self.play:
                    # could be false due to planet-asteroid collision
                    self.asteroids_ingame = [(lambda i: self.asteroids_ingame[i])(i) for i in keep]

                    for orbit in self.orbits:
                        self.to_update.append(pygame.draw.circle(*orbit))

                    if self.asteroids_ingame == []:
                        # win!
                        FILE = join("data", "audio", "effects", "win.wav")
                        pygame.mixer.music.load(FILE)
                        pygame.mixer.music.play()
                        render_level_menu_screen(self)

            if self.updated_moon_pos:
                # update moons in case user moved them around
                for moon in self.moons:
                    self.to_update.append(moon.unrender(self))
                    self.to_update.append(moon.update_parameter(
                                    self.window, 0))

                for orbit in self.orbits:
                    self.to_update.append(pygame.draw.circle(*orbit))

                self.updated_moon_pos = False

            for rect in self.to_update:
                if rect == None:
                    pygame.display.update()
                    break
                pygame.display.update(rect)
            self.to_update.clear()

            self.fps_clock.tick(self.fps)

        return 0

import pygame
from pygame.locals import QUIT


class App:
    def __init__(self):
        '''(App) -> NoneType'''
        self.width = None
        self.height = None
        self.running = None
        self.window = None

    def init(self):
        '''(App) -> int'''
        self.width = 600 # TODO change from hardcode #########################
        self.height = 600 # TODO change from hardcode ########################
        self.running = True
        self.window = pygame.display.set_mode((self.width, self.height))

        # pygame.display.update()

        return 0

    def exit(self):
        '''(App) -> NoneType'''
        self.running = False

    def main(self):
        '''(App) -> int'''
        init_status = self.init()
        if init_status != 0:
            return init_status

        while self.running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.exit()

        return 0

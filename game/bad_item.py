import pygame
from pygame.locals import *

import game.constants as game_constants
import game.object_pool as object_pool

class BadItem:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = game_constants.tile_size
        self.height = game_constants.tile_size

        self.vel = game_constants.tile_size

        object_pool.register(self)

    def update(self):
        pass

    def draw(self, display_surface):
        pygame.draw.rect(display_surface, (255, 0, 0), (self.x, self.y, self.width, self.height))
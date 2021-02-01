import pygame
from pygame.locals import *

import game.constants as game_constants
import game.object_pool as object_pool

class GoodItem:
    def __init__(self, x, y):
        self.x = x
        self.y = y

        object_pool.register(self, 0)

    def update(self):
        pass

    def draw(self, display_surface):
        pygame.draw.rect(display_surface, 
        (0, 255, 0), 
        (self.x * game_constants.tile_size, self.y * game_constants.tile_size, game_constants.tile_size, game_constants.tile_size))
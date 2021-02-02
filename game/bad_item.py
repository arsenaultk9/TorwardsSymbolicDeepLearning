import pygame
from pygame.locals import *

import game.constants as game_constants
from game.object_pool import ObjectPool

class BadItem:
    def __init__(self, x, y):
        self.x = x
        self.y = y

        ObjectPool.register(self, 0)

    def update(self):
        pass

    def draw(self, display_surface):
        pygame.draw.rect(display_surface, 
        (255, 0, 0), 
        (self.x * game_constants.tile_size, self.y * game_constants.tile_size, game_constants.tile_size, game_constants.tile_size))
import pygame
from pygame.locals import *

import game.constants as game_constants
from game.object_pool import ObjectPool
from game.player_collision_pool import PlayerCollisionPool

class GoodItem:
    def __init__(self, x, y):
        self.x = x
        self.y = y

        ObjectPool.register(self, 0)

    def consume_event(self, postEvent):
        def action():
            PlayerCollisionPool.unregister(self)
            ObjectPool.unregister(self, 0)
            postEvent()
        
        return action

    def update(self):
        pass

    def draw(self, display_surface):
        pygame.draw.rect(display_surface, 
        (0, 255, 0), 
        (self.x * game_constants.tile_size, self.y * game_constants.tile_size, game_constants.tile_size, game_constants.tile_size))
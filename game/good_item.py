import os
import pygame
from pygame.locals import *

import game.constants as game_constants
from game.object_pool import ObjectPool
from game.player_collision_pool import PlayerCollisionPool


class GoodItem:
    def __init__(self, x, y):
        self.image = pygame.image.load(
            os.path.join('game\\ressources', 'good_item.png'))
        self.x = x
        self.y = y

        ObjectPool.register(self, 0)

    def coordinates(self):
        return (self.x, self.y)

    def to_text(self):
        return 'X'

    def consume_event(self, postEvent):
        def action():
            PlayerCollisionPool.unregister(self)
            ObjectPool.unregister(self, 0)
            postEvent()

        return action

    def update(self):
        pass

    def draw(self, display_surface):
        display_surface.blit(
            self.image,
            (self.x * game_constants.tile_size, self.y * game_constants.tile_size, game_constants.tile_size, game_constants.tile_size))

import os
import pygame
from pygame.locals import *

import game.constants as game_constants
from game.object_pool import ObjectPool
from game.player_collision_pool import PlayerCollisionPool


class Player:
    def __init__(self, x, y):
        self.image = pygame.image.load(
            os.path.join('game\\ressources', 'player.png'))
        self.x = x
        self.y = y

        ObjectPool.register(self, 1)

    def __move_left(self):
        if self.x - 1 < 0:
            return

        self.x -= 1
        PlayerCollisionPool.update()

    def __move_up(self):
        if self.y - 1 < 0:
            return

        self.y -= 1
        PlayerCollisionPool.update()

    def __move_right(self):
        if self.x + 1 >= game_constants.x_tile_number:
            return

        self.x += 1
        PlayerCollisionPool.update()

    def __move_down(self):
        if self.y + 1 >= game_constants.y_tile_number:
            return

        self.y += 1
        PlayerCollisionPool.update()

    def coordinates(self):
        return (self.x, self.y)

    def is_colliding_with(self, other):
        if self.x == other.x and self.y == other.y:
            return True

        return False

    def update(self):
        pressed_keys = pygame.key.get_pressed()

        if pressed_keys[K_LEFT]:
            self.__move_left()

        if pressed_keys[K_UP]:
            self.__move_up()

        if pressed_keys[K_RIGHT]:
            self.__move_right()

        if pressed_keys[K_DOWN]:
            self.__move_down()

    def draw(self, display_surface):
        display_surface.blit(
            self.image,
            (self.x * game_constants.tile_size, self.y * game_constants.tile_size, game_constants.tile_size, game_constants.tile_size))

import pygame
from pygame import constants
from pygame.locals import *

import game.constants as game_constants
import game.object_pool as object_pool
import game.player_collision_pool as player_collision_pool

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y

        object_pool.register(self, 1)

    def __move_left(self):
        self.x = max(0, self.x - 1)
        player_collision_pool.update()

    def __move_up(self):
        self.y = max(0, self.y - 1)
        player_collision_pool.update()

    def __move_right(self):
        self.x = min(game_constants.x_tile_number - 1, self.x + 1)
        player_collision_pool.update()

    def __move_down(self):
        self.y = min(game_constants.y_tile_number - 1, self.y + 1)
        player_collision_pool.update()

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
        pygame.draw.rect(display_surface, 
        (0, 0, 255), 
        (self.x * game_constants.tile_size, self.y * game_constants.tile_size, game_constants.tile_size, game_constants.tile_size))
import pygame
from pygame.locals import *

import game.constants as game_constants
import game.object_pool as object_pool

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = game_constants.tile_size
        self.height = game_constants.tile_size

        self.vel = game_constants.tile_size

        object_pool.register(self)

    def update(self):
        pressed_keys = pygame.key.get_pressed()

        if pressed_keys[K_LEFT]:
            self.move_left()

        if pressed_keys[K_UP]:
            self.move_up()

        if pressed_keys[K_RIGHT]:
            self.move_right()

        if pressed_keys[K_DOWN]:
            self.move_down()

    def move_left(self):
        self.x = max(0, self.x - self.vel)

    def move_up(self):
        self.y = max(0, self.y - self.vel)

    def move_right(self):
        self.x = min(game_constants.game_width - self.width , self.x + self.vel)

    def move_down(self):
        self.y = min(game_constants.game_height - self.height, self.y + self.vel)

    def draw(self, display_surface):
        pygame.draw.rect(display_surface, (0, 255, 0), (self.x, self.y, self.width, self.height))
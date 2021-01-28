import pygame
from pygame.locals import *

import game.constants as game_constants
from game.player import Player
from game.good_item import GoodItem
from game.bad_item import BadItem


class Level:
    def __init__(self, level_content):
        self.level_content = level_content
        self.items = []
        self.main_player = None

    def instantiate(self):
        player_x = 0
        player_y = 0

        # Draw map first and player second.
        for row_index, row in enumerate(self.level_content):
            for column_index, column_item in enumerate(row):
                if column_item == 'b':
                    bad_item = BadItem(column_index * game_constants.tile_size, row_index * game_constants.tile_size)
                    self.items.append(bad_item)

                if column_item == 'g':
                    good_item = GoodItem(column_index * game_constants.tile_size, row_index * game_constants.tile_size)
                    self.items.append(good_item)

                if column_item == 'p':
                    player_x = column_index * game_constants.tile_size
                    player_y = row_index * game_constants.tile_size 


        self.main_player = Player(player_x, player_y)

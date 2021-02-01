import pygame
from pygame.locals import *

from game.player import Player
from game.good_item import GoodItem
from game.bad_item import BadItem

from game.score import Score

import game.player_collision_pool as player_collision_pool

class Level:
    def __init__(self, level_content):
        self.level_content = level_content
        self.items = []
        self.main_player = None

    def instantiate(self):
        # Draw player first then other items
        for row_index, row in enumerate(self.level_content):
            for column_index, column_item in enumerate(row):
                if column_item == 'p':
                    self.main_player = Player(column_index, row_index)

        for row_index, row in enumerate(self.level_content):
            for column_index, column_item in enumerate(row):
                if column_item == 'b':
                    bad_item = BadItem(column_index, row_index)
                    self.items.append(bad_item)
                    player_collision_pool.register(self.main_player, bad_item, Score.decrement_score)

                if column_item == 'g':
                    good_item = GoodItem(column_index, row_index)
                    self.items.append(good_item)
                    player_collision_pool.register(self.main_player, good_item, Score.increment_score)

                


        

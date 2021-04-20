from pygame.locals import *

from game.player import Player
from game.good_item import GoodItem
from game.bad_item import BadItem

from game.score import Score
import game.constants as game_constants

from game.player_collision_pool import PlayerCollisionPool
from game.player_surroundings import player_surroundings


class Level:
    def __init__(self, level_content):
        self.level_content = level_content
        self.items = []
        self.main_player = None

    def consume_item(self, item, event):
        def consume():
            self.items.remove(item)
            event()

        return consume

    def instantiate(self):
        # Draw player first then other items
        for y_pos, row in enumerate(self.level_content):
            for x_pos, column_item in enumerate(row):
                if column_item == 'p':
                    self.main_player = Player(x_pos, y_pos)

        for y_pos, row in enumerate(self.level_content):
            for x_pos, column_item in enumerate(row):
                if column_item == 'b':
                    bad_item = BadItem(x_pos, y_pos)
                    self.items.append(bad_item)
                    remove_bad_event = self.consume_item(bad_item,
                                                         bad_item.consume_event(Score.decrement_score))

                    PlayerCollisionPool.register(
                        self.main_player, bad_item, remove_bad_event)

                if column_item == 'g':
                    good_item = GoodItem(x_pos, y_pos)
                    self.items.append(good_item)
                    remove_good_event = self.consume_item(good_item,
                                                          good_item.consume_event(Score.increment_score))

                    PlayerCollisionPool.register(
                        self.main_player, good_item, remove_good_event)

    def player_surroundings(self):
        player_surroundings(self)

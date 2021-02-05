import random
import game.constants as game_constants

class LevelGenerator:
    def __init__(self, has_good_items):
        self.has_goot_items = has_good_items
        self.player_position_x = game_constants.x_tile_number // 2
        self.player_position_y = game_constants.y_tile_number // 2

    def generate_level(self):
        level = []

        for row_index in range(game_constants.y_tile_number):
            level_row = []

            for column_index in range(game_constants.y_tile_number):
                if column_index == self.player_position_x and row_index == self.player_position_y:
                    level_row.append('p')
                    continue

                if random.randint(0, 3) == 0:
                    level_row.append('b')
                    continue

                if random.randint(0, 9) == 0 and self.has_goot_items:
                    level_row.append('g')
                    continue

                level_row.append('')

            level.append(level_row)

        return level

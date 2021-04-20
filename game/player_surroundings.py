import game.constants as game_constants


def player_surroundings(level):
    (player_x, player_y) = level.main_player.coordinates()

    (min_x, max_x) = (player_x - game_constants.player_surrounding_vision_length,
                      player_x + game_constants.player_surrounding_vision_length + 1)

    (min_y, max_y) = (player_y - game_constants.player_surrounding_vision_length,
                      player_y + game_constants.player_surrounding_vision_length + 1)

    surrounding = []

    x_repos = player_x - game_constants.player_surrounding_vision_length
    y_repos = player_y - game_constants.player_surrounding_vision_length

    for y_pos in range(min_y, max_y):
        surrounding.append([])

        for x_pos in range(min_x, max_x):
            surrounding[y_pos - y_repos].append('')

            for item in level.items:
                (item_x, item_y) = item.coordinates()

                if item_x != x_pos or item_y != y_pos:
                    continue

                surrounding[y_pos - y_repos][x_pos -
                                             x_repos] = item.to_text()

    surrounding[player_x - x_repos][player_y - y_repos] = 'p'
    print(surrounding)

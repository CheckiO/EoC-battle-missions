__author__ = 'bryukh'

from battle_mocks import *

TIME_LIMIT = 30

MAP_ELEMENTS = [
    obstacle(tile_position=[0, 0], size=20),
    obstacle(tile_position=[0, 20], size=20),
]

DEFENDERS = [
    command_center(level=4, tile_position=[25, 18], player_id=0),
    sentry_tower(level=1, tile_position=[25, 14], player_id=0, code_id=0),
    sentry_tower(level=1, tile_position=[25, 23], player_id=0, code_id=0),
    sentry_tower(level=2, tile_position=[21, 18], player_id=0, code_id=0),
]

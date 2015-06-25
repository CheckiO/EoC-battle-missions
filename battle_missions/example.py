__author__ = 'bryukh'

from battle_mocks import *

TIME_LIMIT = 30

DEFENDERS = [
    command_center(level=1, tile_position=[20, 18], player_id=0),
    sentry_tower(level=1, tile_position=[21, 14], player_id=0, code_id=0),
    sentry_tower(level=5, tile_position=[21, 23], player_id=0, code_id=0),
    sentry_tower(level=5, tile_position=[25, 23], player_id=0, code_id=0),
    crystalite_farm(level=2, tile_position=[25, 19], player_id=0),
]

MAP_ELEMENTS = [
    obstacle(tile_position=[0, 0], size=20),
    obstacle(tile_position=[0, 20], size=20),
]

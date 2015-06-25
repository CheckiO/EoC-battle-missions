__author__ = 'bryukh'

from battle_mocks import *

TIME_LIMIT = 30

MAP_ELEMENTS = [
    obstacle(tile_position=[0, 0], size=20),
    obstacle(tile_position=[0, 20], size=20),
]

DEFENDERS = [
    command_center(level=2, tile_position=[20, 18], player_id=0),
    sentry_tower(level=1, tile_position=[21, 22], player_id=0, code_id=0),
    sentry_tower(level=1, tile_position=[21, 15], player_id=0, code_id=0),
    rocket_tower(level=2, tile_position=[20, 0], player_id=0, code_id=0),
    rocket_tower(level=2, tile_position=[22, 0], player_id=0, code_id=0),
    rocket_tower(level=2, tile_position=[24, 0], player_id=0, code_id=0),
    rocket_tower(level=2, tile_position=[20, 38], player_id=0, code_id=0),
    rocket_tower(level=2, tile_position=[20, 40], player_id=0, code_id=0),
    rocket_tower(level=2, tile_position=[20, 42], player_id=0, code_id=0),
]


__author__ = 'bryukh'

from battle_mocks import *

TIME_LIMIT = 30

MAP_ELEMENTS = [
    obstacle(tile_position=[0, 0], size=20),
    obstacle(tile_position=[0, 20], size=20),
]

DEFENDERS = [
    command_center(level=2, tile_position=[20, 18], player_id=0),
    machine_gun_tower(level=3, tile_position=[28, 9], player_id=0, code_id=0),
    machine_gun_tower(level=3, tile_position=[30, 11], player_id=0, code_id=0),
    machine_gun_tower(level=3, tile_position=[28, 13], player_id=0, code_id=0),
    machine_gun_tower(level=3, tile_position=[30, 15], player_id=0, code_id=0),
    machine_gun_tower(level=3, tile_position=[28, 17], player_id=0, code_id=0),
    machine_gun_tower(level=3, tile_position=[30, 19], player_id=0, code_id=0),
    machine_gun_tower(level=3, tile_position=[28, 21], player_id=0, code_id=0),
    machine_gun_tower(level=3, tile_position=[30, 23], player_id=0, code_id=0),
    machine_gun_tower(level=3, tile_position=[28, 25], player_id=0, code_id=0),
    machine_gun_tower(level=3, tile_position=[30, 27], player_id=0, code_id=0),
    machine_gun_tower(level=3, tile_position=[28, 29], player_id=0, code_id=0),
]

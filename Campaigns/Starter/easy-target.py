from battle_mocks import *

TIME_LIMIT = 30
MAP_ELEMENTS = [
    command_center(level=1, tile_position=[20, 18], player_id=0),
    crystalite_farm(level=1, tile_position=[20, 14], player_id=0),
    crystalite_farm(level=1, tile_position=[20, 123], player_id=0),

    obstacle(tile_position=[0, 0], size=20),
    obstacle(tile_position=[0, 20], size=20),
]

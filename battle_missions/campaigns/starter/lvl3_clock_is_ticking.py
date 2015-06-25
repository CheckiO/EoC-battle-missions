from battle_mocks import *

TIME_LIMIT = 30

MAP_ELEMENTS = [
    obstacle(tile_position=[0, 0], size=20),
    obstacle(tile_position=[0, 20], size=20),
]

DEFENDERS = [
    command_center(level=1, tile_position=[20, 18], player_id=0),
    crystalite_farm(level=5, tile_position=[25, 10], player_id=0),
    crystalite_silo(level=5, tile_position=[25, 14], player_id=0),
    crystalite_farm(level=5, tile_position=[25, 18], player_id=0),
    crystalite_silo(level=5, tile_position=[25, 22], player_id=0),
    crystalite_farm(level=5, tile_position=[25, 26], player_id=0),
    crystalite_silo(level=5, tile_position=[29, 14], player_id=0),
    crystalite_farm(level=5, tile_position=[29, 18], player_id=0),
    crystalite_silo(level=5, tile_position=[29, 22], player_id=0),
]

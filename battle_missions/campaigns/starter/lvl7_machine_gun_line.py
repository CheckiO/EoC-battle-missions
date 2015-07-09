__author__ = 'bryukh'

from copy import deepcopy

from battle_mocks import *
from battle_missions.utils import template, battle_codes
from battle_missions.utils.terms import TERM

TOWER_CODE_ID = battle_codes.PY_TOWER_SHOOT_FIRST_CODE[TERM.ID]

MISSION_DATA = deepcopy(template.MISSION_DATA)

MISSION_DATA[TERM.TIME_LIMIT] = 45
MISSION_DATA[TERM.MAP_ELEMENTS] = [
    # Nature
    obstacle(tile_position=[0, 0], size=20),
    obstacle(tile_position=[0, 20], size=20),
    # Defenders
    # ==========
    # CC
    command_center(level=1, tile_position=[20, 18], player_id=0),
    # Buildings
    crystalite_farm(level=1, tile_position=[20, 0], player_id=0),
    crystalite_farm(level=1, tile_position=[20, 3], player_id=0),
    crystalite_farm(level=1, tile_position=[20, 34], player_id=0),
    crystalite_farm(level=1, tile_position=[20, 37], player_id=0),
    # Towers
    machine_gun_tower(level=3, tile_position=[29, 1], player_id=0, code_id=TOWER_CODE_ID),
    machine_gun_tower(level=3, tile_position=[29, 6], player_id=0, code_id=TOWER_CODE_ID),
    machine_gun_tower(level=3, tile_position=[29, 11], player_id=0, code_id=TOWER_CODE_ID),
    machine_gun_tower(level=3, tile_position=[29, 17], player_id=0, code_id=TOWER_CODE_ID),
    machine_gun_tower(level=3, tile_position=[29, 22], player_id=0, code_id=TOWER_CODE_ID),
    machine_gun_tower(level=3, tile_position=[29, 27], player_id=0, code_id=TOWER_CODE_ID),
    machine_gun_tower(level=3, tile_position=[29, 32], player_id=0, code_id=TOWER_CODE_ID),
    machine_gun_tower(level=3, tile_position=[29, 27], player_id=0, code_id=TOWER_CODE_ID),
]

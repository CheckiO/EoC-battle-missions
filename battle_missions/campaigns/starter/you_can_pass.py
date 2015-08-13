__author__ = 'bryukh'

from copy import deepcopy

from battle_mocks import *
from battle_missions.utils import template, battle_codes
from battle_missions.utils.terms import TERM

TOWER_CODE_ID = battle_codes.PY_TOWER_SHOOT_FIRST_CODE[TERM.ID]

MISSION_DATA = deepcopy(template.MISSION_DATA)

MISSION_DATA[TERM.TIME_LIMIT] = 100
MISSION_DATA[TERM.MAP_ELEMENTS] = [
    # Nature
    obstacle(tile_position=[0, 0], size=20),
    obstacle(tile_position=[0, 20], size=20),
    # Defenders
    # ==========
    # CC
    command_center(level=4, tile_position=[20, 12], player_id=0),
    # Buildings
    adamantite_mine(level=1, tile_position=[25, 9], player_id=0),
    adamantite_mine(level=1, tile_position=[29, 7], player_id=0),
    crystalite_farm(level=1, tile_position=[25, 16], player_id=0),
    crystalite_farm(level=1, tile_position=[29, 18], player_id=0),
    crystalite_silo(level=1, tile_position=[32, 12], player_id=0),
    # Towers
    sentry_tower(level=5, tile_position=[20, 0], player_id=0, code_id=TOWER_CODE_ID),
    sentry_tower(level=5, tile_position=[20, 26], player_id=0, code_id=TOWER_CODE_ID),
    sentry_tower(level=5, tile_position=[22, 33], player_id=0, code_id=TOWER_CODE_ID),
    sentry_tower(level=3, tile_position=[29, 12], player_id=0, code_id=TOWER_CODE_ID),
    machine_gun_tower(level=3, tile_position=[28, 5], player_id=0, code_id=TOWER_CODE_ID),
    machine_gun_tower(level=3, tile_position=[27, 20], player_id=0, code_id=TOWER_CODE_ID),
    machine_gun_tower(level=3, tile_position=[28, 25], player_id=0, code_id=TOWER_CODE_ID),
    rocket_tower(level=4, tile_position=[25, 1], player_id=0, code_id=TOWER_CODE_ID),
    rocket_tower(level=4, tile_position=[27, 1], player_id=0, code_id=TOWER_CODE_ID),
    rocket_tower(level=4, tile_position=[23, 24], player_id=0, code_id=TOWER_CODE_ID),
    rocket_tower(level=4, tile_position=[25, 24], player_id=0, code_id=TOWER_CODE_ID),
    rocket_tower(level=4, tile_position=[25, 30], player_id=0, code_id=TOWER_CODE_ID),
]

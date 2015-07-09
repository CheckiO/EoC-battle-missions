__author__ = 'bryukh'

from copy import deepcopy

from battle_mocks import *
from battle_missions.utils import template, battle_codes
from battle_missions.utils.terms import TERM

TOWER_CODE_ID = battle_codes.PY_TOWER_SHOOT_WEAKEST[TERM.ID]

MISSION_DATA = deepcopy(template.MISSION_DATA)

MISSION_DATA[TERM.TIME_LIMIT] = 60
MISSION_DATA[TERM.MAP_ELEMENTS] = [
    # Nature
    obstacle(tile_position=[0, 0], size=20),
    obstacle(tile_position=[0, 20], size=20),
    # Defenders
    # ==========
    # CC
    command_center(level=3, tile_position=[20, 18], player_id=0),
    # Buildings
    vault(level=1, tile_position=[20, 4], player_id=0),
    vault(level=1, tile_position=[20, 10], player_id=0),
    vault(level=1, tile_position=[20, 27], player_id=0),
    vault(level=1, tile_position=[20, 33], player_id=0),
    # Towers
    sentry_tower(level=1, tile_position=[22, 1], player_id=0, code_id=TOWER_CODE_ID),
    sentry_tower(level=1, tile_position=[27, 1], player_id=0, code_id=TOWER_CODE_ID),
    sentry_tower(level=1, tile_position=[22, 7], player_id=0, code_id=TOWER_CODE_ID),
    sentry_tower(level=1, tile_position=[27, 7], player_id=0, code_id=TOWER_CODE_ID),
    sentry_tower(level=1, tile_position=[22, 13], player_id=0, code_id=TOWER_CODE_ID),
    sentry_tower(level=1, tile_position=[27, 13], player_id=0, code_id=TOWER_CODE_ID),
    sentry_tower(level=1, tile_position=[22, 24], player_id=0, code_id=TOWER_CODE_ID),
    sentry_tower(level=1, tile_position=[27, 24], player_id=0, code_id=TOWER_CODE_ID),
    sentry_tower(level=1, tile_position=[22, 30], player_id=0, code_id=TOWER_CODE_ID),
    sentry_tower(level=1, tile_position=[27, 30], player_id=0, code_id=TOWER_CODE_ID),
    sentry_tower(level=1, tile_position=[22, 36], player_id=0, code_id=TOWER_CODE_ID),
    sentry_tower(level=1, tile_position=[27, 36], player_id=0, code_id=TOWER_CODE_ID),
    sentry_tower(level=1, tile_position=[25, 17], player_id=0, code_id=TOWER_CODE_ID),
    sentry_tower(level=1, tile_position=[25, 20], player_id=0, code_id=TOWER_CODE_ID),
]

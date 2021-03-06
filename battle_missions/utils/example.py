from battle_missions.utils import template, battle_codes

__author__ = 'bryukh'

from copy import deepcopy

from battle_mocks import *
from battle_missions.utils import template, battle_codes
from battle_missions.utils.terms import TERM

TOWER_CODE_ID = battle_codes.PY_TOWER_SHOOT_FIRST_CODE[TERM.ID]

MISSION_DATA = deepcopy(template.MISSION_DATA)

MISSION_DATA[TERM.TIME_LIMIT] = 30
MISSION_DATA[TERM.MAP_ELEMENTS] = [
    # Nature
    obstacle(tile_position=[0, 0], size=20),
    obstacle(tile_position=[0, 20], size=20),
    # Defenders
    command_center(level=1, tile_position=[20, 18], player_id=0),
    sentry_tower(level=1, tile_position=[21, 14], player_id=0, code_id=TOWER_CODE_ID),
    sentry_tower(level=5, tile_position=[21, 23], player_id=0, code_id=TOWER_CODE_ID),
    sentry_tower(level=5, tile_position=[25, 23], player_id=0, code_id=TOWER_CODE_ID),
    crystalite_farm(level=2, tile_position=[25, 19], player_id=0),
]

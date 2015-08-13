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
    command_center(level=2, tile_position=[20, 18], player_id=0),
    machine_gun_tower(level=3, tile_position=[28, 9], player_id=0, code_id=TOWER_CODE_ID),
    machine_gun_tower(level=3, tile_position=[30, 9], player_id=0, code_id=TOWER_CODE_ID),
    machine_gun_tower(level=3, tile_position=[28, 11], player_id=0, code_id=TOWER_CODE_ID),
    machine_gun_tower(level=3, tile_position=[30, 11], player_id=0, code_id=TOWER_CODE_ID),
    machine_gun_tower(level=3, tile_position=[28, 13], player_id=0, code_id=TOWER_CODE_ID),
    machine_gun_tower(level=3, tile_position=[30, 13], player_id=0, code_id=TOWER_CODE_ID),
    machine_gun_tower(level=3, tile_position=[28, 15], player_id=0, code_id=TOWER_CODE_ID),
    machine_gun_tower(level=3, tile_position=[30, 15], player_id=0, code_id=TOWER_CODE_ID),
    machine_gun_tower(level=3, tile_position=[28, 17], player_id=0, code_id=TOWER_CODE_ID),
    machine_gun_tower(level=3, tile_position=[30, 17], player_id=0, code_id=TOWER_CODE_ID),
    machine_gun_tower(level=3, tile_position=[28, 19], player_id=0, code_id=TOWER_CODE_ID),
    machine_gun_tower(level=3, tile_position=[30, 19], player_id=0, code_id=TOWER_CODE_ID),
    machine_gun_tower(level=3, tile_position=[28, 21], player_id=0, code_id=TOWER_CODE_ID),
    machine_gun_tower(level=3, tile_position=[30, 21], player_id=0, code_id=TOWER_CODE_ID),
    machine_gun_tower(level=3, tile_position=[28, 23], player_id=0, code_id=TOWER_CODE_ID),
    machine_gun_tower(level=3, tile_position=[30, 23], player_id=0, code_id=TOWER_CODE_ID),
    machine_gun_tower(level=3, tile_position=[28, 25], player_id=0, code_id=TOWER_CODE_ID),
    machine_gun_tower(level=3, tile_position=[30, 25], player_id=0, code_id=TOWER_CODE_ID),
    machine_gun_tower(level=3, tile_position=[28, 27], player_id=0, code_id=TOWER_CODE_ID),
    machine_gun_tower(level=3, tile_position=[30, 27], player_id=0, code_id=TOWER_CODE_ID),
    machine_gun_tower(level=3, tile_position=[28, 29], player_id=0, code_id=TOWER_CODE_ID),
    machine_gun_tower(level=3, tile_position=[30, 29], player_id=0, code_id=TOWER_CODE_ID),
]

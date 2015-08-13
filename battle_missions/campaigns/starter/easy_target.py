from battle_missions.utils import template

__author__ = 'bryukh'

from copy import deepcopy

from battle_mocks import *
from battle_missions.utils import template
from battle_missions.utils.terms import TERM

MISSION_DATA = deepcopy(template.MISSION_DATA)

MISSION_DATA[TERM.TIME_LIMIT] = 30
MISSION_DATA[TERM.MAP_ELEMENTS] = [
    # Nature
    obstacle(tile_position=[0, 0], size=20),
    obstacle(tile_position=[0, 20], size=20),
    # Defenders
    command_center(level=1, tile_position=[20, 18], player_id=0),
    crystalite_farm(level=1, tile_position=[20, 14], player_id=0),
    crystalite_farm(level=1, tile_position=[20, 23], player_id=0),
]


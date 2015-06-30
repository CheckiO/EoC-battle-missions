from battle_missions.utils import battle_codes

MISSION_DATA = {
    # Required for console output
    'is_stream': True,
    'map_size': (40, 40),
    # Player information
    'players': [
        {'defeat': ['center'], 'env_name': 'python_3', 'id': 0},
        {'defeat': ['units', 'time'], 'env_name': 'python_3', 'id': 1}],
    'rewards': {'adamantite': 400, 'crystalite': 150},
    # If 'time' in defeat reasons, then after this time limit the player are defeated
    'time_limit': 0,

    # Building, obstacles and units
    # Units appears from crafts in random places on the edge
    'map_elements': [],
    # Player Codes
    'codes': [
        battle_codes.PY_TOWER_SHOOT_FIRST_CODE,
    ],
}
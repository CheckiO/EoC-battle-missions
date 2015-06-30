__all__ = ["SHOOT_FIRST_CODE"]

PY_TOWER_SHOOT_FIRST_CODE = {
    "id": 1000,
    "code": """
from battle import commander

tower_client = commander.Client()


def search_next_target(data, **kwargs):
    enemies = tower_client.ask_enemy_items_in_my_firing_range()
    if enemies:
        unit_in_firing_range(enemies[0])
    else:
        tower_client.subscribe_enemy_in_my_firing_range(unit_in_firing_range)


def unit_in_firing_range(data, **kwargs):
    tower_client.attack_item(data['id'])
    tower_client.subscribe_im_idle(search_next_target)

tower_client.subscribe_enemy_in_my_firing_range(unit_in_firing_range)
"""
}

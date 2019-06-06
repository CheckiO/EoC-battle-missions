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
        tower_client.when_enemy_in_range(unit_in_firing_range)


def unit_in_firing_range(data, **kwargs):
    tower_client.attack_item(data['id'])
    tower_client.when_im_idle(search_next_target)

tower_client.when_enemy_in_range(unit_in_firing_range)
"""
}

PY_TOWER_SHOOT_WEAKEST = {
    "id": 1001,
    "code": """
from battle import commander

tower_client = commander.Client()

current_id = None


def search_next_target(data, **kwargs):
    global current_id
    current_id = None
    enemies = tower_client.ask_enemy_items_in_my_firing_range()
    if enemies:
        weakest = min(enemies, key=lambda x: x["hit_points"])
        unit_in_firing_range(weakest)
    else:
        tower_client.when_enemy_in_range(unit_in_firing_range)


def unit_in_firing_range(data, **kwargs):
    global current_id
    if current_id:
        if data['id'] == current_id:
            tower_client.attack_item(data['id'])
        else:
            tower_client.attack_item(
                data['id']
                if data["hit_points"] < tower_client.ask_item_info(current_id)["hit_points"]
                else current_id)
    else:
        current_id = data["id"]
        tower_client.attack_item(data["id"])
    tower_client.unsubscribe_all()
    tower_client.when_im_idle(search_next_target)


tower_client.when_enemy_in_range(unit_in_firing_range)
"""
}

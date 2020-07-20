from arena_log.model.actions.activate import Activate
from arena_log.model.actions.cast import Cast
from arena_log.model.actions.pass_ import Pass
from arena_log.model.actions.play import Play
from arena_log.model.actions.activate_mana import ActivateMana
from arena_log.model.actions.float_mana import FloatMana
from arena_log.model.actions.cast_adventure import CastAdventure

ACTION_LIST = {
    'Activate': Activate,
    'Cast': Cast,
    'Pass': Pass,
    'Play': Play,
    'Activate_Mana': ActivateMana,
    'FloatMana': FloatMana,
    'CastAdventure': CastAdventure
}


def get_action(option):
    action = '_'.join(option.split('_')[1:])
    try:
        return ACTION_LIST[action]
    except KeyError as err:
        print(f'{err}: Action {action} not found')
        raise KeyError

from arena_log.model.items.mana_cost import mana_cost_list


class Activate:

    def __init__(self, content):
        self.grp_id = content['grpId']
        self.instance_id = content['instanceId']
        self.ability_grp_id = content['abilityGrpId']
        self.mana_cost = mana_cost_list(content.get('manaCost'))
        self.should_stop = content.get('shouldStop')
        self.cost_selection_ids = content.get('costSelectionIds')

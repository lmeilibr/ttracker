from arena_log.model.items.mana_cost import mana_cost_list

class CastAdventure:

    def __init__(self, content):
        self.grp_id = content['grpId']
        self.instance_id = content['instanceId']
        self.mana_cost = mana_cost_list(content['manaCost'])
        self.should_stop = content.get('shouldStop')
        self.auto_tap_solution = content.get('autoTapSolution')

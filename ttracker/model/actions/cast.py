from ttracker.model.items.mana_cost import mana_cost_list


class Cast:
    def __init__(self, content):
        self.grp_id = content['grpId']
        self.instance_id = content['instanceId']
        self.mana_cost = mana_cost_list(content['manaCost'])
        self.should_stop = content.get('shouldStop')

class ManaCost:

    def __init__(self, content):
        self.color = content['color']
        self.count = content['count']
        self.costId = content.get('costId')


def mana_cost_list(item):
    if item:
        return [ManaCost(mana_cost) for mana_cost in item]

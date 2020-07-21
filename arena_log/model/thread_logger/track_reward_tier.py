class Updated:
    def __init__(self, content):
        self.tiers_added = content['payload']['tiersAdded']
        self.orb_count_diff = content['payload']['orbCountDiff']
        self.inventory_updates = content['payload']['inventoryUpdates']

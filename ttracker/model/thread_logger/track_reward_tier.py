class Updated:
    def __init__(self, payload):
        self.tiers_added = payload['tiersAdded']
        self.orb_count_diff = payload['orbCountDiff']
        self.inventory_updates = payload['inventoryUpdates']

""" Track the Season Pass Progress """


class GetPlayerProgress:
    def __init__(self, payload):
        self.active_battle_pass = payload['activeBattlePass']
        self.expired_battle_pass = payload['expiredBattlePasses']
        self.current_renewal_id = payload['currentRenewalId']

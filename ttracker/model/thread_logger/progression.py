""" Track the Season Pass Progress """


class GetPlayerProgress:
    def __init__(self, content):
        if 'request' not in content:
            self.active_battle_pass = content['payload']['activeBattlePass']
            self.expired_battle_pass = content['payload']['expiredBattlePasses']
            self.current_renewal_id = content['payload']['currentRenewalId']

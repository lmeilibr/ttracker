class DieRollResultsResp:

    def __init__(self, content):
        self.msg_id = content['msgId']
        self.system_seat_ids = content['systemSeatIds']
        self.player_die_rolls = self.get_player_die_rolls(
            content['dieRollResultsResp']['playerDieRolls'])

    def get_player_die_rolls(self, content):
        return [PlayerDieRoll(roll) for roll in content]


class PlayerDieRoll:

    def __init__(self, content):
        self.system_seat_id = content['systemSeatId']
        self.roll_value = content['rollValue']

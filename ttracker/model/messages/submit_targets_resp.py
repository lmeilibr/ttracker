class SubmitTargetsResp:

    def __init__(self, content):
        self.system_seat_ids = content['systemSeatIds']
        self.msg_id = content['systemSeatIds']
        self.game_state_id = content['gameStateId']
        self.result = content['submitTargetsResp']['result']

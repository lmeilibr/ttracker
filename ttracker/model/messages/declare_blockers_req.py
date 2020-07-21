class DeclareblockerReq:

    def __init__(self, content):
        self.system_seats_ids = content['systemSeatIds']
        self.msg_id = content['msgId']
        self.game_state_id = content['gameStateId']
        self.prompt = content['prompt']
        self.blockers = content['declareBlockersReq']['blockers']

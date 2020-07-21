from ttracker.model.messages.prompt_req import Prompt


class DeclareAttackersReq:
    def __init__(self, content):
        self.system_seat_ids = content['systemSeatIds']
        self.msg_id = content['msgId']
        self.game_state_id = content['gameStateId']
        self.prompt = Prompt(content['prompt'])
        self.attackers = content['declareAttackersReq']['attackers']
        self.attackers = content['declareAttackersReq']['autoAttackers']

from ttracker.model.messages.prompt_req import Prompt

class SubmitBlockersResp:
    def __init__(self, content):
        self.system_seat_ids = content['systemSeatIds']
        self.msg_id = content['msgId']
        self.game_state_id = content['gameStateId']
        self.prompt = Prompt(content['prompt'])
        self.result = content['submitBlockersResp']['result']
        self.non_decision_player_prompt = content['nonDecisionPlayerPrompt']

from arena_log.model.messages.prompt_req import Prompt


class CastingTimeOptionsReq:
    def __init__(self, content):
        self.system_seat_ids = content['systemSeatIds']
        self.msg_id = content['msgId']
        self.game_state_id = content['gameStateId']
        self.prompt = Prompt(content['prompt'])
        self.non_decision_player_prompt = Prompt(
            content['nonDecisionPlayerPrompt'])
        self.casting_time_options_req = content['castingTimeOptionsReq']
        self.allow_cancel = content['allowCancel']
        self.allow_undo = content['allowUndo']

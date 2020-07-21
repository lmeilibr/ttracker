from ttracker.model.messages.prompt_req import Prompt


class OrderReq:

    def __init__(self, content):
        self.system_seat_ids = content['systemSeatIds']
        self.msg_id = content['msgId']
        self.game_state_id = content['gameStateId']
        self.prompt = Prompt(content['prompt'])
        self.order_req = content['orderReq']
        self.non_decision_player_prompt = content['nonDecisionPlayerPrompt']
        self.allow_cancel = content.get('allowCancel')
        self.allow_undo = content.get('allowUndo')

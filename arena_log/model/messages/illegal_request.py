from arena_log.model.messages.prompt_req import Prompt

class IllegalRequest:

    def __init__(self, content):
        self.system_seat_ids = content['systemSeatIds']
        self.msg_id = content['msgId']
        self.game_state_id = content['gameStateId']
        self.prompt = Prompt(content['prompt'])
        self.illegal_request_message = content['illegalRequestMessage']

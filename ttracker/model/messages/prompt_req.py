class PromptReq:

    def __init__(self, content):
        self.system_seat_ids = content['systemSeatIds']
        self.msg_id = content['msgId']
        self.game_state_id = content['gameStateId']
        self.prompt = Prompt(content['prompt'])


class Prompt:

    def __init__(self, content):
        self.prompt_id = content.get('promptId')
        self.parameters = content.get('parameters')

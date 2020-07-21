from ttracker.model.messages.prompt_req import Prompt

class GroupReq:

    def __init__(self, content):
        self.system_seat_ids = content['systemSeatIds']
        self.msg_id = content['msgId']
        self.game_state_id = content['gameStateId']
        self.prompt = Prompt(content['prompt'])
        self.non_decision_prompt = Prompt(content['nonDecisionPlayerPrompt'])
        self.instance_id = content['groupReq']['instanceIds']
        self.group_specs = content['groupReq']['groupSpecs']
        self.total_selected = content['groupReq']['totalSelected']
        self.group_type = content['groupReq']['groupType']
        self.context = content['groupReq']['context']
        self.source_id = content['groupReq']['sourceId']


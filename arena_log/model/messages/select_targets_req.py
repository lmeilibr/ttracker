from arena_log.model.messages.prompt_req import Prompt

class SelectTargetsReq:

    def __init__(self, content):
        self.system_seat_ids = content['systemSeatIds']
        self.msg_id = content['msgId']
        self.game_state_id = content['gameStateId']
        self.prompt = Prompt(content['prompt'])
        self.targets = content['selectTargetsReq']['targets']
        self.source_id = content['selectTargetsReq']['sourceId']
        self.ability_grp_id = content['selectTargetsReq']['abilityGrpId']
        self.allow_cancel = content['allowCancel']
        self.allow_undo = content.get('allowUndo')

from ttracker.model.messages.prompt_req import Prompt


class SelectNReq:

    def __init__(self, content):
        self.system_seat_ids = content['systemSeatIds']
        self.msg_id = content['msgId']
        self.game_state_id = content['gameStateId']
        self.prompt = Prompt(content['prompt'])
        self.max_sel = content['selectNReq']['maxSel']
        self.context = content['selectNReq']['context']
        self.option_type = content['selectNReq'].get('optionType')
        self.option_context = content['selectNReq']['optionContext']
        self.list_type = content['selectNReq']['listType']
        self.ids = content['selectNReq']['ids']
        self.idx = content['selectNReq'].get('idx')
        self.select_prompt = content['selectNReq'].get('prompt')
        self.id_type = content['selectNReq']['idType']
        self.source_id = content['selectNReq'].get('sourceId')
        self.validation_type = content['selectNReq']['validationType']

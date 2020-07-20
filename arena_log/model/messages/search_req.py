from arena_log.model.messages.prompt_req import Prompt


class SearchReq:
    def __init__(self, content):
        self.system_seat_ids = content['systemSeatIds']
        self.msg_id = content['msgId']
        self.game_state_id = content['gameStateId']
        self.prompt = Prompt(content['prompt'])
        self.non_decision_player_prompt = Prompt(
            content['nonDecisionPlayerPrompt'])
        self.option_index = content['searchReq']['optionIndex']
        self.max_find = content['searchReq']['maxFind']
        self.zones_to_search = content['searchReq']['zonesToSearch']
        self.items_to_search = content['searchReq']['itemsToSearch']
        self.items_sought = content['searchReq']['itemsSought']
        self.source_id = content['searchReq']['sourceId']
        self.allow_cancel = content['allowCancel']

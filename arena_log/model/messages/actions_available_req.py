from arena_log.model.messages.prompt_req import Prompt
from arena_log.model.actions import get_action


class ActionsAvailableReq:
    def __init__(self, content):
        self.system_seat_ids = content['systemSeatIds']
        self.msg_id = content['msgId']
        self.game_state_id = content['gameStateId']
        self.prompt = Prompt(content['prompt'])
        self.actions_available_req = self.get_actions(
            content['actionsAvailableReq'].get('actions'))
        self.inactive_actions = self.get_actions(
            content['actionsAvailableReq'].get('inactiveActions'))

    def get_actions(self, content):
        if not content:
            return
        action_list = []
        for action in content:
            action_type = get_action(action['actionType'])
            if not action_type:
                print()
            parsed = action_type(action)
            action_list.append(parsed)
        return action_list





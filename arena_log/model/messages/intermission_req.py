from arena_log.model.items.match import Result
from arena_log.model.messages.prompt_req import Prompt


class IntermissionReq:

    def __init__(self, content):
        self.system_seat_ids = content['systemSeatIds']
        self.msg_id = content['msgId']
        self.game_state_id = content['gameStateId']
        self.options = content['intermissionReq']['options']
        self.intermission_prompt = Prompt(
            content['intermissionReq']['intermissionPrompt'])
        self.game_result_type = content['intermissionReq']['gameResultType']
        self.winning_team_id = content['intermissionReq']['winningTeamId']
        self.result = Result(content['intermissionReq']['result'])

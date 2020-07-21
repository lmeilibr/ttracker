class ChooseStartingPlayerReq:

    def __init__(self, content):
        self.system_seat_id = content['systemSeatIds']
        self.msg_id = content['msgId']
        self.team_type = content['chooseStartingPlayerReq']['teamType']
        self.starting_player_ids = content['chooseStartingPlayerReq'][
            'systemSeatIds']

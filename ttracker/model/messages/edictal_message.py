class EdictalMessage:

    def __init__(self, content):
        self.system_seats_ids = content['systemSeatIds']
        self.msg_id = content['msgId']
        self.game_state_id = content['gameStateId']
        self.edictal_message = content['edictalMessage']

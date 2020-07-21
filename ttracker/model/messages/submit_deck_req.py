from ttracker.model.items.deck import Deck


class SubmitDeckReq:

    def __init__(self, content):
        self.system_seat_ids = content['systemSeatIds']
        self.msg_id = content['msgId']
        self.game_state_id = content['gameStateId']
        self.deck = Deck(content['submitDeckReq']['deck'])

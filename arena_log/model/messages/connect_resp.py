from arena_log.model.items.deck import Deck


class ConnectResp:

    def __init__(self, content):
        self.system_seat_ids = content['systemSeatIds']
        self.msg_id = content['msgId']
        self.deck_message = Deck(content['connectResp']['deckMessage'])



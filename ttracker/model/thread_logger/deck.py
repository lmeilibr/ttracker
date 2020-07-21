from ttracker.model.items.deck import DeckList


class CreateDeckV3:
    def __init__(self, payload):
        self.deck = DeckList(payload)


class GetDeckListsV3:
    def __init__(self, payload):
        self.deck_lists = self.get_deck_lists(payload)

    def get_deck_lists(self, payload):
        return [DeckList(deck) for deck in payload]


class GetPreconDecksV3:
    def __init__(self, payload):
        pass


class UpdateDeckV3:
    def __init__(self, payload):
        self.deck = DeckList(payload)

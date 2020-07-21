from ttracker.model.items.deck import DeckList


class CreateDeckV3:
    def __init__(self, content):
        if 'request' not in content:
            self.deck = DeckList(content['payload'])


class GetDeckListsV3:
    def __init__(self, content):
        if 'request' not in content:
            self.deck_lists = self.get_deck_lists(content['payload'])

    def get_deck_lists(self, payload):
        return [DeckList(deck) for deck in payload]


class GetPreconDecksV3:
    pass


class UpdateDeckV3:
    def __init__(self, content):
        if 'request' not in content:
            self.deck = DeckList(content['payload'])

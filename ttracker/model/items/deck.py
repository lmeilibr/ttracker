class Deck:
    def __init__(self, content):
        self.deck_cards = content['deckCards']
        self.sideboard_cards = content.get('sideboardCards')


class DeckList:
    def __init__(self, content):
        self.command_zone_grp_ids = content['commandZoneGRPIds']
        self.last_played = content['attributes']['lastPlayed']
        self.companion_grp_id = content['companionGRPId']
        self.main_deck = content['mainDeck']
        self.sideboard = content['sideboard']
        self.is_valid = content['isValid']
        self.isCompanionValid = content['isCompanionValid']
        self.locked_for_use = content['lockedForUse']
        self.locked_for_edit = content['lockedForEdit']
        self.resource_id = content['resourceId']
        self.card_skins = content['cardSkins']
        self.id = content['id']
        self.name = content['name']
        self.description = content['description']
        self.format = content['format']
        self.deck_tile_id = content['deckTileId']
        self.card_back = content['cardBack']
        self.last_updated = content['lastUpdated']


class Card:

    def __init__(self, content):
        self.arena_id = content['id']
        self.quantity = content['quantity']

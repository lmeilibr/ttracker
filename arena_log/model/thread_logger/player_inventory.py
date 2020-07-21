from arena_log.model.items import Format
from arena_log.model.items.deck import Card


class GetFormats:
    def __init__(self, content):
        if 'request' not in content:
            self.formats = self.get_formats(content)

    def get_formats(self, content):
        return [Format(format) for format in content['payload']]


class GetPlayersCardsV3:
    def __init__(self, content):
        if 'request' not in content:
            self.player_cards = self.get_player_cards(content['payload'])

    def get_player_cards(self, payload):
        return [Card({'id': key, 'quantity': value})
                for key, value in
                payload.items()]


class GetPlayerInventory:
    def __init__(self, content):
        if 'request' not in content:
            payload = content['payload']
            self.player_id = payload['playerId']
            self.wc_common = payload['wcCommon']
            self.wc_uncommon = payload['wcUncommon']
            self.wc_rare = payload['wcRare']
            self.wc_mythic = payload['wcMythic']
            self.gold = payload['gold']
            self.gems = payload['gems']
            self.draft_tokens = payload['draftTokens']
            self.sealed_tokens = payload['sealedTokens']
            self.wc_track_position = payload['wcTrackPosition']
            self.vault_progress = payload['vaultProgress']
            self.boosters = payload['boosters']
            self.vanity_items = payload['vanityItems']
            self.vanity_selections = payload['vanitySelections']
            self.vouchers = payload['vouchers']
            self.basic_land_set = payload['basicLandSet']
            self.latest_basic_land_set = payload['latestBasicLandSet']
            self.starter_decks = payload['starterDecks']
            self.first_seen_date = payload['firstSeenDate']
            self.event_tokens = payload['eventTokens']


class GetRewardSchedule:
    def __init__(self, content):
        if 'request' not in content:
            payload = content['payload']
            self.daily_reset = payload['dailyReset']
            self.weekly_reset = payload['weeklyReset']
            self.daily_rewards = payload['dailyRewards']
            self.weekly_rewards = payload['weeklyRewards']
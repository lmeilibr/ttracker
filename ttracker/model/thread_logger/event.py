from ttracker.model.items.deck import DeckList


class UpdateDeckV3:
    pass


class DeckSubmitV3:
    def __init__(self, content):
        if 'request' not in content:
            payload = content['payload']
            self.id = payload['Id']
            self.internal_event_name = payload['InternalEventName']
            self.player_id = payload['PlayerId']
            self.event_type = payload['EventType']
            self.event_sub_type = payload['EventSubType']
            self.module_instance_data = payload['ModuleInstanceData']
            self.current_event_state = payload['CurrentEventState']
            self.current_module = payload['CurrentModule']
            self.card_pool = payload['CardPool']
            self.course_deck = DeckList(payload['CourseDeck'])
            self.previous_opponents = payload['PreviousOpponents']


class GetActiveEventsV2:
    def __init__(self, content):
        if 'request' not in content:
            self.events = content['payload']


class GetActiveMatches:
    def __init__(self, content):
        if 'request' not in content:
            self.id = content['id']


class GetCombinedRankInfo:
    def __init__(self, content):
        if 'request' not in content:
            payload = content['payload']

            self.player_id = payload['playerId']
            self.constructed_season_ordinal = payload[
                'constructedSeasonOrdinal']
            self.constructed_class = payload['constructedClass']
            self.constructed_level = payload['constructedLevel']
            self.constructed_step = payload['constructedStep']
            self.constructed_matches_won = payload['constructedMatchesWon']
            self.constructed_matches_lost = payload['constructedMatchesLost']
            self.constructed_matches_drawn = payload['constructedMatchesDrawn']
            self.limited_season_ordinal = payload['limitedSeasonOrdinal']
            self.limited_class = payload['limitedClass']
            self.limited_level = payload['limitedLevel']
            self.limited_step = payload['limitedStep']
            self.limited_matches_won = payload['limitedMatchesWon']
            self.limited_matches_lost = payload['limitedMatchesLost']
            self.limited_matches_drawn = payload['limitedMatchesDrawn']
            self.constructed_percentile = payload['constructedPercentile']
            self.constructed_leaderboard_place = payload[
                'constructedLeaderboardPlace']
            self.limited_percentile = payload['limitedPercentile']
            self.limited_leaderboard_place = payload['limitedLeaderboardPlace']


class GetPlayerCourseV2:
    def __init__(self, content):
        if 'request' not in content:
            self.player_course = DeckSubmitV3(content)


class GetPlayerCoursesV2:
    def __init__(self, content):
        if 'request' not in content:
            self.player_courses = content['payload']


class GetSeasonAndRankDetail:
    def __init__(self, content):
        if 'request' not in content:
            self.current_season = content['payload']['currentSeason']
            self.limited_rank_info = content['payload']['limitedRankInfo']
            self.constructed_rank_info = content['payload'][
                'constructedRankInfo']


class Join:
    def __init__(self, content):
        if 'request' not in content:
            self.join = content['payload']


class JoinQueue:
    def __init__(self, content):
        if 'request' not in content:
            self.result = content['payload']


class MatchCreated:
    def __init__(self, content):
        if 'request' not in content:
            payload = content['payload']
            self.controller_fabric_uri = payload['controllerFabricUri']
            self.match_endpoint_host = payload['matchEndpointHost']
            self.match_endpoint_port = payload['matchEndpointPort']
            self.opponent_screen_name = payload['opponentScreenName']
            self.opponent_is_wotc = payload['opponentIsWotc']
            self.match_id = payload['matchId']
            self.opponent_ranking_class = payload['opponentRankingClass']
            self.opponent_ranking_tier = payload['opponentRankingTier']
            self.opponentMythicPercentile = payload['opponentMythicPercentile']
            self.opponentMythicLeaderboardPlace = payload[
                'opponentMythicLeaderboardPlace']
            self.eventId = payload['eventId']
            self.opponent_avatar_selection = payload['opponentAvatarSelection']
            self.opponent_card_back_selection = payload[
                'opponentCardBackSelection']
            self.opponent_pet_selection = payload['opponentPetSelection']
            self.avatar_selection = payload['avatarSelection']
            self.cardback_selection = payload['cardbackSelection']
            self.pet_selection = payload['petSelection']
            self.battlefield = payload['battlefield']
            self.opponent_commander_grp_ids = payload['opponentCommanderGrpIds']
            self.commander_grp_ids = payload['commanderGrpIds']
            self.match_type = payload['matchType']

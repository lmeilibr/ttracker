class UpdateDeckV3:
    pass


class DeckSubmitV3:
    pass


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
    pass


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
    pass


class JoinQueue:
    pass


class MatchCreated:
    pass

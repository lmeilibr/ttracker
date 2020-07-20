class Result:

    def __init__(self, content):
        self.scope = content['scope']
        self.result = content['result']
        self.winning_team_id = content['winningTeamId']
        self.reason = content.get('reason')


class MatchResult:

    def __init__(self, content):
        if content:
            self.match_id = content.get('matchId')
            self.match_completed_reason = content['matchCompletedReason']
            self.resultList = self.get_result_list(content)

    @staticmethod
    def get_result_list(content):
        return [Result(result) for result in content['resultList']]


class FinalMatchResult:

    def __init__(self, content):
        self.match_id = content['matchId']
        self.match_completed_reason = content['matchCompletedReason']
        self.resultList = content['resultList']


class Deck:
    def __init__(self, content):
        self.deck_cards = content['deckCards']
        self.sideboard_cards = content.get('sideboardCards')
        print(self.deck_cards)
        print(self.sideboard_cards)

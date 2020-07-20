from arena_log.model.items.match import MatchResult


class Player:

    def __init__(self, content):
        self.user_id = content['userId']
        self.player_name = content['playerName']
        self.system_seat_id = content['systemSeatId']
        self.team_id = content['teamId']

    def __repr__(self):
        return f'<{self.__class__.__name__}>'

    def __str__(self):
        return f'<{self.player_name}>'


class GameRoomConfig:

    def __init__(self, content):
        self.event_id = content['eventId']
        self.reserved_players = self.get_reserved_players(content)
        self.match_id = content['matchId']

    @staticmethod
    def get_reserved_players(content):
        if content.get('reservedPlayers'):
            return [Player(player) for player in content['reservedPlayers']]

    def __repr__(self):
        return f'<{self.__class__.__name__}>'

    def __str__(self):
        return f'<{self.match_id}>'


class MatchGameRoomStateChangedEvent:

    def __init__(self, content):
        self.transaction_id = content['transactionId']
        self.timestamp = content['timestamp']

        game_room_info = content['matchGameRoomStateChangedEvent'][
            'gameRoomInfo']
        self.game_room_config = GameRoomConfig(
            game_room_info['gameRoomConfig'])
        self.state_type = game_room_info['stateType']

        self.final_match_result = MatchResult(
            game_room_info.get('finalMatchResult', None))

    def __repr__(self):
        return f'<{self.__class__.__name__}>'

    def __str__(self):
        return f'<{self.event_id}>'

class GameStateMessage:
    def __init__(self, content):
        self.system_seat_ids = content['systemSeatIds']
        self.msg_id = content['msgId']
        self.game_state_id = content['gameStateId']
        self.game_info = GameInfo(content['gameStateMessage'].get('gameInfo'))
        self.teams = self.get_teams(content['gameStateMessage'].get('teams'))
        self.players = self.get_players(content['gameStateMessage'].get('players'))
        self.turn_info = TurnInfo(content['gameStateMessage'].get('turnInfo'))
        self.zones = self.get_zones(content['gameStateMessage'].get('zones'))
        self.diff_deleted_instance_ids = content['gameStateMessage'].get('diffDeletedInstanceIds')
        self.pending_message_count = content['gameStateMessage'].get('pendingMessageCount')
        self.timers = content['gameStateMessage'].get('timers')
        self.update = content['gameStateMessage']['update']

    @staticmethod
    def get_teams(content):
        if content:
            return [Team(team) for team in content]

    @staticmethod
    def get_players(content):
        if content:
            return [Player(player) for player in content]

    @staticmethod
    def get_zones(content):
        if content:
            return [Zone(zone) for zone in content]


class GameInfo:
    def __init__(self, content):
        if content:
            self.match_id = content['matchID']
            self.game_number = content['gameNumber']
            self.stage = content['stage']
            self.type = content['type']
            self.variant = content['variant']
            self.match_state = content['matchState']
            self.match_win_condition = content['matchWinCondition']
            self.max_timeout_count = content['maxTimeoutCount']
            self.max_pip_count = content['maxPipCount']
            self.timeout_duration_sec = content['timeoutDurationSec']
            self.super_format = content['superFormat']
            self.mulligan_type = content['mulliganType']
            self.deck_constraint_info = content['deckConstraintInfo']


class Team:
    def __init__(self, content):
        self.id = content['id']
        self.player_ids = content['playerIds']


class Player:

    def __init__(self, content):
        self.life_total = content.get('lifeTotal')
        self.system_seat_number = content['systemSeatNumber']
        self.max_hand_size = content['maxHandSize']
        self.team_id = content['teamId']
        self.time_ids = content['timerIds']
        self.controller_seat_id = content['controllerSeatId']
        self.controller_type = content['controllerType']
        self.pending_message_type = content.get('pendingMessageType')
        self.stating_life_total = content['startingLifeTotal']


class TurnInfo:
    def __init__(self, content):
        if content:
            self.active_player = content.get('activePlayer')
            self.decision_player = content.get('decisionPlayer')


class Zone:
    def __init__(self, content):
        self.zone_id = content.get('zoneId')
        self.type = content.get('type')
        self.visibility = content.get('visibility')
        self.owner_seat_id = content.get('ownerSeatId')
        self.object_instance_ids = content.get('objectInstanceIds')
        self.viewers = content.get('viewers')

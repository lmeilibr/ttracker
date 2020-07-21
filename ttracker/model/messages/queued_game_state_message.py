class QueuedGameStateMessage:

    def __init__(self, content):
        self.system_seat_ids = content['systemSeatIds']
        self.msg_id = content['msgId']
        self.game_state_id = content['gameStateId']
        self.type = content['gameStateMessage']['type']
        self.game_objects = content['gameStateMessage'].get('gameObjects')
        self.annotations = content['gameStateMessage']['annotations']
        self.prev_game_state_id = content['gameStateMessage']['prevGameStateId']
        self.timers = content['gameStateMessage']['timers']
        self.update = content['gameStateMessage']['update']
        self.actions = content['gameStateMessage']['actions']



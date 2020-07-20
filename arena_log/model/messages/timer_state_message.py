class TimerStateMessage:

    def __init__(self, content):
        self.system_seat_ids = content['systemSeatIds']
        self.msgId = content['msgId']
        self.game_state_id = content['gameStateId']
        self.timer_state_message = content['timerStateMessage']

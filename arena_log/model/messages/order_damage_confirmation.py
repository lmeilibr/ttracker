class OrderDamageConfirmation:
    def __init__(self, content):
        self.system_seat_ids = content['systemSeatIds']
        self.msg_id = content['msgId']
        self.game_state_id = content['gameStateId']
        self.result = content['orderDamageConfirmation']['result']
        self.order_damage_type = content['orderDamageConfirmation'][
            'orderDamageType']

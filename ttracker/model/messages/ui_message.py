class UiMessage:

    def __init__(self, content):
        self.system_seat_ids = content['systemSeatIds']
        self.on_generic_event = content['uiMessage'].get('onGenericEvent')
        self.on_hover = content['uiMessage'].get('onHover')



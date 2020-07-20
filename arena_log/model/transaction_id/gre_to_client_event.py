from arena_log.model.messages import get_message_class


class GreToClientEvent:

    def __init__(self, content):
        self.transaction_id = content['transactionId']
        self.timestamp = content['timestamp']
        self.message_list = self.get_messages(
            content['greToClientEvent']['greToClientMessages'])

    def get_messages(self, content):
        message_list = []
        for message in content:
            message_class = get_message_class(message)
            if not message_class:
                print()
            parsed = message_class(message)
            message_list.append(parsed)
        return message_list

    def __repr__(self):
        return '<GreToClientEvent>'

    def __str__(self):
        return f'<{self.screen_name}>'

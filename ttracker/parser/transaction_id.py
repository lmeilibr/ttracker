import json

from ttracker.model.transaction_id import get_message_class


class Transaction:
    def __init__(self):
        self.transaction_list = []

    @staticmethod
    def build_message_key(message):
        do_not_include = ('transactionId', 'requestId', 'timestamp')
        keys = [key for key in message.keys() if key not in do_not_include]
        return '|'.join(keys)

    def add_transaction_line(self, line):
        if line.startswith('{ "transactionId"'):
            message = json.loads(line)
            key = self.build_message_key(message)
            message_class = get_message_class(key)
            self.transaction_list.append(message_class(message))

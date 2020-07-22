from ttracker.parser.thread_logger import ThreadLogger
from ttracker.parser.transaction_id import Transaction


class Parser:

    def __init__(self):
        self.thread_parser = ThreadLogger()
        self.transaction_parser = Transaction()

    def parse_file(self, filepath):
        with open(filepath) as file_handler:
            for line in file_handler:
                self._add_transaction_line(line)
                self._add_thread_line(line)

    def _add_transaction_line(self, line):
        self.transaction_parser.add_transaction_line(line)

    def _add_thread_line(self, line):
        self.thread_parser.add_thread_line(line)

    def get_thread_list(self):
        return self.thread_parser.thread_list

    def get_transaction_list(self):
        return self.transaction_parser.transaction_list

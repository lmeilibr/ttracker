import json

from ttracker.model.thread_logger import get_thread_class

PAYLOAD = 'payload'
THREAD_KEY = 'thread_key'
UNITY_CROSS_THREAD_LOGGER = '[UnityCrossThreadLogger]'
FLOW_SIGN = '=='


class ThreadLogger:
    def __init__(self):
        self.thread_list = []

    @staticmethod
    def parse_thread_line(line):
        item = line[(line.find(FLOW_SIGN) + 3):].strip()
        thread_key = item.split()[0].strip()
        content = ''.join(item.split()[1:]).strip()
        if PAYLOAD in content:
            return {THREAD_KEY: thread_key,
                    PAYLOAD: json.loads(content)[PAYLOAD]}

    def add_thread_line(self, line):
        if UNITY_CROSS_THREAD_LOGGER in line and FLOW_SIGN in line:
            thread_line = self.parse_thread_line(line)
            if thread_line:
                thread_class = get_thread_class(thread_line[THREAD_KEY])
                self.thread_list.append(thread_class(thread_line[PAYLOAD]))

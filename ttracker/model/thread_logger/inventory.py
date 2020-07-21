class Updated:

    def __init__(self, content):
        self.context = content['payload']['context']
        self.updates = content['payload']['updates']

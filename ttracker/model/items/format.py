class Format:

    def __init__(self, content):
        self.name = content['name']
        self.sets = content['sets']
        self.banned_title_ids = content['bannedTitleIds']
        self.suspended_title_ids = content['suspendedTitleIds']
        self.allowed_title_ids = content['allowedTitleIds']
        self.card_count_restriction = content['cardCountRestriction']

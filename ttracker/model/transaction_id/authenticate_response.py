class AuthenticateResponse:

    def __init__(self, content):
        self.transaction_id = content['transactionId']
        self.request_id = content['requestId']

        name = 'authenticateResponse'

        self.client_id = content[name]['clientId']
        self.session_id = content[name]['sessionId']
        self.screen_name = content[name]['screenName']

    def __repr__(self):
        return '<AuthenticateResponse>'

    def __str__(self):
        return f'<{self.screen_name}>'

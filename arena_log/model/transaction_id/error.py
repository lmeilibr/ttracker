class Error:

    def __init__(self, content):
        self.transaction_id = content['transactionId']
        self.error_code = content['error']['errorCode']
        self.error_message = content['error']['errorMessage']

    def __repr__(self):
        return '<Error>'

    def __str__(self):
        return f'<{self.error_code}>'

class Play:
    def __init__(self, content):
        self.grp_id = content['grpId']
        self.instance_id = content['instanceId']
        self.should_stop = content.get('shouldStop')

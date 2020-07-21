class Update:
    def __init__(self, payload):
        self.quest_update = payload['questUpdate']
        self.daily_win_updates = payload['dailyWinUpdates']
        self.weekly_win_updates = payload['weeklyWinUpdates']
        self.battle_pass_update = payload.get('battlePassUpdate')
        self.campaign_graph_updates = payload['campaignGraphUpdates']

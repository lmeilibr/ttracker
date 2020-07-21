class ActivateMana:

    def __init__(self, content):
        self.grpId = content['grpId']
        self.instanceId = content['instanceId']
        self.ability_grp_id = content['abilityGrpId']
        self.mana_payment_options = content.get('manaPaymentOptions')
        self.max_activations = content.get('maxActivations')
        self.is_batchable = content.get('isBatchable')


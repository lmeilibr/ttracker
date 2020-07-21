from ttracker.model.messages.connect_resp import ConnectResp
from ttracker.model.messages.die_roll_results_resp import \
    DieRollResultsResp
from ttracker.model.messages.game_state_message import \
    GameStateMessage
from ttracker.model.messages.choose_starting_player_req import \
    ChooseStartingPlayerReq
from ttracker.model.messages.ui_message import UiMessage
from ttracker.model.messages.set_settings_resp import \
    SetSettingsResp
from ttracker.model.messages.mulligan_req import MulliganReq
from ttracker.model.messages.prompt_req import PromptReq
from ttracker.model.messages.group_req import GroupReq
from ttracker.model.messages.actions_available_req import \
    ActionsAvailableReq
from ttracker.model.messages.get_settings_resp import GetSettingsResp
from ttracker.model.messages.timer_state_message import TimerStateMessage
from ttracker.model.messages.casting_time_options_req import \
    CastingTimeOptionsReq
from ttracker.model.messages.select_targets_req import SelectTargetsReq
from ttracker.model.messages.submit_targets_resp import SubmitTargetsResp
from ttracker.model.messages.select_n_req import SelectNReq
from ttracker.model.messages.optional_action_message import \
    OptionalActionMessage
from ttracker.model.messages.pay_cost_req import PayCostReq
from ttracker.model.messages.declare_blockers_req import DeclareblockerReq
from ttracker.model.messages.submit_blockers_resp import SubmitBlockersResp
from ttracker.model.messages.declare_attackers_req import DeclareAttackersReq
from ttracker.model.messages.submit_attackers_resp import SubmitAttackersResp
from ttracker.model.messages.intermission_req import IntermissionReq
from ttracker.model.messages.submit_deck_req import SubmitDeckReq
from ttracker.model.messages.queued_game_state_message import \
    QueuedGameStateMessage
from ttracker.model.messages.search_req import SearchReq
from ttracker.model.messages.illegal_request import IllegalRequest
from ttracker.model.messages.edictal_message import EdictalMessage
from ttracker.model.messages.timeout_message import TimeoutMessage
from ttracker.model.messages.order_req import OrderReq
from ttracker.model.messages.order_combat_damage_req import OrderCombatDamageReq
from ttracker.model.messages.order_damage_confirmation import OrderDamageConfirmation
from ttracker.model.messages.assign_damage_req import AssignDamageReq
from ttracker.model.messages.assign_damage_confirmation import AssignDamageConfirmation

MESSAGE_FACTORY = {
    'ConnectResp': ConnectResp,
    'DieRollResultsResp': DieRollResultsResp,
    'GameStateMessage': GameStateMessage,
    'ChooseStartingPlayerReq': ChooseStartingPlayerReq,
    'UIMessage': UiMessage,
    'SetSettingsResp': SetSettingsResp,
    'MulliganReq': MulliganReq,
    'PromptReq': PromptReq,
    'GroupReq': GroupReq,
    'ActionsAvailableReq': ActionsAvailableReq,
    'GetSettingsResp': GetSettingsResp,
    'TimerStateMessage': TimerStateMessage,
    'CastingTimeOptionsReq': CastingTimeOptionsReq,
    'SelectTargetsReq': SelectTargetsReq,
    'SubmitTargetsResp': SubmitTargetsResp,
    'SelectNReq': SelectNReq,
    'OptionalActionMessage': OptionalActionMessage,
    'PayCostsReq': PayCostReq,
    'DeclareBlockersReq': DeclareblockerReq,
    'SubmitBlockersResp': SubmitBlockersResp,
    'DeclareAttackersReq': DeclareAttackersReq,
    'SubmitAttackersResp': SubmitAttackersResp,
    'IntermissionReq': IntermissionReq,
    'SubmitDeckReq': SubmitDeckReq,
    'QueuedGameStateMessage': QueuedGameStateMessage,
    'SearchReq': SearchReq,
    'IllegalRequest': IllegalRequest,
    'EdictalMessage': EdictalMessage,
    'TimeoutMessage': TimeoutMessage,
    'OrderReq': OrderReq,
    'OrderCombatDamageReq': OrderCombatDamageReq,
    'OrderDamageConfirmation': OrderDamageConfirmation,
    'AssignDamageReq': AssignDamageReq,
    'AssignDamageConfirmation': AssignDamageConfirmation,
}


def get_message_class(option):
    message_type = option['type'].split('_')[-1]
    try:
        return MESSAGE_FACTORY[message_type]
    except KeyError as err:
        print(err)
        raise KeyError

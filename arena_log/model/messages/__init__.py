from arena_log.model.messages.connect_resp import ConnectResp
from arena_log.model.messages.die_roll_results_resp import \
    DieRollResultsResp
from arena_log.model.messages.game_state_message import \
    GameStateMessage
from arena_log.model.messages.choose_starting_player_req import \
    ChooseStartingPlayerReq
from arena_log.model.messages.ui_message import UiMessage
from arena_log.model.messages.set_settings_resp import \
    SetSettingsResp
from arena_log.model.messages.mulligan_req import MulliganReq
from arena_log.model.messages.prompt_req import PromptReq
from arena_log.model.messages.group_req import GroupReq
from arena_log.model.messages.actions_available_req import \
    ActionsAvailableReq
from arena_log.model.messages.get_settings_resp import GetSettingsResp
from arena_log.model.messages.timer_state_message import TimerStateMessage
from arena_log.model.messages.casting_time_options_req import \
    CastingTimeOptionsReq
from arena_log.model.messages.select_targets_req import SelectTargetsReq
from arena_log.model.messages.submit_targets_resp import SubmitTargetsResp
from arena_log.model.messages.select_n_req import SelectNReq
from arena_log.model.messages.optional_action_message import \
    OptionalActionMessage
from arena_log.model.messages.pay_cost_req import PayCostReq
from arena_log.model.messages.declare_blockers_req import DeclareblockerReq
from arena_log.model.messages.submit_blockers_resp import SubmitBlockersResp
from arena_log.model.messages.declare_attackers_req import DeclareAttackersReq
from arena_log.model.messages.submit_attackers_resp import SubmitAttackersResp
from arena_log.model.messages.intermission_req import IntermissionReq
from arena_log.model.messages.submit_deck_req import SubmitDeckReq
from arena_log.model.messages.queued_game_state_message import \
    QueuedGameStateMessage
from arena_log.model.messages.search_req import SearchReq
from arena_log.model.messages.illegal_request import IllegalRequest
from arena_log.model.messages.edictal_message import EdictalMessage
from arena_log.model.messages.timeout_message import TimeoutMessage
from arena_log.model.messages.order_req import OrderReq
from arena_log.model.messages.order_combat_damage_req import OrderCombatDamageReq
from arena_log.model.messages.order_damage_confirmation import OrderDamageConfirmation
from arena_log.model.messages.assign_damage_req import AssignDamageReq
from arena_log.model.messages.assign_damage_confirmation import AssignDamageConfirmation

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

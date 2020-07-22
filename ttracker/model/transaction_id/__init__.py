from ttracker.model.transaction_id.authenticate_response import \
    AuthenticateResponse
from ttracker.model.transaction_id.error import Error
from ttracker.model.transaction_id.gre_to_client_event import GreToClientEvent
from ttracker.model.transaction_id.match_game_room_state_changed_event import \
    MatchGameRoomStateChangedEvent
from ttracker.model.transaction_id.null_message import NullMessage

AUTHENTICATE_RESPONSE = 'authenticateResponse'
ERROR = 'error'
GRE_TO_CLIENT_EVENT = 'greToClientEvent'
MATCH_GAME_ROOM_STATE_CHANGED_EVENT = 'matchGameRoomStateChangedEvent'

MESSAGE_FACTORY = {
    AUTHENTICATE_RESPONSE: AuthenticateResponse,
    ERROR: Error,
    GRE_TO_CLIENT_EVENT: GreToClientEvent,
    MATCH_GAME_ROOM_STATE_CHANGED_EVENT: MatchGameRoomStateChangedEvent,
    'Default': NullMessage
}


def get_message_class(message_key):
    try:
        return MESSAGE_FACTORY[message_key]
    except KeyError as err:
        print(err)
        raise KeyError

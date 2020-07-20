from arena_log.scryfall.client import MtgClient
from arena_log.settings import ARENA_FOLDER, SCRYFALL_TIMER
import time


def fetch_card_list(card_list):
    client = MtgClient(ARENA_FOLDER)
    for card_id in card_list:
        client.get_by_arena_id(card_id)
        time.sleep(SCRYFALL_TIMER)

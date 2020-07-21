from ttracker.etl.fetch_card import fetch_card_list
from ttracker.parser.player_inventory.player_cards import parser


def test_fetch_card_list():
    with open("resources/samples/player_cards.json") as content:
        card_list = parser(content)
        fetch_card_list(card_list)

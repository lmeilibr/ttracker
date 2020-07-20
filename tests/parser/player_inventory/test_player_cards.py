from arena_log.parser.player_inventory.player_cards import parser
import json


def test_parser():
    with open("resources/samples/player_cards.json") as content:
        data = parser(content)

    assert isinstance(data, dict)

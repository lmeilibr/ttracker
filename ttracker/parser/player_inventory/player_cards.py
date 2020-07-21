import json


def parser(content):
    content = json.load(content)
    return content['payload']

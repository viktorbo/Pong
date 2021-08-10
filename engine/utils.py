import json


def read_json(path):
    with open(file=path, mode='r', encoding='utf-8') as file:
        content = json.load(file)
    return content

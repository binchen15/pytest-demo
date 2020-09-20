import json


class MysteryError(Exception):
    pass


def add(a, b):
    if a == 99:
        raise MysteryError()
    return a + b


def subtract(a, b):
    return a - b


def read_json(file_path):
    with open(file_path, "r") as f:
        return json.load(f)

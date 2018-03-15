import json


class JSONReader:
    def __init__(self, source_file):
        self.source_file = source_file

    @staticmethod
    def get_items():
        items = open('data/train.json')
        return json.load(items)

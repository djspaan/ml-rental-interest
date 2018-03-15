import json


class JSONReader:
    def __init__(self, source_file):
        self.source_file = source_file

    def get_items(self):
        items = open(self.source_file)
        return json.load(items)

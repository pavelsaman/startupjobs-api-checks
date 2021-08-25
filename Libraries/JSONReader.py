import json


class JSONReader:

    @staticmethod
    def read_json(filename):
        data = None
        with open(filename, 'r') as json_file:
            data = json.load(json_file)
        return data

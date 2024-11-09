import json

class JsonUtil:
    @staticmethod
    def read_json_from_file(file_name):
        try:
            with open(file_name, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            raise Exception(f"File not found: {file_name}")

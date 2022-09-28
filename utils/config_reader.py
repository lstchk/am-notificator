import json


class ConfigReader:
    def __init__(self, file_name):
        self.file_name = file_name

    def read_config(self) -> dict:
        file = open(self.file_name)

        conf = json.load(file)
        return conf


config_reader = ConfigReader("resources/config.json")
config = config_reader.read_config()

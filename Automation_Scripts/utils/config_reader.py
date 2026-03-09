import json
def read_config():

    with open("Automation_Scripts/config/config.json") as file:
        config = json.load(file)

    return config
import json

from files_helper import create_if_doesnt_exists

MOVIES_LINKS_FILE_NAME = 'movies.txt'
CHANNELS_LINKS_FILE_NAME = 'channels.txt'
CONFIG_FILE_NAME = 'config.json'
YT_API_KEY: str


def load():
    create_if_doesnt_exists(CONFIG_FILE_NAME)
    with open(CONFIG_FILE_NAME, 'r') as f:
        text = f.read()
        data = json.loads(text)
        global YT_API_KEY
        YT_API_KEY = data['YT_API_KEY']

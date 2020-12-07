from typing import List

import config
from files_helper import create_if_doesnt_exists, load_links

MOVIES_LINKS_LIST: List[str]
CHANNELS_LINKS_LIST: List[str]


def load() -> None:
    create_if_doesnt_exists(config.MOVIES_LINKS_FILE_NAME)
    create_if_doesnt_exists(config.CHANNELS_LINKS_FILE_NAME)
    global MOVIES_LINKS_LIST
    global CHANNELS_LINKS_LIST
    MOVIES_LINKS_LIST = list(load_links(config.MOVIES_LINKS_FILE_NAME))
    CHANNELS_LINKS_LIST = list(load_links(config.CHANNELS_LINKS_FILE_NAME))

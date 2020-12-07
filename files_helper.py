import os
from typing import Iterator

import validators


def create_if_doesnt_exists(filename: str) -> None:
    if not os.path.isfile(filename):
        open(filename, 'a').close()


def load_links(filename: str) -> Iterator[str]:
    with open(filename, 'r') as f:
        lines = f.readlines()
        lines = map(lambda l: l.strip(), lines)
        lines = filter(lambda l: validators.url(l), lines)
        return lines

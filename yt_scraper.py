from typing import Optional

import requests

from json_helper import get_json_data
from yt_chanel_data import YTChannelData
from yt_movie_data import YTMovieData


def get_movie_data(link: str) -> Optional[YTMovieData]:
    BEGINNING_OF_JSON = "ytInitialData = "

    response = requests.get(link)
    try:
        response.raise_for_status()
        text = get_json_data(response.text, BEGINNING_OF_JSON)
        movie = YTMovieData()
        movie.parse(text)
        return movie
    except Exception:
        return None


def get_channel_data(link: str) -> Optional[YTChannelData]:
    BEGINNING_OF_JSON = 'ytInitialData = '

    response = requests.get(link)
    try:
        response.raise_for_status()
        text = get_json_data(response.text, BEGINNING_OF_JSON)
        channel = YTChannelData()
        channel.parse(text)
        return channel
    except Exception:
        return None

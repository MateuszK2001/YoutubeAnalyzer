from typing import Optional, List, Iterator

import requests
import urllib.parse as urlparse
from urllib.parse import parse_qs

import config
from yt_chanel_data import YTChannelData
from yt_movie_data import YTMovieData


def link_to_video_id(url: str) -> Optional[str]:
    parsed = urlparse.urlparse(url)
    if "youtube.com/watch" in url:
        params = parse_qs(parsed.query)
        if 'v' not in params:
            return None
        return params['v'][0]
    elif "youtu.be" in url:
        return parsed.path.replace('/', '')
    else:
        return None


def get_movies_data(ids: List[str]) -> Iterator[YTMovieData]:
    URL = 'https://www.googleapis.com/youtube/v3/videos'
    args = {
        'part': 'statistics,snippet',
        'id': ','.join(ids),
        'key': config.YT_API_KEY
    }
    response = requests.get(URL, args)
    json = response.json()

    def to_yt_movie_data(item) -> YTMovieData:
        res = YTMovieData()
        res.title = item['snippet']['title']
        res.views = int(item['statistics']['viewCount'])
        res.likes = int(item['statistics']['likeCount'])
        res.dislikes = int(item['statistics']['dislikeCount'])
        res.channel_id = item['snippet']['channelId']
        res.channel_name = item['snippet']['channelTitle']
        res.description = item['snippet']['description']
        return res

    return map(to_yt_movie_data, json['items'])


def get_channel_data(ids: List[str]) -> Iterator[YTChannelData]:
    URL = 'https://www.googleapis.com/youtube/v3/channels'
    args = {
        'part': 'statistics,snippet',
        'id': ','.join(ids),
        'key': config.YT_API_KEY
    }
    response = requests.get(URL, args)
    json = response.json()

    def to_yt_channel_data(item) -> YTChannelData:
        res = YTChannelData()
        res.id = item['id']
        res.name = item['snippet']['title']
        res.description = item['snippet']['description']
        res.subscriptions = item['statistics']['subscriberCount']
        res.url = f"https://www.youtube.com/channel/{res.id}"
        return res

    return map(to_yt_channel_data, json['items'])

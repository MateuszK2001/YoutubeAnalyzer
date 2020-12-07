import json
import re
from decimal import Decimal
from json_helper import dict_eval


class YTMovieData:
    title: str
    likes: int
    dislikes: int
    views: int
    description: str
    channel_id: str
    channel_name: str

    def __init__(self, title='', likes=0, dislikes=0, views=0, description='', channel_id='',
                 channel_name='') -> None:
        self.title = title
        self.likes = likes
        self.dislikes = dislikes
        self.views = views
        self.description = description
        self.channel_id = channel_id
        self.channel_name = channel_name

    def __str__(self):
        return \
            f"""Tytuł: {self.title}
Liki: {self.likes}
Disliki: {self.dislikes}
Wyświetleń: {self.views}
Id kanału: {self.channel_id}
Nazwa kanału: {self.channel_name}"""

    # description lepiej nie wyswietlac bo bywa bardzo dlugie

    def __text_to_num(text: str) -> int:
        m = 1
        if "mln" in text:
            m = 1000000
        elif "tys" in text:
            m = 1000
        number_str = re.sub(r"[^(0-9|,)]", "", text).replace(",", ".")
        return int(Decimal(number_str) * m)

    def parse(self, text: str):
        data = json.loads(text)

        self.title = dict_eval(data,
                               'contents/twoColumnWatchNextResults/results/results/contents/0'
                               '/videoPrimaryInfoRenderer/title/runs/0/text')

        views_text = dict_eval(data,
                               'contents/twoColumnWatchNextResults/results/results/contents/0/videoPrimaryInfoRenderer'
                               '/viewCount/videoViewCountRenderer/viewCount/simpleText')
        self.views = YTMovieData.__text_to_num(views_text)

        likes_text = dict_eval(data,
                               'contents/twoColumnWatchNextResults/results/results/contents/0/videoPrimaryInfoRenderer'
                               '/videoActions/menuRenderer/topLevelButtons/0/toggleButtonRenderer/defaultText'
                               '/accessibility/accessibilityData/label')
        self.likes = YTMovieData.__text_to_num(likes_text)

        dislikes_text = dict_eval(data,
                                  'contents/twoColumnWatchNextResults/results/results/contents/0'
                                  '/videoPrimaryInfoRenderer/videoActions/menuRenderer/topLevelButtons/1'
                                  '/toggleButtonRenderer/defaultText/accessibility/accessibilityData/label')
        self.dislikes = YTMovieData.__text_to_num(dislikes_text)

        self.channel_id = dict_eval(data,
                                    'contents/twoColumnWatchNextResults/results/results/contents/1'
                                    '/videoSecondaryInfoRenderer/owner/videoOwnerRenderer/title/runs/0'
                                    '/navigationEndpoint/browseEndpoint/browseId')

        self.channel_name = dict_eval(data,
                                      'contents/twoColumnWatchNextResults/results/results/contents/1'
                                      '/videoSecondaryInfoRenderer/owner/videoOwnerRenderer/title/runs/0/text')

        # Moze nie byc opisu wogole i wtedy nie zostanie bedzie blad
        try:
            description_array = dict_eval(data,
                                          'contents/twoColumnWatchNextResults/results/results/contents/1'
                                          '/videoSecondaryInfoRenderer/description/runs')
            description_array = map(lambda l: l['text'], description_array)
            self.description = "".join(description_array)
        except Exception:
            pass

import json
import re
from decimal import Decimal

from json_helper import dict_eval


class YTChannelData:
    id: str
    name: str
    description: str
    subscriptions: int
    url: str

    def __str__(self):
        return \
            f"""Nazwa: {self.name}
Id: {self.id}
Opis: {self.description}
Liczba subskrypcji: {self.subscriptions}
Url: {self.url}"""

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

        self.id = dict_eval(data,
                            'metadata/channelMetadataRenderer/externalId')

        self.name = dict_eval(data,
                              'metadata/channelMetadataRenderer/title')

        self.description = dict_eval(data,
                                     'metadata/channelMetadataRenderer/description')

        self.url = dict_eval(data,
                             'metadata/channelMetadataRenderer/channelUrl')

        subscriptions_text = dict_eval(data,
                                       'header/c4TabbedHeaderRenderer/subscriberCountText/simpleText')
        self.subscriptions = YTChannelData.__text_to_num(subscriptions_text)

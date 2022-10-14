import json
import requests
from json import loads
from utils import Utils


class YandexMapApi:
    def __init__(self, api_key: str):
        self.__url__ = "https://search-maps.yandex.ru/v1/"
        self.api_key = api_key

    def get_by_index(self, index: int) -> str:
        r = requests.get(self.__url__, params={"text": index, "type": "biz", "lang": "ru_RU",
                                               "results": 1, "apikey": self.api_key})
        return r.text

    def get_by_range(self, center=(0, 0), spn=None) -> str:
        center = (Utils.dms_to_dd(center[0]), Utils.dms_to_dd(center[1]))
        spn = (1 / 111.3) * int(spn)
        spn = ((center[0] + (spn)) - (center[0] - (spn)), (center[1] + (spn)) - (center[1] - (spn)))
        r = requests.get(self.__url__, params={"apikey": self.api_key, "lang": "ru_RU",
                                               "ll": f"{center[1]},{center[0]}", "results": 500,
                                               "spn": f"{round(spn[1], 6)},{round(spn[0], 6)}", "text": "Отделение почтовой связи"})
        return r.text
import json
import os
from flask import Flask, render_template, request

import config
from utils import Utils
from yandex_map_api import YandexMapApi

app = Flask(__name__)
app.config.from_object(config.DevelopmentConfig)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Получение данных с формы (ИЛЯ!!!)
        index = request.form.get('index')
        geo_coords_longitude = request.form.get('geo_coords_longitude')  # Longitude - долгота
        geo_coords_latitude = request.form.get('geo_coords_latitude')  # Latitude - широта
        geo_coords = (geo_coords_longitude, geo_coords_latitude)  # Объединение координат в dict
        geo_range = request.form.get('geo_range').replace(",", ".")
        if geo_range and Utils.isfloat(geo_range):
            geo_range = float(geo_range)
        else:
            geo_range = 0
        data_from_api = get_data_from_api(index=index, geo_coords=geo_coords, geo_range=geo_range)
        data = parse_data_from_api(data_from_api)
        return render_template('index.html', data_from_server=data, data={"index": index,
                                                                          "geo_coords_longitude": geo_coords_longitude,
                                                                          "geo_coords_latitude": geo_coords_latitude,
                                                                          "geo_range": int(geo_range*1000)})
    return render_template('index.html')


# Принимает в себя до 3-х параметров: int index, dict geo_cords, float geo_range
def get_data_from_api(**data) -> str:
    api = YandexMapApi("a1910da4-923c-41a1-b952-e3de90a6859a")
    if data.get("index"):
        data_from_api = api.get_by_index(data.get("index"))
    else:
        data_from_api = api.get_by_range(center=data.get("geo_coords"), spn=data.get("geo_range"))
    return data_from_api


def parse_data_from_api(data_from_api) -> dict:
    data = json.loads(data_from_api).get("features")
    data_dict = []
    for item in data:
        name = item["properties"]["CompanyMetaData"]["name"]
        address = item["properties"]["CompanyMetaData"]["address"]
        index = name.replace("Отделение почтовой связи №", '')
        la_coord = item["geometry"]["coordinates"][0]  # Широта
        lo_coord = item["geometry"]["coordinates"][1]  # Долгота
        coords = (lo_coord, la_coord)
        data_dict.append([name, address, index, coords])
    return data_dict


if __name__ == "__main__":
    app.run()

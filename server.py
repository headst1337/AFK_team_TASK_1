import json
import os
from flask import Flask, render_template, request
from yandex_map_api import YandexMapApi

os.environ['FLASK_CONFIG'] = 'config.DevelopmentConfig'
os.environ['YANDEX_MAP_API'] = 'a1910da4-923c-41a1-b952-e3de90a6859a'

app = Flask(__name__)
app.config.from_object(os.environ['FLASK_CONFIG'])

@app.route('/', methods=['GET', 'POST'])
def index() -> None:
    if request.method == 'POST':
        # Получение данных с формы
        index = request.form.get('index')
        geo_coords_longitude = request.form.get('geo_coords_longitude') # Longitude - долгота
        geo_coords_latitude = request.form.get('geo_coords_latitude')   # Latitude - широта
        geo_coords = (geo_coords_longitude, geo_coords_latitude)        # Объединение координат в dict
        geo_range = request.form.get('geo_range')

        data_from_api = get_data_from_api(index=index, geo_coords=geo_coords, geo_range=geo_range)
        data = parse_data_from_api(data_from_api)

        return render_template('index.html', data_from_server=data)
    return render_template('index.html')

def get_data_from_api(**data) -> str:
    api = YandexMapApi(os.environ['YANDEX_MAP_API'])
    if data.get("index"):
        data_from_api = api.get_by_index(data.get("index"))
    else:
        data_from_api = api.get_by_range(center=data.get("geo_coords"), spn=data.get("geo_range"))
    return data_from_api

# def parse_data_from_api(data_from_api) -> dict:
#     search_result_count = data_from_api.count("CompanyMetaData")
#     data_json = json.loads(data_from_api)
#     print(data_from_api)
#     data_dict = {}
#     post_count = 0
#     for i in range(search_result_count):
#         name = data_json["features"][i]["properties"]["CompanyMetaData"]["name"]
#         if name.find("Отделение почтовой связи") != -1:
#             address = data_json["features"][i]["properties"]["CompanyMetaData"]["address"]
#             index = name.replace("Отделение почтовой связи №", '')
#             la_coord = data_json["features"][i]["geometry"]["coordinates"][0] # Широта
#             lo_coord = data_json["features"][i]["geometry"]["coordinates"][1] # Долгота
#             coords = (lo_coord, la_coord)
#             post_count += 1
#             data_dict[f"{post_count}"] = name, address, index, coords
#         else: continue
#     return data_dict

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
    
# How to run:

**Install requirements via requirements.txt**
```sh
pip install - r requirements.txt
```
**Set env variables**
```sh
export FLASK_CONFIG="config.DevelopmentConfig"
export YANDEX_MAP_API=<api_key>
```
> Note: `"config.ProductionConfig"` for production mode

**Run**
```sh
python server.py
```



## For Windows


> Use setx for create environment variable

for example:
```sh
setx FLASK_CONFIG config.DevelopmentConfig
```


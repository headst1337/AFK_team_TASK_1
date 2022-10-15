## How to run:

**Install requirements via requirements.txt**
```sh
pip install -r requirements.txt
```
**Set env variables**
```sh
export FLASK_CONFIG="config.DevelopmentConfig"
export YANDEX_MAP_API="a1910da4-923c-41a1-b952-e3de90a6859a"
```
> Note: `"config.ProductionConfig"` for production mode

**Run**
```sh
python server.py
```



### For Windows


> Use setx for create environment variable

for example:
```sh
setx FLASK_CONFIG config.DevelopmentConfig
```


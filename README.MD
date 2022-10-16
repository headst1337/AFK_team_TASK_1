## How to run:
**Install python**
```sh
sudo apt update
sudo apt upgrade
sudo apt install python3-pip
```
**Install requirements via requirements.txt**
```sh
pip install -r requirements.txt
```
**Set env variables**
```sh
export FLASK_CONFIG="config.DevelopmentConfig"
export YANDEX_MAP_API="df372d7a-a7fd-49e1-9ae9-235bda72ddfd"
```
> Note: `"config.ProductionConfig"` for production mode

### For Windows

> Use setx for create environment variable

```sh
setx FLASK_CONFIG config.DevelopmentConfig
setx YANDEX_MAP_API df372d7a-a7fd-49e1-9ae9-235bda72ddfd
python server.py
```


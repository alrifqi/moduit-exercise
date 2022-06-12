import os
import yaml

from yaml.loader import SafeLoader
from pydantic import BaseSettings

yaml_settings = dict()

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, "config.yaml")) as f:
    yaml_settings.update(yaml.load(f, Loader=yaml.FullLoader))


class Settings(BaseSettings):
    MODUIT_ENDPOINT = yaml_settings['MODUIT_ENDPOINT']
    BASE_URL = yaml_settings['BASE_URL']


settings = Settings()

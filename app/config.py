from functools import lru_cache

from pydantic import BaseSettings


class Config(BaseSettings):
    # App setting
    app_name: str = "scroll-shelter"

    # Db Settings
    db_path: str

    # Google OAuth Settings
    client_id: str
    client_secret: str

    # HTTP server settings
    secret: str

    # Google Picker API
    gpicker_key: str

    class Config:
        env_file = ".env"


@lru_cache()
def get_config():
    return Config()

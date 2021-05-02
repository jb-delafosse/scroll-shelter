from app.config import get_config
from fastapi import FastAPI

config = get_config()

SECRET: str = config.secret
app = FastAPI()

import motor.motor_asyncio
from app.config import get_config

config = get_config()


DATABASE_URL: str
DATABASE_URL = config.db_path
CLIENT = motor.motor_asyncio.AsyncIOMotorClient(
    DATABASE_URL, uuidRepresentation="standard"
)

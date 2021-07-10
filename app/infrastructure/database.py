import motor.motor_asyncio
from app.adapter.folder_db.factories import MongoFolderDbFactory
from app.config import get_config
from app.interface import folder_db

config = get_config()


DATABASE_URL: str
DATABASE_URL = config.db_path
CLIENT = motor.motor_asyncio.AsyncIOMotorClient(
    DATABASE_URL, uuidRepresentation="standard"
)
DATABASE = CLIENT["scroll-shelter"]
folder_db.FOLDER_DB_FACTORY = MongoFolderDbFactory(DATABASE)

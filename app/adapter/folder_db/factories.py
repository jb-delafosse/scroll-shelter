from app.adapter.folder_db.implems import MongoFolderDb
from app.common.type import UserId
from motor.motor_asyncio import AsyncIOMotorDatabase


class MongoFolderDbFactory:
    def __init__(
        self,
        db: AsyncIOMotorDatabase,
    ):
        self._db = db
        self.folder_collection = db.folders

    def __call__(self) -> MongoFolderDb:
        return MongoFolderDb(collection=self.folder_collection)

from app.interface.folder_db import (
    FolderInsertQuery,
    FolderInsertResponse,
    IFolderDB,
)
from motor.motor_asyncio import AsyncIOMotorCollection


class MongoFolderDb(IFolderDB):
    def __init__(self, collection: AsyncIOMotorCollection) -> None:
        self.coll = collection

    async def insert_folder(
        self, query: FolderInsertQuery
    ) -> FolderInsertResponse:
        result = await self.coll.insert_one(query.dict())
        return FolderInsertResponse(
            provider_name=query.provider_name,
            provider_id=query.provider_id,
            id=result.inserted_id,
        )

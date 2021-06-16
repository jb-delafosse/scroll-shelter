from typing import NewType

from bson.objectid import ObjectId as BsonObjectId
from pydantic import UUID4


class PydanticObjectId(BsonObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not isinstance(v, BsonObjectId):
            raise TypeError("ObjectId required")
        return v


UserId = NewType("UserId", UUID4)
FolderId = NewType("FolderId", PydanticObjectId)

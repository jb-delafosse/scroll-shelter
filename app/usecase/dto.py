from typing import List

from datetime import datetime

from app.common.type import FolderId
from fastapi_users import models
from pydantic import BaseModel
from pydantic.dataclasses import dataclass


@dataclass(frozen=True)
class FetchFileRequest:
    file_id: str


@dataclass(frozen=True)
class File:
    file_id: str
    created_at: datetime
    updated_at: datetime
    url: str
    folders: List[str]
    size: int
    name: str
    file_extension: str


class User(models.BaseUser, models.BaseOAuthAccountMixin):
    pass


class UserCreate(models.BaseUserCreate):
    pass


class UserUpdate(User, models.BaseUserUpdate):
    pass


class BaseUserDB(models.BaseUserDB):
    pass


@dataclass(frozen=True)
class FolderCreate:
    provider_id: str
    provider_name: str


class Folder(BaseModel):
    provider_id: str
    provider_name: str
    id: FolderId

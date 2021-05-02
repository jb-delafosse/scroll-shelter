from typing import List

from dataclasses import dataclass
from datetime import datetime

from fastapi_users import models


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

from typing import List

from dataclasses import dataclass
from datetime import datetime


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

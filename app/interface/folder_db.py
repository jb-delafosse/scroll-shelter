from typing import Callable, Optional

from abc import ABC, abstractmethod

from app.common.type import FolderId, UserId
from pydantic import UUID4, BaseModel
from pydantic.dataclasses import dataclass


@dataclass(frozen=True)
class FolderInsertQuery(BaseModel):
    provider_id: str
    provider_name: str
    user_id: UUID4


@dataclass(frozen=True)
class FolderInsertResponse:
    provider_id: str
    provider_name: str
    id: FolderId


class IFolderDB(ABC):
    """
    Interface that defines a way to store Folders
    """

    @abstractmethod
    async def insert_folder(
        self, query: FolderInsertQuery
    ) -> FolderInsertResponse:
        """
        Insert Folder in DB

        Args:
            query: a FolderCreateQuery

        Returns:
            None
        """
        pass


FolderDBFactory = Callable[[], IFolderDB]
FOLDER_DB_FACTORY: FolderDBFactory

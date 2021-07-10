import logging

from app.common.type import FolderId, UserId
from app.interface import folder_db
from app.interface.folder_db import FolderInsertQuery
from app.usecase.dto import Folder, FolderCreate


class FolderUsecase:
    """
    Manage all the interactions that can be done with a folder.
    """

    def __init__(self, user_id: UserId) -> None:
        self.user_id = user_id
        self._folder_db = folder_db.FOLDER_DB_FACTORY()

    async def save_folder(self, request: FolderCreate) -> Folder:
        """
        Fetch a file from the file_provider given its id

        Args:
            request: the request to create the folder

        Returns:
            a File obtained from the file provider
        """
        query = FolderInsertQuery(
            provider_id=request.provider_id,
            provider_name=request.provider_name,
            user_id=self.user_id,
        )
        response = await self._folder_db.insert_folder(query=query)
        return Folder(
            provider_id=response.provider_id,
            provider_name=response.provider_name,
            id=response.id,
        )

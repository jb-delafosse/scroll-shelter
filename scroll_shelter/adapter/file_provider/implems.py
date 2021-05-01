from typing import List

from dataclasses import dataclass
from datetime import datetime

from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from scroll_shelter.interface.file_provider import FileRequest, IFileProvider
from scroll_shelter.usecase.dto import File


@dataclass(frozen=True)
class GdriveFileResponse:
    id: str
    createdTime: datetime
    modifiedTime: datetime
    webViewLink: str
    parents: List[str]
    size: str
    name: str
    fileExtension: str


SCROLL_FIELDS = ", ".join(GdriveFileResponse.__annotations__.keys())


class GDriveFileProvider(IFileProvider):
    def __init__(self, credentials: Credentials) -> None:
        """
        Instantiate a GDriveFileProvider (mostly an API Client)

        Args:
            credentials:
        """
        self.drive_service = build("drive", "v3", credentials=credentials)

    def get_file(self, request: FileRequest) -> File:
        """
        Get file info from Gdrive

        Args:
            request: a FileRequest

        Returns:
            a File
        """
        drive_request = self.drive_service.files().get(
            fileId=request.file_id, fields=SCROLL_FIELDS
        )
        response = GdriveFileResponse(**drive_request.execute())
        return File(
            file_id=response.id,
            created_at=response.createdTime,
            updated_at=response.modifiedTime,
            url=response.webViewLink,
            folders=response.parents,
            size=int(response.size),
            name=response.name,
            file_extension=response.fileExtension,
        )

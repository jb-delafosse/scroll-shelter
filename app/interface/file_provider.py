from typing import Callable

from abc import ABC, abstractmethod
from dataclasses import dataclass

from app.usecase.dto import File


@dataclass(frozen=True)
class FileRequest:
    file_id: str


class IFileProvider(ABC):
    """
    Interface that defines a File provider such as GDrive
    """

    @abstractmethod
    def get_file(self, request: FileRequest) -> File:
        """
        Get file info from the file provider

        Args:
            request: a FileRequest

        Returns:
            a File
        """
        pass


ScrollProviderFactory = Callable[[], IFileProvider]
SCROLL_PROVIDER_FACTORY: ScrollProviderFactory

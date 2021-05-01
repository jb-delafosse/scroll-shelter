from typing import Callable

from unittest.mock import MagicMock

import pytest
from scroll_shelter.interface import file_provider
from scroll_shelter.usecase.dto import File


@pytest.fixture(scope="function")
def mock_file_provider() -> Callable[[File], file_provider.IFileProvider]:
    """
    Fixture that

    Returns:

    """

    def mock_provider_factory():
        provider = MagicMock(spec=file_provider.IFileProvider)
        file_provider.SCROLL_PROVIDER_FACTORY = MagicMock(return_value=provider)
        return provider

    return mock_provider_factory

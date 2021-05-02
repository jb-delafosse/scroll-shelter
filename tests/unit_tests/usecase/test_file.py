from datetime import datetime
from unittest.mock import MagicMock

from app.usecase.dto import FetchFileRequest, File
from app.usecase.file import fetch_file


def test_fetch_file(mock_file_provider):
    # Given :
    # A Mocked file provider that will return a file
    expected_file = File(
        file_id="123",
        created_at=datetime.now(),
        updated_at=datetime.now(),
        url="https://google.com",
        folders=["1234"],
        size=1234,
        name="my-note.pdf",
        file_extension="pdf",
    )
    file_provider = mock_file_provider()
    file_provider.get_file = MagicMock(return_value=expected_file)
    request = FetchFileRequest(file_id="123")

    # When:
    file = fetch_file(request)

    # Then:
    assert file == expected_file

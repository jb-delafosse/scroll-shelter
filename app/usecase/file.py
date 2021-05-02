from app.interface import file_provider
from app.interface.file_provider import FileRequest
from app.usecase.dto import FetchFileRequest, File


def fetch_file(fetch_scroll_request: FetchFileRequest) -> File:
    """
    Fetch a file from the file_provider given its id

    Args:
        fetch_scroll_request: the request made to the usecase

    Returns:
        a File obtained from the file provider
    """
    _file_provider = file_provider.SCROLL_PROVIDER_FACTORY()

    file_get = FileRequest(file_id=fetch_scroll_request.file_id)
    return _file_provider.get_file(file_get)

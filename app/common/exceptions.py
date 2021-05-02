# This module contains all business Exceptions.
#
# This Exception must correspond to a business case and not
# have technicals information.
from typing import Optional


class ScrollShelterError(Exception):
    """Base class for all business errors in scroll-shelter.
    Args:
        code: An unique indentifier for this kind of error.
    """

    def __init__(self, code: str, message: Optional[str] = None) -> None:
        self.code = code
        super().__init__(message)


class InvalidFileProviderFactoryError(ScrollShelterError):
    def __init__(self, message: Optional[str] = None) -> None:
        super().__init__(
            code="invalid-scroll-provider-factory", message=message
        )

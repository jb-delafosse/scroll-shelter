from __future__ import annotations

from typing import cast

import logging

from app.adapter.file_provider.implems import GDriveFileProvider
from app.common.exceptions import InvalidFileProviderFactoryError
from google.auth.exceptions import RefreshError
from google.oauth2.credentials import Credentials
from google_auth_httplib2 import Request


class GDriveFileProviderFactory:
    _credentials: Credentials = None

    def __new__(cls, credentials: Credentials) -> GDriveFileProviderFactory:
        if not credentials.valid:
            if (
                credentials
                and credentials.expired
                and credentials.refresh_token
            ):
                try:
                    credentials.refresh(Request())
                except RefreshError as e:
                    logging.error(e, exc_info=True)
                    raise InvalidFileProviderFactoryError(
                        "Could not get a valid token."
                    )
            else:
                raise InvalidFileProviderFactoryError(
                    "No refresh token available to get new token."
                )
        cls._credentials = credentials
        return cast(GDriveFileProviderFactory, super().__new__(cls))

    @classmethod
    def __call__(cls) -> GDriveFileProvider:
        return GDriveFileProvider(credentials=cls._credentials)

from scroll_shelter.infrastructure.fastapi_user import (
    AUTH_ROUTER,
    GOOGLE_OAUTH_ROUTER,
    REGISTER_ROUTER,
    RESET_PASSWORD_ROUTER,
    USERS_ROUTER,
    VERIFY_ROUTER,
)
from scroll_shelter.infrastructure.web_app import app

AUTH_TAG = "auth"
AUTH_PREFIX = f"/{AUTH_TAG}"

app.include_router(AUTH_ROUTER, prefix=f"{AUTH_PREFIX}/jwt", tags=[AUTH_TAG])
app.include_router(REGISTER_ROUTER, prefix=AUTH_PREFIX, tags=[AUTH_TAG])
app.include_router(RESET_PASSWORD_ROUTER, prefix=AUTH_PREFIX, tags=[AUTH_TAG])
app.include_router(VERIFY_ROUTER, prefix=AUTH_PREFIX, tags=[AUTH_TAG])
app.include_router(USERS_ROUTER, prefix="/users", tags=["users"])
app.include_router(
    GOOGLE_OAUTH_ROUTER, prefix=f"{AUTH_PREFIX}/google", tags=[AUTH_TAG]
)

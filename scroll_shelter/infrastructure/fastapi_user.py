from fastapi_users import FastAPIUsers
from fastapi_users.authentication import JWTAuthentication
from fastapi_users.db import MongoDBUserDatabase
from scroll_shelter.infrastructure.database import CLIENT
from scroll_shelter.infrastructure.google_oauth_client import (
    GOOGLE_OAUTH_CLIENT,
)
from scroll_shelter.infrastructure.web_app import SECRET
from scroll_shelter.interface.user_db import UserDB
from scroll_shelter.usecase.dto import User, UserCreate, UserUpdate

db = CLIENT["database_name"]
collection = db["users"]
user_db = MongoDBUserDatabase(UserDB, collection)
jwt_authentication = JWTAuthentication(
    secret=SECRET, lifetime_seconds=3600, tokenUrl="/auth/jwt/login"
)

fastapi_users = FastAPIUsers(
    user_db,
    [jwt_authentication],
    User,
    UserCreate,
    UserUpdate,
    UserDB,
)

AUTH_ROUTER = fastapi_users.get_auth_router(jwt_authentication)
REGISTER_ROUTER = fastapi_users.get_register_router()
RESET_PASSWORD_ROUTER = fastapi_users.get_reset_password_router(SECRET)
VERIFY_ROUTER = fastapi_users.get_verify_router(SECRET)
USERS_ROUTER = fastapi_users.get_users_router()
OAUTH_ROUTER = fastapi_users.get_oauth_router(GOOGLE_OAUTH_CLIENT, SECRET)
GOOGLE_OAUTH_ROUTER = fastapi_users.get_oauth_router(
    GOOGLE_OAUTH_CLIENT, SECRET
)

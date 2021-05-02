from app.usecase.dto import User
from fastapi_users import models


class UserDB(User, models.BaseUserDB):
    pass

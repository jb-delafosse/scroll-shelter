from fastapi_users import models
from scroll_shelter.usecase.dto import User


class UserDB(User, models.BaseUserDB):
    pass

from app.common.type import UserId
from app.infrastructure.fastapi_user import fastapi_users
from app.infrastructure.web_app import app
from app.usecase.dto import BaseUserDB, FolderCreate, User
from app.usecase.folder import FolderUsecase
from fastapi import APIRouter, Depends
from pydantic import BaseModel, Field

router = APIRouter(
    prefix="/folders",
    tags=["folders"],
)


class FolderCreateMessage(BaseModel):
    provider_id: str = Field(
        ...,
        example="1WEk01UAmDG0RxyDQrcFrBueeeDFTLn2f",
        description="The id of the folder on provider side",
    )
    provider_name: str = Field(
        ...,
        example="notes",
        description="The name of the folder on provider side",
    )


class FolderCreateResponse(BaseModel):
    provider_id: str = Field(
        ...,
        example="1WEk01UAmDG0RxyDQrcFrBueeeDFTLn2f",
        description="The id of the folder on provider side",
    )
    provider_name: str = Field(
        ...,
        example="notes",
        description="The name of the folder on provider side",
    )
    id: str = Field(
        ...,
        example="60ca51d2708c16650ce77d2c",
        description="The id of the folder",
    )


@router.post(path="/")
async def create_folder(
    message: FolderCreateMessage,
    user: BaseUserDB = Depends(fastapi_users.current_user()),
) -> FolderCreateResponse:
    folder = FolderCreate(
        provider_name=message.provider_name,
        provider_id=message.provider_id,
    )
    value = await FolderUsecase(user_id=UserId(user.id)).save_folder(folder)
    return FolderCreateResponse(
        provider_id=value.provider_id,
        provider_name=value.provider_name,
        id=str(value.id),
    )


app.include_router(router)

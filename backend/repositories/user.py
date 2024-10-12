from models.core import PyObjectId
from models.user import USERS_COLLECTION, UpdateUserRequest, UserCreate, UserInDB
from pydantic import EmailStr
from pymongo.cursor import Cursor
from pymongo.database import Database
from repositories.base import BaseRepository

COLLECTION_NAME = USERS_COLLECTION


class UserRepository(BaseRepository):
    def __init__(self, db: Database) -> None:
        super().__init__(db)

    async def find_many(self, *, limit: None | int, offset: int = 0) -> list[UserInDB]:
        result_iter: Cursor = super().find_many(
            collection_name=COLLECTION_NAME,
            offset=offset,
            limit=limit,
        )
        return [UserInDB(**result) for result in result_iter]

    async def find_one_filter_by_id(self, *, _id: PyObjectId) -> UserInDB | None:
        result: dict | None = super().find_one_filter_by_id(
            collection_name=COLLECTION_NAME,
            _id=_id,
        )
        return UserInDB(**result) if result else None

    async def find_one_filter_by_email(
        self, *, email: EmailStr | str
    ) -> UserInDB | None:
        result: dict | None = super().find_one(
            collection_name=COLLECTION_NAME, filter_dict={"email": email}
        )
        return UserInDB(**result) if result else None

    async def create_one(
        self,
        *,
        user: UserCreate,
    ) -> PyObjectId:
        created_id: PyObjectId = super().insert_one(
            collection_name=COLLECTION_NAME,
            insert_dict=user.model_dump(),
        )
        return created_id

    async def update_one_filter_by_id(
        self,
        *,
        user: UpdateUserRequest | UserInDB,
        _id: PyObjectId,
    ) -> None:
        update_dict: dict = super().get_update_dict(model=user)
        super().update_one_filter_by_id(
            collection_name=COLLECTION_NAME, _id=_id, update_dict=update_dict
        )

    async def delete_one_filter_by_id(
        self,
        *,
        _id: PyObjectId,
    ) -> None:
        super().delete_one_filter_by_id(collection_name=COLLECTION_NAME, _id=_id)

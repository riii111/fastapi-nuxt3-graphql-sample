from config import app_config
from depends.database import get_repository
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from functions import auth_proc
from functions.exceptions import NotFoundException
from models.core import PyObjectId
from models.user import UserInDB
from repositories.user import UserRepository

oauth2_scheme = OAuth2PasswordBearer(tokenUrl=f"{app_config.API_V1}/auth/login/")


async def verify_user_from_token(
    *,
    token: str = Depends(oauth2_scheme),
    user_repo: UserRepository = Depends(get_repository(UserRepository)),
) -> UserInDB:
    payload = await auth_proc.decode_token(
        token=token, secret_key=str(app_config.SECRET_KEY)
    )
    user_id: PyObjectId = PyObjectId(payload.user_id)
    user_in_db: UserInDB | None = await user_repo.find_one_filter_by_id(_id=user_id)
    if not user_in_db:
        raise NotFoundException(f"user_id: {user_id} のユーザーが見つかりません。")
    return user_in_db


async def verify_current_active_user(
    current_user: UserInDB = Depends(verify_user_from_token),
) -> UserInDB:
    # current_userの情報処理をする場合は以下に記述すること
    return current_user

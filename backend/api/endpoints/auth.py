from config import app_config
from depends.database import get_repository
from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from functions import auth_proc
from functions.exceptions import (
    FailedPreconditionException,
    InvalidArgumentException,
    NotFoundException,
    RouteErrorHandler,
)
from functions.utils import get_now_utc
from models.user import UserInDB, UserViewAuth
from repositories.user import UserRepository
from starlette.status import HTTP_200_OK

router = APIRouter(route_class=RouteErrorHandler)


@router.post(
    "/login/",
    response_model=UserViewAuth,
    status_code=HTTP_200_OK,
)
async def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    user_repo: UserRepository = Depends(get_repository(UserRepository)),
):
    email = form_data.username  # OAuth2PasswordRequestFormの仕様上usernameとなっているがemailを想定
    password = form_data.password

    # 登録ユーザーの確認
    user: UserInDB | None = await user_repo.find_one_filter_by_email(email=email)
    if not user:
        raise NotFoundException("ユーザーが見つかりません。")

    # ログイン失敗回数の確認
    if user and user.login_failure_count > app_config.MAX_LOGIN_FAILURE_COUNT:
        raise FailedPreconditionException(
            message=f"ログイン失敗回数が{app_config.MAX_LOGIN_FAILURE_COUNT}を超えているため、アカウントをロックしました。解除には問い合わせが必要です。"
        )

    # パスワードの確認
    if not await auth_proc.verify_password(
        password=password, salt=user.salt, hashed_pw=user.hashed_password
    ):
        user.login_failure_count += 1
        await user_repo.update_one_filter_by_id(
            user=user,
            _id=user.id,
        )
        raise InvalidArgumentException("パスワードが一致しません。")

    # ログイン成功処理
    if user.login_failure_count > 0:
        user.login_failure_count = 0
        await user_repo.update_one_filter_by_id(
            user=user,
            _id=user.id,
        )

    user.is_login = True
    user.last_login_time = get_now_utc()
    await user_repo.update_one_filter_by_id(user=user, _id=user.id)

    access_token: str = await auth_proc.create_access_token(user=user)
    refresh_token: str = await auth_proc.create_refresh_token(user=user)

    return UserViewAuth(
        **user.model_dump(by_alias=True),
        access_token=access_token,
        refresh_token=refresh_token,
    )

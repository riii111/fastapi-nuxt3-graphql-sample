from depends.common import ListQuery, list_query
from depends.database import get_repository
from fastapi import APIRouter, Depends
from functions import auth_proc
from functions.exceptions import (
    AlreadyExistsException,
    NotFoundException,
    RouteErrorHandler,
)
from models.core import PyObjectId
from models.user import (
    CreateUserRequest,
    ListUserResponse,
    UpdateUserRequest,
    UserCreate,
    UserInDB,
    UserSecret,
    UserView,
)
from repositories.user import UserRepository
from starlette.status import HTTP_200_OK

router = APIRouter(route_class=RouteErrorHandler)


@router.get(
    "/",
    description="Listメソッド: ユーザーの一覧を取得する",
    response_model=ListUserResponse,
    response_description="ユーザーの一覧",
    status_code=HTTP_200_OK,
)
async def list_users(
    list_query: ListQuery = Depends(list_query),
    user_repo: UserRepository = Depends(get_repository(UserRepository)),
):
    result_iter: list[UserInDB] = await user_repo.find_many(
        limit=list_query.limit, offset=list_query.offset
    )
    users: list[UserView] = [
        UserView(**result.model_dump(by_alias=True)) for result in result_iter
    ]
    return ListUserResponse(users=users)


@router.get(
    "/{user_id}/",
    description="Getメソッド: ユーザーを取得する",
    response_model=UserView,
    response_description="ユーザーの取得",
    status_code=HTTP_200_OK,
)
async def get_user(
    user_id: PyObjectId,
    user_repo: UserRepository = Depends(get_repository(UserRepository)),
) -> UserView:
    user: None | UserInDB = await user_repo.find_one_filter_by_id(_id=user_id)
    if not user:
        raise NotFoundException(message=f"Userリソース 「user_id: {user_id}」 が見つかりません。")
    return UserView(**user.model_dump(by_alias=True))


@router.post(
    "/",
    description="Createメソッド: ユーザーを新規に登録する",
    response_model=UserView,
    response_description="ユーザーの新規登録",
    status_code=HTTP_200_OK,
)
async def create_user(
    request: CreateUserRequest,
    user_repo: UserRepository = Depends(get_repository(UserRepository)),
) -> UserView:
    # ユーザー登録前チェック
    if await user_repo.find_one_filter_by_email(email=request.email):
        raise AlreadyExistsException(f"email: {request.email} はすでに登録されています。")

    # ユーザーのパスワード処理
    user_secret: UserSecret = await auth_proc.create_salt_and_hashed_password(
        plaintext_password=request.password
    )
    user: UserCreate = UserCreate(
        **request.model_dump(),
        hashed_password=user_secret.hashed_password,
        salt=user_secret.salt,
    )

    created_id: PyObjectId = await user_repo.create_one(user=user)
    return await get_user(user_id=created_id, user_repo=user_repo)


@router.put(
    "/{user_id}/",
    description="Updateメソッド: ユーザー情報を更新する",
    response_model=UserView,
    response_description="ユーザー情報を更新",
    status_code=HTTP_200_OK,
)
async def update_user(
    user_id: PyObjectId,
    request: UpdateUserRequest,
    user_repo: UserRepository = Depends(get_repository(UserRepository)),
) -> UserView:
    _ = await user_repo.update_one_filter_by_id(user=request, _id=user_id)
    return await get_user(user_id=user_id, user_repo=user_repo)


@router.delete(
    "/{user_id}/",
    description="Deleteメソッド: ユーザー情報を削除する",
    response_model=None,
    response_description="ユーザー情報を削除",
    status_code=HTTP_200_OK,
)
async def delete_book(
    user_id: PyObjectId,
    user_repo: UserRepository = Depends(get_repository(UserRepository)),
) -> None:
    await user_repo.delete_one_filter_by_id(_id=user_id)
    return

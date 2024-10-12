import re
from datetime import datetime

from functions.exceptions import InvalidArgumentException
from functions.utils import multi_space_to_single
from models.core import DateTimeModelMixin, IDModelMixin
from models.token import AuthToken
from pydantic import BaseModel, EmailStr, Field, computed_field, field_validator

user_name_field: str = Field(None, max_length=100, min_length=1)
password_field: str = Field(None, max_length=100, min_length=8)

USERS_COLLECTION: str = "users"


class UserBase(BaseModel):
    """User基本情報"""

    email: None | EmailStr = Field(None, description="メールアドレス")
    full_name: None | str = Field("田中 太郎", description="フルネーム（スペースを1つ入れること）")

    @field_validator("full_name", mode="before")
    @classmethod  # type: ignore
    def valid_full_name(cls, val: str):
        if val:
            proc_val: str = multi_space_to_single(val).strip()
            splited_name = proc_val.split()
            if splited_name and len(splited_name) != 2:
                raise InvalidArgumentException("full_name は姓名の間をスペースで区切ってください")
            return proc_val
        return val


class UserSecret(BaseModel):
    """シークレット情報"""

    hashed_password: str = Field(..., description="ハッシュ化されたパスワード")
    salt: str = Field(..., description="ソルト")


class UserCreate(UserBase, UserSecret, DateTimeModelMixin):
    """DBにデータを作成する時のモデル"""

    pass


class UserInDB(UserBase, UserSecret, DateTimeModelMixin, IDModelMixin):
    """DBに保管されている状態のモデル"""

    login_failure_count: int = Field(0, description="ログイン失敗回数")
    is_login: bool = Field(False, description="ログイン状態")
    last_login_time: datetime | None = Field(None, description="最終ログイン日時")


class UserView(UserBase, IDModelMixin, DateTimeModelMixin):
    """Get・Create・UpdateメソッドでのAPIレスポンスのビュー"""

    is_login: bool = Field(False, description="ログイン状態")
    last_login_time: datetime | None = Field(None, description="最終ログイン日時")

    def split_name(self, name) -> None | list[str]:
        if name:
            return name.split()
        return None

    @computed_field
    @property
    def first_name(self) -> str | None:
        splited_name: None | list[str] = self.split_name(name=self.full_name)
        if splited_name and len(splited_name) > 0:
            return splited_name[0]  # type: ignore
        return None

    @computed_field
    @property
    def last_name(self) -> str | None:
        splited_name: None | list[str] = self.split_name(name=self.full_name)
        if splited_name and len(splited_name) > 0:
            return splited_name[-1]  # type: ignore
        return None


class UserViewAuth(UserView, AuthToken):
    pass


class ListUserResponse(BaseModel):
    """Listメソッドでのレスポンス"""

    users: list[UserView] = Field([], description="User一覧")

    @computed_field
    @property
    def counts(self) -> int:
        return len(self.users)


class UpdateUserRequest(UserBase):
    """Updateメソッドのリクエスト"""

    pass


class CreateUserRequest(UserBase):
    """Createメソッドのリクエスト"""

    email: EmailStr = Field(description="メールアドレス")
    password: str = Field("P@ssw0rd", max_length=100, description="パスワード")

    @field_validator("password", mode="before")
    @classmethod  # type: ignore
    def check_password(cls, val: str) -> str:
        # 空文字の確認
        if re.search(r"\s+", val):
            raise InvalidArgumentException("passwordにはスペース等の空文字を含めないでください。")
        # 数字を含む
        if not re.search("[0-9]", val):
            raise InvalidArgumentException("passwordには半角数字を1つ以上含めてください。")
        # 大文字を含む
        if not re.search("[A-Z]", val):
            raise InvalidArgumentException("passwordには半角の大文字アルファベットを1つ以上含めてください。")
        # 小文字を含む
        if not re.search("[a-z]", val):
            raise InvalidArgumentException("passwordには半角の小文字アルファベットを1つ以上含めてください。")
        # 半角記号を含む
        if not re.search("[!-/:-@[-`{-~]", val):
            raise InvalidArgumentException("passwordには半角記号を1つ以上含めてください。")
        return val

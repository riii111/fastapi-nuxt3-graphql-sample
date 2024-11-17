from pydantic import BaseModel, Field, computed_field

from .core import DateTimeModelMixin, IDModelMixin

BOOK_COLLECTION = "books"


class BookBase(BaseModel):
    """Book基本情報"""

    name: str = Field("", description="本のタイトル")
    price_without_tax: int = Field(0, description="税抜価格")
    tax_rate: float = Field(0.1, description="税率")


class BookSecret(BaseModel):
    """一般には非公開な情報のモデル"""

    secret: None | str = Field(None, description="ネタバレ")


class BookCreate(BookBase, BookSecret, DateTimeModelMixin):
    """DBにデータを作成する時のモデル"""

    pass


class BookInDB(BookBase, BookSecret, IDModelMixin, DateTimeModelMixin):
    """DBに保管されている状態のモデル"""

    pass


class UpdateBookRequest(BookBase):
    """Updateメソッドのリクエスト"""

    pass


class CreateBookRequest(BookBase):
    """Createメソッドのリクエスト"""

    pass

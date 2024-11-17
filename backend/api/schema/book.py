from models.book import BookInDB
from pydantic import BaseModel, Field, computed_field


class BookResponse(BookInDB):

    # 計算した値を含めたいとき
    @computed_field
    @property
    def price_with_tax(self) -> int:
        # 一般的な四捨五入ではないので実際はこのようにはしないこと
        return int(self.price_without_tax * (1.0 + self.tax_rate))


class ListBookResponse(BaseModel):
    """Listメソッドでのレスポンス"""

    books: list[BookResponse] = Field([], description="Book一覧")

    @computed_field
    @property
    def counts(self) -> int:
        return len(self.books)

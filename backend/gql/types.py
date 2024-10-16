import strawberry
from strawberry import auto, field
from models.book import BookView
from .scalars import ObjectIdScalar


@strawberry.experimental.pydantic.type(model=BookView)
class BookType:
    id: ObjectIdScalar
    name: auto
    price_without_tax: auto
    tax_rate: auto
    created_time: auto
    updated_time: auto

    @field
    def price_with_tax(self) -> int:
        return int(self.price_without_tax * (1.0 + self.tax_rate))

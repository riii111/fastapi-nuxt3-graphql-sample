from typing import Callable, Generator, Type

from db.session import client
from fastapi import Depends
from pymongo.database import Database
from repositories.base import BaseRepository


def get_db() -> Generator:
    db: Database = client.db
    yield db


def get_repository(repogitory_type: Type[BaseRepository]) -> Callable:
    def get_repo(db: Database = Depends(get_db)) -> Type[BaseRepository]:
        return repogitory_type(db)

    return get_repo

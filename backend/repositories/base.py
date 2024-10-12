from typing import Any

from bson.objectid import ObjectId
from config import db_config
from functions.utils import get_now_utc
from models.core import PyObjectId
from pydantic import BaseModel
from pymongo import ASCENDING
from pymongo.command_cursor import CommandCursor
from pymongo.cursor import Cursor
from pymongo.database import Database
from pymongo.results import InsertManyResult, InsertOneResult, UpdateResult


class BaseRepository:
    """DBにリクエストし、そのレスポンスをリターンするベースクラス"""

    def __init__(self, db: Database) -> None:
        self.db = db
        self.bulk_limit = db_config.BULK_LIMIT

    def get_update_dict(
        self, *, model: BaseModel, exclude_unset: bool = True, exclude: set = {"id"}
    ) -> dict:
        """Update時に必要な情報を含むdictを返す"""
        model_dict: dict = model.model_dump(
            by_alias=True,
            exclude=exclude,
            exclude_unset=exclude_unset,
        )
        model_dict["updated_time"] = get_now_utc()
        return model_dict

    def find_many(
        self,
        *,
        collection_name: str,
        filter_dict: dict[str, Any] | None = None,
        sort_list: list[tuple[str, Any]] = [
            ("created_at", ASCENDING),
            ("_id", ASCENDING),
        ],
        projection: dict[str, Any] | None = None,
        offset: int = 0,
        limit: None | int = None,
    ) -> Cursor:
        cursor = (
            self.db[collection_name]
            .find(
                filter=filter_dict,
                sort=sort_list,
                projection=projection,
            )
            .skip(offset)
        )
        if limit and limit > 0:
            cursor.limit(limit)
        return cursor

    def find_one(
        self,
        *,
        collection_name: str,
        filter_dict: dict[str, Any],
    ) -> dict | None:
        return self.db[collection_name].find_one(filter=filter_dict)

    def find_one_filter_by_id(
        self,
        *,
        collection_name: str,
        _id: PyObjectId,
    ) -> dict | None:
        return self.find_one(
            collection_name=collection_name,
            filter_dict={"_id": ObjectId(_id)},
        )

    def find_many_by_id(
        self,
        *,
        collection_name: str,
        _id_list: list[PyObjectId],
    ) -> Cursor:
        return self.db[collection_name].find(
            filter={"_id": {"$in": _id_list}},
        )

    def insert_one(
        self,
        *,
        collection_name: str,
        insert_dict: dict[str, Any],
    ) -> PyObjectId:
        result: InsertOneResult = self.db[collection_name].insert_one(insert_dict)
        return result.inserted_id

    def insert_many(
        self,
        *,
        collection_name: str,
        insert_dict_list: list[dict[str, Any]],
    ) -> list[PyObjectId]:
        result: InsertManyResult = self.db[collection_name].insert_many(
            insert_dict_list
        )
        return result.inserted_ids

    def update_one(
        self, *, collection_name: str, update_dict: dict, filter_dict: dict
    ) -> UpdateResult:
        return self.db[collection_name].update_one(
            filter=filter_dict, update={"$set": update_dict}
        )

    def update_one_filter_by_id(
        self,
        *,
        collection_name: str,
        update_dict: dict,
        _id: PyObjectId,
    ) -> UpdateResult:
        return self.update_one(
            collection_name=collection_name,
            update_dict=update_dict,
            filter_dict={"_id": ObjectId(_id)},
        )

    def update_many(
        self,
        *,
        collection_name: str,
        update_dict: dict,
        filter_dict: dict,
    ) -> UpdateResult:
        return self.db[collection_name].update_many(
            filter=filter_dict,
            update=update_dict,
        )

    def update_many_filter_by_ids(
        self,
        *,
        collection_name: str,
        update_dict: dict,
        _id_list: list[PyObjectId],
    ) -> UpdateResult:
        return self.update_many(
            collection_name=collection_name,
            update_dict=update_dict,
            filter_dict={"_id": {"$in": _id_list}},
        )

    def delete_many(
        self,
        *,
        collection_name: str,
        filter_dict: dict[str, Any],
    ) -> None:
        self.db[collection_name].delete_many(filter=filter_dict)
        return

    def delete_one_filter_by_id(
        self,
        *,
        collection_name: str,
        _id: PyObjectId,
    ) -> None:
        self.delete_many(
            collection_name=collection_name, filter_dict={"_id": ObjectId(_id)}
        )
        return

    def aggregate(
        self,
        *,
        collection_name: str,
        pipeline_list: list[dict],
    ) -> CommandCursor:
        return self.db[collection_name].aggregate(pipeline_list)

    def count(
        self,
        *,
        collection_name: str,
        filter: dict = {},
    ) -> int:
        return self.db[collection_name].count_documents(filter=filter)

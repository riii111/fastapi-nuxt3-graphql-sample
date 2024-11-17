import urllib

from config import db_config
from pymongo import MongoClient
from pymongo.database import Database


USER_NAME = urllib.parse.quote_plus(db_config.MONGO_INITDB_ROOT_USERNAME)
PASSWORD = urllib.parse.quote_plus(db_config.MONGO_INITDB_ROOT_PASSWORD)
HOST = db_config.MONGO_DATABASE_CONTAINER_NAME
PORT = db_config.MONGO_PORT

MONGO_DATABASE_URL: str = f"mongodb://{USER_NAME}:{PASSWORD}@{HOST}:{PORT}"

client = MongoClient(MONGO_DATABASE_URL)


def get_db() -> Database:
    db: Database = client.db
    return db

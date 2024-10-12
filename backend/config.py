from typing import List, Optional

from pydantic_settings import BaseSettings


class AppConfig(BaseSettings):
    ORIGINS: List[str] = [
        "http://localhost:3000",
        "http://localhost",
    ]
    API_BASE_PATH: str = "/api"
    API_V1: str = f"{API_BASE_PATH}/v1"
    MY_HOST: str = f"http://localhost:8000{API_V1}"
    # フロントエンド情報
    FRONTEND_HOST: str = "http://localhost:3000"
    # メール情報
    MAIL_SIGNATURE: str = "hoge"
    # JWT
    SECRET_KEY: str = ""
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60
    REFRESH_TOKEN_EXPIRE_MINUTES: int = 1 * 24 * 60
    JWT_ISSUER: str = "app"
    JWT_AUDIENCE: str = "app:auth"
    JWT_ALGORITHM: str = "HS256"
    JWT_TOKEN_PREFIX: str = "Bearer"
    PEPPER: str = ""
    # APIパラメータ
    MAX_LIST_LIMIT: int = 100
    MAX_LOGIN_FAILURE_COUNT: int = 5
    MAX_BATCH_REQUEST: int = 20


class AWSConfig(BaseSettings):
    AWS_DEFAULT_REGION: Optional[str] = "ap-northeast-1"
    AWS_ACCESS_KEY_ID: Optional[str] = None
    AWS_SECRET_ACCESS_KEY: Optional[str] = None
    # SES
    SES_REGION: Optional[str] = "ap-northeast-1"
    SYSTEM_EMAIL_ADDRESS: Optional[str] = "hoge@gmail.com"


class MongoConfig(BaseSettings):
    # mongo
    MONGO_INITDB_DATABASE: str = "app"
    MONGO_INITDB_ROOT_USERNAME: str = ""
    MONGO_INITDB_ROOT_PASSWORD: str = ""
    MONGO_DATABASE_CONTAINER_NAME: Optional[str] = "mongo"
    MONGO_PORT: str = "27017"
    BULK_LIMIT: int = 1000


app_config = AppConfig()
aws_config = AWSConfig()
db_config = MongoConfig()

from datetime import datetime, timedelta

from config import app_config
from pydantic import BaseModel, Field


class JWTMeta(BaseModel):
    iss: str = Field(app_config.JWT_ISSUER, description="発行者")
    aud: str = Field(app_config.JWT_AUDIENCE, description="利用者")
    iat: float = Field(datetime.timestamp(datetime.utcnow()), description="発行日時")
    exp: float = Field(
        datetime.timestamp(
            datetime.utcnow()
            + timedelta(minutes=app_config.ACCESS_TOKEN_EXPIRE_MINUTES)
        ),
        description="失効日時",
    )


class JWTCreds(BaseModel):
    user_id: str = Field(description="ユーザーID")


class JWTPayload(JWTMeta, JWTCreds):
    pass


class AuthToken(BaseModel):
    access_token: str = Field(description="アクセストークン")
    refresh_token: str = Field(description="リフレッシュトークン")
    token_type: str = Field("Bearer", description="トークンタイプ")

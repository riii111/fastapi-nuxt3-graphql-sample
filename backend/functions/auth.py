import random
import string
from datetime import datetime, timedelta

import bcrypt
from config import app_config
from functions.exceptions import UnauthenticatedException
from jose import jwt
from models.token import JWTCreds, JWTMeta, JWTPayload
from models.user import UserInDB, UserSecret
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class AuthProcess:
    async def decode_token(self, *, token: str, secret_key: str) -> JWTPayload:
        try:
            decoded_token = jwt.decode(
                token,
                str(secret_key),
                audience=app_config.JWT_AUDIENCE,
                algorithms=[app_config.JWT_ALGORITHM],
            )
            payload: JWTPayload = JWTPayload(**decoded_token)
            return payload
        except Exception as e:
            raise UnauthenticatedException(
                message="トークンがない、無効、または期限切れのためにリクエストが認証できません。", raw_error=e
            )

    async def create_salt_and_hashed_password(
        self, plaintext_password: str
    ) -> UserSecret:
        salt = await self.generate_salt()
        hashed_password = await self.hash_password(
            password=plaintext_password, salt=salt
        )
        return UserSecret(salt=salt, hashed_password=hashed_password)

    async def generate_salt(self) -> str:
        return bcrypt.gensalt().decode()

    async def hash_password(self, password: str, salt: str) -> str:
        return pwd_context.hash(password + salt + app_config.PEPPER)

    async def verify_password(self, password: str, salt: str, hashed_pw: str) -> bool:
        return pwd_context.verify(password + salt + app_config.PEPPER, hashed_pw)

    async def create_token(
        self,
        user: UserInDB,
        expires_minutes: int,
    ) -> str:
        jwt_meta = JWTMeta(
            aud=app_config.JWT_AUDIENCE,
            iat=datetime.timestamp(datetime.utcnow()),
            exp=datetime.timestamp(
                datetime.utcnow() + timedelta(minutes=expires_minutes)
            ),
        )

        jwt_creds = JWTCreds(user_id=str(user.id))
        token_payload = JWTPayload(**jwt_meta.model_dump(), **jwt_creds.model_dump())
        token = jwt.encode(
            token_payload.model_dump(),
            app_config.SECRET_KEY,
            algorithm=app_config.JWT_ALGORITHM,
        )
        return token

    async def create_access_token(
        self,
        user: UserInDB,
    ) -> str:
        return await self.create_token(
            user=user, expires_minutes=app_config.ACCESS_TOKEN_EXPIRE_MINUTES
        )

    async def create_refresh_token(
        self,
        user: UserInDB,
    ) -> str:
        return await self.create_token(
            user=user, expires_minutes=app_config.REFRESH_TOKEN_EXPIRE_MINUTES
        )


async def generate_random_password(length: int = 12) -> str:
    characters = list(string.ascii_letters + string.digits)
    random.shuffle(characters)
    password: str = "".join(characters[:length])
    return password

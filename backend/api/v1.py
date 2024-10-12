from api.endpoints import auth, batch, book, user
from fastapi import APIRouter

api_router = APIRouter()

api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
api_router.include_router(user.router, prefix="/users", tags=["user"])
api_router.include_router(book.router, prefix="/books", tags=["book"])
api_router.include_router(batch.router, prefix="/batch", tags=["batch"])

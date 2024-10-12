from api import v1
from config import app_config
from db.session import client
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Sample API",
    swagger_ui_parameters={"deepLinking": False},
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=app_config.ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(v1.api_router, prefix=app_config.API_V1)


@app.on_event("shutdown")
def shutdown_event():
    client.close()


@app.get("/")
def read_root():
    return "FastAPI-Nuxt3-GraphQL-Sample"

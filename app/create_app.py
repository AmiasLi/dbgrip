from fastapi import FastAPI

from app.api.api_v1.api import api_router
from app.core.config.config import get_settings


def create_app():
    settings = get_settings()

    settings.init_logging()
    app = FastAPI(**settings.app_kwargs)

    app.include_router(api_router, prefix=settings.API_V1_STR)

    return app

import logging
import sys
from enum import Enum
from typing import List, Tuple, Dict, Any
from pydantic_settings import BaseSettings
from app.core.logger import InterceptHandler
from loguru import logger


class Envs(Enum):
    dev: str = "dev"
    prod: str = "prod"


class Settings(BaseSettings):
    APP_NAME: str = "DBGrip"
    APP_DESCRIPTION: str = "MongoDB query platform."
    APP_VERSION: str = "0.0.1"
    LOGGING_LEVEL: int = logging.INFO
    DEBUG: bool = True
    LOGGERS: Tuple[str, str] = ("uvicorn.asgi", "uvicorn.access")
    ORIGINS: List[str] = ["*"]

    APP_HOST: str = "0.0.0.0"
    APP_PORT: int = 8097
    APP_ENV: Envs = Envs.dev

    OPENAPI_URL: str = "/openapi.json"
    ROOT_PATH: str = ""
    DOCS_URL: str = "/docs"
    API_V1_STR: str = "/api/v1"

    SQLALCHEMY_DATABASE_URL: str = ""

    @property
    def app_kwargs(self) -> Dict[str, Any]:
        return {
            "debug": self.DEBUG,
            "docs_url": self.DOCS_URL,
            "root_path": self.ROOT_PATH,
            "openapi_url": self.OPENAPI_URL,
            "name": self.APP_NAME,
            "version": self.APP_VERSION,
            "description": self.APP_DESCRIPTION,

        }

    def init_logging(self) -> None:
        logging.getLogger('apscheduler').setLevel(self.LOGGING_LEVEL)
        logging.getLogger().handlers = [InterceptHandler()]
        for logger_name in self.LOGGERS:
            logging_logger = logging.getLogger(logger_name)
            logging_logger.handlers = [InterceptHandler(level=self.LOGGING_LEVEL)]

        logger.configure(handlers=[{"sink": sys.stderr, "level": self.LOGGING_LEVEL}])

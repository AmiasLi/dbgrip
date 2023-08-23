import logging
from app.core.config.base import Settings


class DevSettings(Settings):
    DEBUG: bool = True
    LOGGING_LEVEL: int = logging.DEBUG
    SQLALCHEMY_DATABASE_URL: str = "mysql+pymysql://dbo:123456Aa@192.168.124.64:3306/db_grip"

import logging
from app.core.config.base import Settings


class PrdSettings(Settings):
    LOGGING_LEVEL: int = logging.INFO
    SQLALCHEMY_DATABASE_URL: str = "mysql+pymysql://mon_dbo:123456Aa@localhost:3306/mdb_metadata"

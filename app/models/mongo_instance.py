from app.db.mysql.session_local import Base
from sqlalchemy import Column, Integer, SmallInteger, String, DateTime, JSON
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime


class MongoInstanceModel(Base):
    __tablename__ = "mongo_instance"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name = Column(String(50), unique=True, index=True)
    host = Column(String(50), nullable=False)
    port = Column(Integer, nullable=False)
    username = Column(String(50), nullable=False)
    password = Column(String(50), nullable=False)
    db = Column(String(50), nullable=False)
    auth_source = Column(String(50), nullable=False)
    auth_mechanism = Column(String(50), nullable=False)
    kwargs = Column(JSON, nullable=True)
    create_at = Column(DateTime, default=datetime.now)
    update_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    create_by = Column(String(50), nullable=True)
    update_by = Column(String(50), nullable=True)
    status = Column(SmallInteger, default=1)
    remark = Column(String(100), nullable=True)
    __table_args__ = ({'comment': 'mongo实例表'})

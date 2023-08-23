from app.db.mysql.session_local import Base
from sqlalchemy import Column, Integer, SmallInteger, String, DateTime
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime


class MongoInstanceModel(Base):
    __tablename__ = "mongo_instance"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(50), unique=True, index=True)
    host: Mapped[str] = mapped_column(String(50), nullable=False)
    host_ip: Mapped[str] = mapped_column(String(50), nullable=False)
    port: Mapped[int] = mapped_column(Integer, nullable=False)
    create_time = Column(DateTime, default=datetime.now)
    update_time = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    create_by = Column(String(50), nullable=True)
    update_by = Column(String(50), nullable=True)
    status = Column(SmallInteger, default=1)
    remark = Column(String(100), nullable=True)
    __table_args__ = ({'comment': 'mongo实例表'})

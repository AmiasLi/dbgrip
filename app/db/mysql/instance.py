from app.models.mongo_instance import MongoInstanceModel
from sqlalchemy.orm import Session

from app.schemas.mongo_instance import MongoInstance


class MongoInstanceService:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return self.db.query(MongoInstanceModel).all()

    def get_by_id(self, instance_id: int):
        return self.db.query(MongoInstanceModel).filter(
            MongoInstanceModel.id == instance_id).first()

    def get_by_name(self, name: str):
        return self.db.query(MongoInstanceModel).filter(
            MongoInstanceModel.name == name).first()

    def get_by_host(self, host: str):
        return self.db.query(MongoInstanceModel).filter(
            MongoInstanceModel.host == host).first()

    def get_by_host_port(self, host_ip: str, port: int):
        return self.db.query(MongoInstanceModel).filter(
            MongoInstanceModel.host_ip == host_ip,
            MongoInstanceModel.port == port).first()

    def create(self, instance: MongoInstance):
        db_instance = MongoInstanceModel(**instance.model_dump())
        self.db.add(db_instance)
        self.db.commit()
        self.db.refresh(db_instance)
        return db_instance

    def remove(self, instance: MongoInstanceModel):
        instance.status = 0
        self.db.commit()
        self.db.refresh(instance)
        return instance

    def update(self, instance: MongoInstanceModel):
        self.db.commit()
        self.db.refresh(instance)
        return instance

    def update_by_id(self, instance_id: int, instance: MongoInstanceModel):
        db_instance = self.get_by_id(instance_id)
        if db_instance:
            db_instance.name = instance.name
            db_instance.host = instance.host
            db_instance.host_ip = instance.host_ip
            db_instance.port = instance.port
            db_instance.update_at = instance.update_at
            db_instance.update_by = instance.update_by
            db_instance.status = instance.status
            db_instance.remark = instance.remark
            self.db.commit()
            self.db.refresh(db_instance)
            return db_instance
        return None

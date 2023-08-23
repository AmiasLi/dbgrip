from app.models.mongo_instance import MongoInstanceModel
from app.schemas.mongo_instance import MongoInstanceCreate
from sqlalchemy.orm import Session


def create_mongodb_instance(instance: MongoInstanceCreate, db: Session) -> None:
    mongo_instance = MongoInstanceModel(**instance.model_dump())
    db.add(mongo_instance)
    db.commit()
    db.refresh(mongo_instance)


def remove_mongodb_instance(instance_id: int, db: Session):
    mongo_instance = db.query(
        MongoInstanceModel
    ).filter(MongoInstanceModel.id == instance_id).first()

    if not mongo_instance:
        raise Exception('Database not found')

    try:
        db.delete(mongo_instance)
        db.commit()
    except Exception as e:
        raise e

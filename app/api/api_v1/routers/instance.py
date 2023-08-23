from fastapi import APIRouter, Depends, status, HTTPException
from app.schemas.mongo_instance import MongoInstance
from app.db.mysql.session_local import get_db
from sqlalchemy.orm import Session
from app.db.mysql.instance import MongoInstanceService

router = APIRouter()


@router.get('/instances', response_model=list[MongoInstance])
async def get_mongo_instance(db: Session = Depends(get_db)):
    service = MongoInstanceService(db)

    if not service.get_all():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='Mongo instance not found')

    return service.get_all()


@router.post('/instance',
             status_code=status.HTTP_201_CREATED,
             response_model=MongoInstance, )
async def add_mongo_instance(instance: MongoInstance, db: Session = Depends(get_db)):
    service = MongoInstanceService(db)
    db_instance = service.get_by_host_port(instance.host_ip, instance.port)
    if db_instance:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail='Mongo instance already exists')

    return service.create(instance)
